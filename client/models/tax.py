from django.db import models
from client.models import Customer, customer

class Tax(models.Model):
    tax_rate = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)