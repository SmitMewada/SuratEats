from client.models.authorization import Authorization
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    password = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    auth = models.ForeignKey(Authorization, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"