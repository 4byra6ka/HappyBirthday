from django.urls import path

from employees.apps import EmployeesConfig
from employees.views import EmployeesListView, EmployeesCreateView, EmployeesUpdateView, EmployeesDeleteView

app_name = EmployeesConfig.name

urlpatterns = [
    path("", EmployeesListView.as_view(), name="list"),
    path("create/", EmployeesCreateView.as_view(), name="create"),
    path("<int:pk>/update/", EmployeesUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", EmployeesDeleteView.as_view(), name="delete"),
]
