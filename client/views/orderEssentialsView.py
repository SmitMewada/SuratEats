import json
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
        account_sid = "AC7c4f6e3456430c03cad171415cd5c9ff"
        token = "e00e17653bec025250b163839eda54ab"
        message = "Your order is successfully placed! your order for "

        auth_creds = get_auth_creds(request)
        phone = request.POST.get("phone")
        cart = request.session.get("cart")
        dishes = Dish.get_dishes_from_cart(request)
        return_object = { "createdOrders": []}


        try:

            if dishes:
                new_transaction = Transaction(
                        order_qty=len(cart.keys()),
                        customer=Customer.objects.get(pk=auth_creds.get("customer_id")),                       
                    )

                new_transaction.save()

                for dish in dishes:

                    new_address = AddressForm.addAddress(request.POST)            
                    new_address.save()

                    new_order = Order(
                        qty=float(cart.get(str(dish.id))),
                        dish=dish,
                        restaurant=Restaurant.objects.get(pk=dish.restaurant.id),
                        customer=Customer.objects.get(pk=auth_creds.get("customer_id")),
                        price=dish.price,
                        phone=phone,
                        transaction=new_transaction,
                        address=new_address
                    )
                    new_order.save()
                    message = message + new_order.dish.name

                    # Twilio
                    

                    return_object["createdOrders"].append({
                        "_id": new_order.id,
                        "qty": new_order.qty,
                        "restaurant": new_order.restaurant.name,
                        "order_date": new_order.order_date,
                        "price": new_order.price,
                        "address": {
                            "house_no": new_address.house_no,
                            "street": new_address.street,
                            "pincode": new_address.pincode
                        }
                    })
                    
                request.session.pop("cart")
                client = Client(account_sid, token)
                message = client.messages.create(
                        body="Your order has been placed. It will be at your doorstep in 30 minutes \n \n with regards\n SuratEats",
                        from_="+12342310267",
                        to=f"+91{phone}"
                    )
                return redirect('invoice', new_transaction.id)
            else:
                raise Exception("Error getting dishes!")
                    
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            })