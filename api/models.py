from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    user_id = models.IntegerField(unique=False)
    title = models.CharField(max_length = 200)
    note = models.CharField(max_length=500)
    completed = models.BooleanField(default= False, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    