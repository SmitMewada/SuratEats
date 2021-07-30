from client.models.restaurant import Restaurant
from django.views import View
from django.shortcuts import render, redirect
from client.models import Category, category
from restaurant.forms  import CategoryForm
from client.views.customFuntions import get_auth_creds
from django.http import JsonResponse


class CatFormView(View):
    def get(self, request, id = 0):

        if id == 0:
            form = CategoryForm()
        else: 
            form = CategoryForm(instance=Category.objects.get(pk=id))
        return render(request, "restaurant/edit-cat.html" ,{
            "page_name": "Add category" if id == 0 else "Update category",
            "form": form
        })

    def post(slef, request, id):
        auth_creds = get_auth_creds(request)
        if id == 0:
            new_cat = Category(
                category=request.POST.get("category"),
                restaurant=Restaurant.objects.get(pk=auth_creds.get("restaurant_id"))
            )
            new_cat.save()
        else:
            updated_cat = CategoryForm(request.POST, instance=Category.objects.get(pk=id))
            if updated_cat.is_valid():
                updated_cat.save()
            
        return redirect("rest-categories")