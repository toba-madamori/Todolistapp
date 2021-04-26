from django.db import models
from django.urls import reverse
# Create your models here.

class Todo(models.Model):
    title= models.CharField(max_length=200)
    note= models.TextField(null= True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')    
