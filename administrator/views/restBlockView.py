from django.http.response import JsonResponse
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from client.models import Restaurant, Customer

class RestBlockView(View):
    def get(self, request):
        action = request.GET.get("action")
        if action:
            rest_id = request.GET.get("restID")
            
            restaurant = Restaurant.objects.get(pk=rest_id)
            if action == "block":
                restaurant.blocked = True
                restaurant.save(update_fields=["blocked"])
                return JsonResponse({
                    "success": "Blocked!"
                })
            if action == "unblock":
                restaurant.blocked = False
                restaurant.save(update_fields=["blocked"])
                return JsonResponse({
                    "success": "Unblocked!"
                })

        restaurants = Restaurant.objects.filter(blocked=True)
        return render(request, 'administrator/rest-block.html', {
            "restaurants": restaurants, "page_name": "Blocked restaurants"
        })