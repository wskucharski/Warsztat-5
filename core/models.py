from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Photo(models.Model):
    file = models.ImageField(upload_to='photos')
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

