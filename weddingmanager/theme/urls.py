from django.urls import path

from weddingmanager.theme.views import (
    DecorItemDeleteView,
    DecorItemFile,
    DecorItemSelectionView,
    ThemeOrderView,
)

app_name = "theme"

urlpatterns = [
    path("order-theme/<str:username>/", ThemeOrderView.as_view(), name="orderTheme"),
    path("decor-item-file/<int:pk>/", DecorItemFile.as_view(), name="decorItemFile"),
    path(
        "select-decor-items/",
        DecorItemSelectionView.as_view(),
        name="select-decor-items",
    ),
    path("delete-decor-item/", DecorItemDeleteView.as_view(), name="delete-decor-item"),
]
