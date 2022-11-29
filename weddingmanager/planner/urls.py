from django.urls import path

from weddingmanager.planner.views import EventCreateView

app_name = "planner"

urlpatterns = [
    path("create/", EventCreateView.as_view(), name="create"),
]
