from django.http.response import JsonResponse
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from client.models import Restaurant, Customer

class PendingRequestsView(View):
    def get(self, request):

        action = request.GET.get("action")
        if action:
            print("#####", action)
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

            if action == "activate":
                restaurant.active_status = True
                restaurant.save(update_fields=["active_status"])
                return JsonResponse({
                    "success": "Activated!"
                })
            
            if action == "deactivate":
                restaurant.active_status = False
                restaurant.save(update_fields=["active_status"])
                return JsonResponse({
                    "success": "Deactivated!"
                })


        restaurants = Restaurant.objects.filter(active_status=False, blocked=False)
        return render(request, 'administrator/pending-requests.html', {
            "restaurants": restaurants, "page_name": "Pending requests"
            })