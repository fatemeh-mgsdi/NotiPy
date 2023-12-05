from django.db import models

class EmailTemplate(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subject = models.CharField(max_length=255)
    template = models.TextField()

    def __str__(self):
        return self.name

class Notification(models.Model):
    message = models.TextField(blank=True, null=True)
    receiver = models.EmailField()
    status = models.CharField(max_length=50, default='pending')
    template = models.ForeignKey('EmailTemplate', on_delete=models.CASCADE)

    def __str__(self):
        return self.topic
