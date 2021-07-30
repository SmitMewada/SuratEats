from django.views import View
from django.shortcuts import render
from client.models import Category, Restaurant
from client.views.customFuntions import get_auth_creds
from django.http import JsonResponse

class CategoryView(View):
    def get(self, request):
        cat_id = request.GET.get("catID")
      
        if cat_id:
            try:
                to_be_deleted = Category.objects.get(pk=cat_id)
                to_be_deleted.delete()
                return JsonResponse({
                    "success": "Successful!"
                })
            except Exception as e:
                return JsonResponse({
                    "error": str(e)
                })

        auth_creds = get_auth_creds(request)
        categories = Category.objects.filter(restaurant=Restaurant.objects.get(pk=auth_creds.get("restaurant_id")))
        return render(request, "restaurant/categories.html", {"categories": categories, "page_name": "Categories"})