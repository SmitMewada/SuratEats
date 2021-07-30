from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from client.models import Order, Customer, Address
from client.views.customFuntions import get_auth_creds


class OrdersView(View):
    def get(self, request):
        order_id = request.GET.get("orderID")
        if order_id:
            try:
                to_be_deleted_order = Order.objects.get(pk=order_id)
                address = Address.objects.get(pk=to_be_deleted_order.address.id)
                address.delete()
                to_be_deleted_order.delete()
                return JsonResponse({
                    "success": "Deleted successfuly!"
                })
            except:
                return JsonResponse({
                    "error": "Error occured!"
                })


        auth_creds = get_auth_creds(request)
        orders = Order.objects.filter(customer=Customer.objects.get(pk=auth_creds.get("customer_id")))
        return render(request, "client/orders.html", {
            "orders": orders
        })