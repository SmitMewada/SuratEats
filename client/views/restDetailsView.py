from django.views import View
from django.shortcuts import get_object_or_404, render, HttpResponse
from client.models import Restaurant, Dish, Category, dish
from django.core import serializers
from .customFuntions import get_item_count_from_cart, calc_grand_total, isInCart
from django.http import JsonResponse

class RestDetailsView(View):

    def get(self, request, id):

        category_id = request.GET.get("category_id")
        action = request.GET.get('action')

        cart = request.session.get('cart')
        dish_id = request.GET.get('dish_id')
        
        

        if action:

            if action == "check_cart":
                print('######', cart.get(dish_id))
                return JsonResponse({
                    "isInCart": isInCart(request.session.get('cart'), dish_id),
                    "qty": cart.get(dish_id)
                })
            
            if cart:
                qty = cart.get(dish_id)
                if "null" in cart:
                    cart.pop("null")
                if qty:
                    if action == "remove":
                        if qty < 1:
                            cart.pop(dish_id)
                        else:
                            cart[dish_id] = qty - 1
                    else:
                        cart[dish_id] = qty + 1
                else:
                    cart[dish_id] = 1
            else:
                cart = {}
                cart[dish_id] = 1
            request.session['cart'] = cart
           
            
            return JsonResponse({
                'qty': cart.get(dish_id),
                'item_count': get_item_count_from_cart(request),
                "grand_total":  f"₹{calc_grand_total(request.session.get('cart'))}"
            })
            

        if category_id:
            cat_dishes = Dish.objects.filter(category=Category.objects.get(pk=category_id))
            return HttpResponse(serializers.serialize('json', cat_dishes), content_type="text/json-comment-filtered")
        

        rest = get_object_or_404(Restaurant, pk=id)
        dishes = Dish.objects.filter(restaurant=Restaurant.objects.get(pk=id))
        categories = Category.objects.filter(restaurant=Restaurant.objects.get(pk=id))

        nearby_rests = Restaurant.objects.filter(blocked=False, active_status=True).exclude(id=id)[:4]


        return render(request, "client/rest-details.html", {"rest": rest, "dishes": dishes, "categories": categories, "nearby_rests": nearby_rests})