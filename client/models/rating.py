from django.db import models
from client.models import Customer, Restaurant

class Rating(models.Model):
    rating = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)