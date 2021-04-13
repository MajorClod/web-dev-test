from django.db import models

# Create your models here.
class Account(models.Model):
    domain = models.CharField(max_length=255)
    start_date = models.DateField()
    