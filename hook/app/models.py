from django.db import models

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=255, blank=True)
    time = models.CharField(max_length=255, blank=True)
    branch = models.CharField(max_length=255, blank=True)
    message = models.CharField(max_length=255, blank=True)

