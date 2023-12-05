from rest_framework.generics import CreateAPIView
from .models import Notification
from .serializers import NotificationSerializer

class NotificationCreateAPIView(CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
