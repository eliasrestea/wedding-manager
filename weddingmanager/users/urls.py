from django.urls import path

from weddingmanager.users.views import (
    UserListView,
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("user-list/", view=UserListView.as_view(), name="userList"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
