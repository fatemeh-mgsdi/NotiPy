from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Notification

@receiver(post_save, sender=Notification)
def send_notification_email(sender, instance, created, **kwargs):
    if instance.status != 'pending':
        return
    email_template = instance.template
    subject = email_template.subject

    try:
        message = email_template.template.format(token=instance.message)
        recipient_list = [instance.receiver]
        send_mail(subject=subject, message=message, recipient_list=recipient_list)
        instance.status = 'sent'
        instance.save()
    except Exception as ex:
        print(f"An error occured, {str(ex)}")
