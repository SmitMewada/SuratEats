from client.models.dish import Dish
from django.db import models
from client.models import Customer

class Rating(models.Model):
    rating = models.FloatField(default=0.)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
