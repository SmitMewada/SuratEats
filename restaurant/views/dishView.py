from django.views import View
from django.shortcuts import redirect, render
from client.models import Dish, Restaurant
from client.views.customFuntions import get_auth_creds
from django.http import JsonResponse

class DishView(View):
    def get(self, request):
        auth_creds = get_auth_creds(request)
        dish_id = request.GET.get("dishID")
      
        if dish_id:
            del_dish = Dish.objects.get(pk=dish_id)
            del_dish.delete()
            return JsonResponse({
                "url": "/restaurant-panel/dishes"
            })

        dishes = Dish.objects.filter(restaurant=Restaurant.objects.get(pk=auth_creds.get("restaurant_id")))
        return render(request, "restaurant/dishes.html", {
            "dishes": dishes,
            "page_name": "Dishes"
        })