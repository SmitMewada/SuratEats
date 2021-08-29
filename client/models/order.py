from django.db import models
from client.models import Dish, Customer, Restaurant, Transaction, Address
import datetime

class Order(models.Model):
    qty = models.IntegerField()
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    order_date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.FloatField()
    phone = models.IntegerField()
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    tax_rate = models.IntegerField(default=15)
    isPaid = models.BooleanField(default=False)
