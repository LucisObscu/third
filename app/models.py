from django.db import models

# Create your models here.

class Lost_ark(models.Model):
    name = models.CharField(max_length=10)
    count = models.IntegerField()

class Address(models.Model):
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.address