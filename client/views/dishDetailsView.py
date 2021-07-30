from django.views import View
from django.shortcuts import render, get_object_or_404
from client.models import Dish



class DishDetailsView(View):
    def get(self, request, id):
        dish = get_object_or_404(Dish, pk=id)
        return render(request, "client/dish-details.html", {"dish": dish})