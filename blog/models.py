from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=100)
    blog = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title