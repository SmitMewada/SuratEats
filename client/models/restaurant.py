from django.db import models
from client.models import Customer, Area, Address


class Restaurant(models.Model):
    image = models.ImageField(upload_to="uploads/restaurants")
    name = models.CharField(max_length=150)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    online_status = models.BooleanField(default=True)
    active_status = models.BooleanField(default=False)
    from_hrs = models.IntegerField(default=6)
    to_hrs = models.IntegerField(default=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, default=None)
    blocked = models.BooleanField(default=False)


    def __str__(self):
        return self.name