from client.models.category import Category
from django.views import View
from django.shortcuts import render, redirect
from client.models import Dish
from restaurant.forms import DishForm
from client.views.customFuntions import get_auth_creds


class EditDishView(View):

    def get(self, request, id):
        form = DishForm(instance=Dish.objects.get(pk=id), load=True)
        return render(request, "restaurant/edit-dish.html", {"form": form})

    def post(self, request, id):
        dish = Dish.objects.get(pk=id)

        name = request.POST.get("name")
        price = request.POST.get("price")
        image = request.FILES.get("image")
        desc = request.POST.get("description")
        category = request.POST.get("category")

        dish.name = name
        dish.price = price
        dish.description = desc
        dish.category = Category.objects.get(pk=category)

        if image:
            dish.image = image

        dish.save()
        return redirect("rest-dishes")