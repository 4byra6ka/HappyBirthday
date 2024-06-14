import uuid

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, FormView, CreateView

from employees.models import Employees
from users.forms import UserRegisterForm, UserProfileForm, UserRecoveryPasswordForm, UserLoginForm
from users.models import User
from users.tasks import send_notification_users


class CustomLoginView(FormView):
    """Контроллер входа пользователя"""
    model = User
    template_name = 'users/login.html'
    form_class = UserLoginForm
    extra_context = {
        'title': 'Войти'
    }

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            return redirect('main:main')
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = User.objects.get(username=username)
                if not user.is_active:
                    messages.add_message(self.request, messages.WARNING, 'Не пройдена верификация или пользователь заблокирован')
                    return render(
                        self.request, 'users/login.html', context={'form': form})
                if user.check_password(password):
                    login(self.request, user)
                    return redirect('main:main')
                else:
                    messages.add_message(self.request, messages.WARNING, 'Неправельный пользователь или пароль')
            except:
                messages.add_message(self.request, messages.WARNING, 'Неправельный пользователь или пароль')
            else:
                message = 'Login failed!'
        return render(
            self.request, 'users/login.html', context={'form': form})


class RegisterView(CreateView):
    """Контроллер регистрации пользователя"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    extra_context = {
        'title': 'Регистрация'
    }

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.is_active = False
            self.object.register_uuid = uuid.uuid4().hex
            self.object.save()
            current_site = get_current_site(self.request)
            send_notification_users.delay(
                subject='Верификация пользователя',
                message=f'Верификация пользователя пройдите по ссылке http://{current_site}{reverse_lazy(
                    "users:success_register", kwargs={"register_uuid": self.object.register_uuid})}',
                recipient_list=[self.object.email]
            )
            return super().form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                             f'Пользователь создан. Пройдите верификацию. Данные направлена на Email: {self.object.email}')
        return reverse_lazy('users:login')


def verification_user(request, *args, **kwargs):
    """Функция верификации пользователя"""
    user = User.objects.get(register_uuid=kwargs['register_uuid'])
    if user.register_uuid == kwargs['register_uuid']:
        user.is_active = True
        user.save()
        Employees.objects.get_or_create(
            first_name=user.first_name,
            last_name=user.last_name,
            birthday=user.birthday,
            email=user.email,
            telegram=user.telegram,
            owner=user,
        )
        messages.add_message(request, messages.INFO, f'Учетная запись {user.username} активирована')
    return redirect(reverse('users:login'))


class ProfileView(LoginRequiredMixin, UpdateView):
    """Обновление профиля"""
    login_url = "/users/"
    model = User
    form_class = UserProfileForm
    extra_context = {
        'title': 'Данные профиля'
    }

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        user = User.objects.get(id=self.request.user.pk)
        user.employees.first_name = user.first_name
        user.employees.last_name = user.last_name
        user.employees.birthday = user.birthday
        user.employees.email = user.email
        user.employees.telegram = user.telegram
        user.employees.save()
        messages.add_message(self.request, messages.INFO, 'Данные профиля изменены')
        return reverse_lazy('users:profile')


class RecoveryPasswordView(FormView):
    """Контроллер восстановления пароля"""
    model = User
    template_name = 'users/recovery_password.html'
    form_class = UserRecoveryPasswordForm
    extra_context = {
        'title': 'Восстановление пароля'
    }

    def form_valid(self, form, *args, **kwargs):
        try:
            recovery_user = User.objects.get(username=form.cleaned_data['username_recovery'])
            self.object = form
            if recovery_user and form.is_valid():
                password = User.objects.make_random_password()
                recovery_user.set_password(password)
                recovery_user.save()
                send_notification_users.delay(
                    subject='Новый пароль',
                    message=f'Ваш новый пароль: {password}',
                    recipient_list=[recovery_user.email]
                )
                return super().form_valid(form, *args, **kwargs)
        except:
            messages.add_message(self.request, messages.WARNING, 'Неправельный логин')
        return super().form_invalid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                             f'Пароль направлен на Email')
        return reverse_lazy('users:login')
