from django.urls import path
from .views import NotificationCreateAPIView

urlpatterns = [
    path(
        "send",
        NotificationCreateAPIView.as_view(),
        name="notification_create_api",
    ),
]
