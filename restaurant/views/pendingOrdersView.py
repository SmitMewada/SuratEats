from django.views import View
from django.shortcuts import render
from client.models import Order, Restaurant
from client.views.customFuntions import get_auth_creds
from django.http import JsonResponse


class PendingOrdersView(View):
    def get(self, request):
        action = request.GET.get("action")
        if action:
            order_id = request.GET.get("orderID")
            order = Order.objects.get(pk=order_id)
            if action == "check":
                order.status = True
                order.save(update_fields=["status"])
                return JsonResponse({
                    "success": "Checked"
                })
            else:
                order.status = False
                order.save(update_fields=["status"])
                return JsonResponse({
                    "success": "Unchecked"
                })
                

        auth_creds = get_auth_creds(request)
        orders = Order.objects.filter(restaurant=Restaurant.objects.get(pk=auth_creds.get("restaurant_id")), status=False)
        return render(request, "restaurant/pending-orders.html",{
            "page_name": "Pending orders",
            "orders": orders
        })