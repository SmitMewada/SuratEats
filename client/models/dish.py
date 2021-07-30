from client.models import Restaurant, Category
from django.db import models

class Dish(models.Model):
    image = models.ImageField(upload_to="uploads/dishes")
    name = models.CharField(max_length=150)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name

    @staticmethod
    def get_dishes_from_cart(request):
        cart = request.session.get("cart")
        if cart:
            return Dish.objects.filter(id__in=cart.keys())
        return None