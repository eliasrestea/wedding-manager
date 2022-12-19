from django.urls import path
from django.views.generic import TemplateView

from weddingmanager.planner.views import (
    OrderCreateView,
    VenueDetailView,
    VenueServicesView,
)

app_name = "planner"

urlpatterns = [
    path("venue-detail/<slug:slug>/", VenueDetailView.as_view(), name="venueDetail"),
    path(
        "servicesDetail/<slug:slug>/",
        VenueServicesView.as_view(),
        name="servicesDetail",
    ),
    path(
        "success/",
        TemplateView.as_view(template_name="planner/order_success.html"),
        name="success",
    ),
    path("create/", OrderCreateView.as_view(), name="create"),
]
