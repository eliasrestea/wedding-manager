from django.urls import path

from weddingmanager.venues.views import (
    ServiceFile,
    VenueCreate,
    VenueDetailView,
    VenueServicesView,
)

app_name = "venues"

urlpatterns = [
    path("venue-detail/<slug:slug>/", VenueDetailView.as_view(), name="venueDetail"),
    path(
        "services-detail/<slug:slug>/",
        VenueServicesView.as_view(),
        name="servicesDetail",
    ),
    path("venue-create/", VenueCreate.as_view(), name="venueCreate"),
    path("service-file/<slug:slug>/", ServiceFile.as_view(), name="serviceFile"),
]
