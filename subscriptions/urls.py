from django.urls import path

from subscriptions.apps import SubscriptionsConfig
from subscriptions.views import SubscriptionsListView, SubscriptionsCreateView, SubscriptionsDeleteView, \
    SubscriptionsUpdateView

app_name = SubscriptionsConfig.name

urlpatterns = [
    path("", SubscriptionsListView.as_view(), name="list"),
    path("create/<int:pk>", SubscriptionsCreateView.as_view(), name="create"),
    path("update/<int:pk>/", SubscriptionsUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", SubscriptionsDeleteView.as_view(), name="delete"),
]
