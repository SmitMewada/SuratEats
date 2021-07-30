from django.db import models

class Area(models.Model):
    area = models.CharField(max_length=100)

    def __str__(self):
        return self.area