from django.urls import path
from django.views.generic import TemplateView

from weddingmanager.orders.views import OrderCreateView, OrderDetailView

app_name = "orders"

urlpatterns = [
    path(
        "success/",
        TemplateView.as_view(template_name="orders/order_success.html"),
        name="success",
    ),
    path("create/", OrderCreateView.as_view(), name="create"),
    path("order-view/<str:username>/", OrderDetailView.as_view(), name="order-view"),
]
