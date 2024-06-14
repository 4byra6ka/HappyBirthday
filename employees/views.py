from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from employees.forms import EmployeesCreateForm
from employees.models import Employees


class EmployeesListView(ListView):
    """Просмотр рассылок"""
    model = Employees
    extra_context = {
        'title': 'Сотрудники'
    }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['object_list'] = Employees.objects.all()
        return context


class EmployeesCreateView(LoginRequiredMixin, CreateView):
    """Создание сотрудника"""
    login_url = "/users/"
    model = Employees
    extra_context = {
        'title': 'Добавить сотрудника'
    }
    form_class = EmployeesCreateForm

    def get_context_data(self, *args, **kwargs):
        if self.request.user.is_staff:
            context = super().get_context_data(*args, **kwargs)
        else:
            raise PermissionDenied()
        return context

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employees:list')


class EmployeesUpdateView(LoginRequiredMixin, UpdateView):
    """Обновление сотрудника"""
    login_url = "/users/"
    model = Employees
    form_class = EmployeesCreateForm

    def get_context_data(self, *args, **kwargs):
        if self.request.user.is_staff:
            context = super().get_context_data(*args, **kwargs)
            context['title'] = f'Изменение данных {context['object'].first_name} {context['object'].last_name}'
        else:
            raise PermissionDenied()
        return context

    def get_success_url(self):
        return reverse_lazy('employees:list')


class EmployeesDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление сотрудника"""
    login_url = "/users/"
    model = Employees
    success_url = reverse_lazy('employees:list')

    def get_context_data(self, *args, **kwargs):
        if self.request.user.is_staff:
            context = super().get_context_data(*args, **kwargs)
            context['title'] = f'Удаление сотрудника {context['object'].first_name} {context['object'].last_name}'
            context['object_list'] = Employees.objects.all()
        else:
            raise PermissionDenied()
        return context
