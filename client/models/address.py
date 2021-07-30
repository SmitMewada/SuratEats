from django.db import models

class Address(models.Model):
    house_no = models.CharField(max_length=50)
    street = models.CharField(max_length=150)
    pincode = models.BigIntegerField()
    area = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.house_no} {self.street}, {self.area}, {self.pincode}"
