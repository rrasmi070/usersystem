from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pic(models.Model):
    pcid = models.OneToOneField(User, on_delete=models.CASCADE)
    pc = models.FileField(upload_to="Profile",max_length=50)