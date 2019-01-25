from django.db import models

# Create your models here.
class user(models.Model):
    IP = models.GenericIPAddressField(max_length=60)
    name = models.CharField(max_length=50)
