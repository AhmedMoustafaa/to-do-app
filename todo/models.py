from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Todo(models.Model):
    item = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'todos'
    
    def __str__(self):
        return self.item

    def get_absolute_url(self):
        reverse('home')
