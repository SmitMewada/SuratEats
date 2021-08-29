import json
from django.views import View 
from django.http import JsonResponse
from client.models import Dish, Category
from django.core import serializers
from django.shortcuts import HttpResponse, render

class DemoView(View):
    def get(self, request):
    
        return render(request, "client/demo.html")
        
