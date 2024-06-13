from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from employees.models import Employees
from subscriptions.forms import SubscriptionsCreateForm
from subscriptions.models import Subscriptions
from subscriptions.services import create_periodic_task


class SubscriptionsListView(ListView):
    """Просмотр рассылок"""
    model = Subscriptions
    extra_context = {
        'title': 'Подписки на ДР'
    }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.is_staff:
            context['object_list'] = Subscriptions.objects.all()
        else:
            context['object_list'] = Subscriptions.objects.filter(employees= self.request.user)
        return context


class SubscriptionsCreateView(LoginRequiredMixin, CreateView):
    """Создание рассылки"""
    model = Subscriptions
    extra_context = {
        'title': 'Подписаться'
    }
    form_class = SubscriptionsCreateForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['birthday_person'] = Employees.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.birthday_person = Employees.objects.get(pk=self.kwargs['pk'])
        form.instance.employees = self.request.user
        self.object = form.save()
        self.object.save()
        self.object.task = create_periodic_task(self.object.pk, self.object.notification)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('subscriptions:list')


class SubscriptionsUpdateView(LoginRequiredMixin, UpdateView):
    """Обновление рассылки"""
    model = Subscriptions
    form_class = SubscriptionsCreateForm

    def form_valid(self, form):
        self.object.task.delete()
        self.object.task = create_periodic_task(self.object.pk, self.object.notification)
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = f'Изменение подписки {context['object'].birthday_person}'
        return context

    def get_success_url(self):
        return reverse_lazy('subscriptions:list')


class SubscriptionsDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление рассылки"""
    model = Subscriptions
    success_url = reverse_lazy('subscriptions:list')

    def form_valid(self, form):
        self.object.task.delete()
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = f'Отписаться от рассылки {context['object'].birthday_person}'
        if self.request.user.is_staff:
            context['object_list'] = Subscriptions.objects.all()
        else:
            context['object_list'] = Subscriptions.objects.filter(employees=self.request.user)
        return context
