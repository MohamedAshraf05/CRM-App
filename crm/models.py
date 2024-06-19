from typing import Iterable
from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    nationalID = models.CharField(max_length=14)
    Custom_id = models.PositiveIntegerField(unique=True , null=True , blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self,*args , **kwargs):
        if self.Custom_id is None:
            last_customer = Customer.objects.all().order_by('Custom_id').last()
            if last_customer :
                self.Custom_id = last_customer.Custom_id + 1
            else:
                self.Custom_id = 1
        super().save(*args , **kwargs)