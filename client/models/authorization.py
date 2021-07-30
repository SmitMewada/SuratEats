from django.db import models

class Authorization(models.Model):
    authorization = models.CharField(max_length=50)

    def __str__(self):
        return self.authorization