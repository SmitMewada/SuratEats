from django.views import View
from django.shortcuts import render
from client.models import Dish
from django.http import JsonResponse
from .customFuntions import get_item_count_from_cart


class CartView(View):

    def get(self, request):
        cart = request.session.get('cart')
        action = request.GET.get('action')

        if cart:
            if action:
               dish_id = request.GET.get('dish_id')

            if action == "pop":
                cart.pop(dish_id)
                request.session['cart'] = cart
                return JsonResponse({'success': "Deletion successful!", "count": get_item_count_from_cart(request)})

            if "null" in cart:
                cart.pop("null")
            cart_keys = [ cart_key for cart_key in cart.keys() if cart[cart_key] >= 1]
            dishes = Dish.objects.filter(id__in=cart_keys)

            return render(request, "client/cart.html", {
                "dishes": dishes,
                "item-count": get_item_count_from_cart(request)
            })
        else:
            return render(request, "client/cart.html", {
                "isCartEmpty": True
            })