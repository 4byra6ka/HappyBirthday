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


class EmployeesCreateView(CreateView):
    """Создание сотрудника"""
    model = Employees
    extra_context = {
        'title': 'Добавить сотрудника'
    }
    form_class = EmployeesCreateForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('employees:list')


class EmployeesUpdateView(UpdateView):
    """Обновление сотрудника"""
    model = Employees
    form_class = EmployeesCreateForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = f'Изменение данных {context['object'].first_name} {context['object'].last_name}'
        return context

    def get_success_url(self):
        return reverse_lazy('employees:list')


class EmployeesDeleteView(DeleteView):
    """Удаление сотрудника"""
    model = Employees
    success_url = reverse_lazy('employees:list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = f'Удаление сотрудника {context['object'].first_name} {context['object'].last_name}'
        context['object_list'] = Employees.objects.all()
        return context
