from django.db import models
from client.models import Customer

class Transaction(models.Model):
    order_qty = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, default=None)
