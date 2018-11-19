from django.db import models

# Create your models here.

class Lost_ark(models.Model):
    name = models.CharField(max_length=10)
    count = models.IntegerField()

class Address(models.Model):
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.address

class House(models.Model):
    number = models.IntegerField()
    address = models.ForeignKey(Address,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number) + self.address.address

# Address.objects.create(address='부산시청')
#  a=Address.objects.get(address='부산시청')
#House.objects.create(number=101,address=a)

#h=House.objects.get(number=101)
# h.address