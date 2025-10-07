from django.db import models

# Create your models here.
class ChatUser(models.Model):
    username = models.CharField(max_length=150, unique=True, null=False)
    xconnect_number = models.CharField(max_length=20, unique=True, )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username