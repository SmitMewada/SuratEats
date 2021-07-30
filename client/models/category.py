from django.db import models
from client.models import Restaurant

class Category(models.Model):
    category = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.category