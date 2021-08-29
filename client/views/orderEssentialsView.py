import json
from logging import error
from client.models import transaction
from client.models.transaction import Transaction
from client.models import Order, Dish, Restaurant, Customer, address, order
from django.views import View
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from client.forms import AddressForm
from client.views.customFuntions import get_auth_creds
from django.core import serializers
from twilio.rest import Client

class OrderEssentialsView(View):
    def get(self, request):
        form = AddressForm()
        return render(request, "client/orderEssentials.html", {"form": form})

    def post(self, request):
        
        house_no = request.POST.get("house_no")
        street = request.POST.get("street")
        area = request.POST.get("area")
        pincode = request.POST.get("pincode")
        phone = request.POST.get("phone")


        request.session["order_details"] = {
            "house_no": house_no,
            "street": street,
            "area": area,
            "pincode": pincode,
            "phone": phone
        }

        return redirect("payment")