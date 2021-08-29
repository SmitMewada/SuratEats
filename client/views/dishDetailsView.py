from django.views import View
from django.shortcuts import render, get_object_or_404
from client.models import Dish, Restaurant



class DishDetailsView(View):
    def get(self, request, id):
        dish = get_object_or_404(Dish, pk=id)
        dishes =  Dish.objects.filter(restaurant=dish.restaurant.id).exclude(id=id)
        
        return render(request, "client/dish-details.html", {
            "dish": dish,
            "other_dishes": dishes
        })