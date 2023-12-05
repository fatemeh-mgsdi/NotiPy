from django.contrib import admin

# Register your models here.
from .models import Notification, EmailTemplate

admin.site.register(Notification)
admin.site.register(EmailTemplate)