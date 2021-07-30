from django import template
import math
from client.views.customFuntions import calc_grand_total
from client.models import Restaurant, Order, Dish

register = template.Library()

@register.filter(name="get_grandtotal_from_order")
def get_grandtotal_from_order(orders):
    try:
        grand_total = 0
        for order in orders:
            grand_total += order.dish.price * order.qty
        return grand_total
    except:
        return 0

@register.filter(name="subtotal_for_orders_rest_wise")
def subtotal_for_orders_rest_wise(dish, orders):
    try:
        qty = get_qty_from_order(dish, orders)
        return dish.price * int(qty)
    except:
        return 0

@register.filter(name="get_qty_from_order")
def get_qty_from_order(dish, orders):
    try:
        for order in orders:
            transaction_id = order.transaction.id
        order = Order.objects.get(dish=dish.id, transaction=transaction_id)
        return order.qty
    except:
        return 0

@register.filter(name="get_dishes_from_restaurant")
def get_dishes_from_restaurant(orders, restaurant):
    try:
        dish_ids = [order.dish.id for order in orders]
        dishes = Dish.objects.filter(id__in=dish_ids, restaurant=restaurant)
        return dishes
    except:
        return None

@register.filter(name="get_restaurant_query_set")
def get_restaurant_query_set(orders):
    try:
        rest_ids = [order.restaurant.id for order in orders]
        restuarants = Restaurant.objects.filter(id__in=rest_ids)
        return restuarants
    except:
        return None

@register.filter(name="has_area")
def sub_total(request):
    return request.GET.get("area-id")

@register.filter(name="sub_total")
def sub_total(order):
    return order.price * order.qty

@register.filter(name="is_loggedin")
def is_loggedin(request):
    return request.session.get("customer_id") and request.session.get("cust_navbar")

@register.filter(name="calculate_grandtotal")
def calculate_grandtotal(cart):
    return calc_grand_total(cart)

@register.filter(name="currency")
def currency(value):
    return f"₹{value}"

@register.filter(name="calculate_subtotal")
def calculate_subtotal(dish, cart):
    if str(dish.id) in list(cart.keys()):
        return dish.price * cart.get(str(dish.id))

@register.filter(name="set_cart_indicator")
def set_cart_indicator(cart):
    try:
        return len([cart_key for cart_key in list(cart.keys()) if cart_key != 'null' and cart[cart_key] >= 1])
    except:
        return 0

@register.filter(name="get_qty_from_cart")
def get_qty_from_cart(dish, cart):
    return cart.get(str(dish.id))

@register.filter(name='is_in_cart')
def is_in_cart(dish, cart):
    if cart.get(str(dish.id)):
        return True
    return False