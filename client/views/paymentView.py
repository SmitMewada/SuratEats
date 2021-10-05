import json
from client.models import transaction
from client.models.transaction import Transaction
from client.models import Order, Dish, Restaurant, Customer, Address
from django.views import View
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from client.forms import AddressForm
from client.views.customFuntions import get_auth_creds
from django.core import serializers
from twilio.rest import Client
from client.views.customFuntions import calc_grand_total
class PaymentsView(View):

    def get(self, request):
        return render(request, "client/payment.html", {
            "total_price": calc_grand_total(request.session.get("cart"))
        })

    def post(self, request):
        body = json.loads(request.body)
        success = body.get("success")

        if success:
            account_sid = ""
            token = ""
            message = "Your order is successfully placed! your order for "

            auth_creds = get_auth_creds(request)
            order_details = request.session.get("order_details")
            cart = request.session.get("cart")
            dishes = Dish.get_dishes_from_cart(request)
            return_object = { "createdOrders": []}
            phone = order_details.get("phone")

            try:

                if dishes:
                    new_transaction = Transaction(
                            order_qty=len(cart.keys()),
                            customer=Customer.objects.get(pk=auth_creds.get("customer_id")),                       
                        )

                    new_transaction.save()

                    for dish in dishes:

                        new_address = Address(house_no=order_details.get("house_no"), street=order_details.get("street"), pincode=order_details.get("pincode"), area=order_details.get("area"))       
                        new_address.save()

                        new_order = Order(
                            qty=float(cart.get(str(dish.id))),
                            dish=dish,
                            restaurant=Restaurant.objects.get(pk=dish.restaurant.id),
                            customer=Customer.objects.get(pk=auth_creds.get("customer_id")),
                            price=dish.price,
                            phone=order_details.get("phone"),
                            transaction=new_transaction,
                            address=new_address
                        )
                        new_order.save()
                        message = message + new_order.dish.name

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
                            from_="+12055308750",
                            to=f"+91{phone}"
                        )
                    return JsonResponse({
                        "transactionID": new_transaction.id
                    })
                else:
                    raise Exception("Error getting dishes!")
                        
            except Exception as e:
                return JsonResponse({
                    "error": str(e),
                    "transactionID": new_transaction.id
                })

        
        else:
            return JsonResponse({
                "error": "Transaction was not completed!"
            })
        
