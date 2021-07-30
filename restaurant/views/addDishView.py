from client.models.dish import Dish
from django.http.response import JsonResponse
from django.views import View
from django.shortcuts import render, redirect
from restaurant.forms import DishForm
from client.views.customFuntions import get_auth_creds
from client.models import Category, Restaurant

class AddDishView(View):
    def get(self, request):
        auth_creds = get_auth_creds(request)
        form = DishForm(initial = { "restaurant" : auth_creds.get("restaurant_id")}, load=True)
      
        return render(request, "restaurant/add-dish.html", {"form": form})

    def post(self, request):
        new_dish = DishForm(request.POST, request.FILES)
        auth_creds = get_auth_creds(request)
        restaurant = Restaurant.objects.get(pk=auth_creds.get("restaurant_id"))
        print(request.GET.get("name"))
      
        try:
            new_dish = Dish(
                image=request.FILES.get("image"),
                price=request.POST.get("price"),
                description=request.POST.get("description"),
                category=Category.objects.get(pk=request.POST.get("category")),
                restaurant=restaurant,
                name=request.POST.get("name")
            )

            new_dish.save()

            return redirect("rest-dishes")
        except Exception as e:
            return JsonResponse({
             "error": str(e)
            })
            
        
        
        