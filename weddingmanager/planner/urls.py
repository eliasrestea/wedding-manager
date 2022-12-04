from django.urls import path

from weddingmanager.planner.views import OrderCreateView, VenueDetailView

app_name = "planner"

urlpatterns = [
    path("detail/<slug:slug>/", VenueDetailView.as_view(), name="detail"),
    path("create/", OrderCreateView.as_view(), name="create"),
]

htmx_urlpatterns = [
    # path("venue_chosen/", views.venue_chosen, name="venue_chosen")
    # path("services/<int:pk>", views.services, name="services")
]

urlpatterns += htmx_urlpatterns
