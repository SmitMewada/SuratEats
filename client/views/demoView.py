import json
from django.views import View 
from django.http import JsonResponse
from client.models import Dish, Category
from django.core import serializers
from django.shortcuts import HttpResponse, render

class DemoView(View):
    def get(self, request):
        category_id = request.GET.get('category_id')
        cat_dishes = Dish.objects.filter(category=Category.objects.get(pk=category_id))
        return render(request, "client/dish_by_cat.html", {'dish': cat_dishes})
        
