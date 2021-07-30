from django.http.response import JsonResponse
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from client.models import Customer, Authorization

class CustomersView(View):
    def get(self, request):
        action = request.GET.get("action")
        if action:
            cust_id = request.GET.get("custID")
            
            customer = Customer.objects.get(pk=cust_id)
            if action == "block":
                customer.status = True
                customer.save(update_fields=["status"])
                return JsonResponse({
                    "success": "Blocked!"
                })
            if action == "unblock":
                customer.status = False
                customer.save(update_fields=["status"])
                return JsonResponse({
                    "success": "Unblocked!"
                })
        customers = Customer.objects.filter(status=False, auth=Authorization.objects.get(pk=1))
        return render(request, 'administrator/customers.html', {
                "customers": customers,
                "page_name": "Customers"
            })