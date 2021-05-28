from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, default = 1, null = True, on_delete = models.SET_NULL)
    
   
   
    def __str__(self):
        return self.title
