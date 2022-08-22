from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Message(models.Model):
    host = models.ForeignKey(User, related_name='sender', on_delete=models.SET_NULL, null=True)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.SET_NULL, null=True)
    seen = models.BooleanField(default=False)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content[0:25]


class Draft(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    header = models.CharField(max_length=200)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content[0:25]