from django.db import models
from accounts.models import User
# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=300, null=True)
    text = models.CharField(max_length=500, null=True)
    userRead = models.BooleanField(default=False)
    adminRead = models.BooleanField(default=False)
    createdAt= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title