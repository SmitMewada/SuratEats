from django import template
from client.models import Customer
import math

register = template.Library()

@register.filter(name="subtotal")
def is_index_active(order):
    return order.price * order.qty


@register.filter(name="rest_dishes_active")
def rest_dishes_active(page_name):
    return page_name == "Dishes"

@register.filter(name="rest_orders_active")
def is_orders_active(page_name):
    return page_name == "All Orders"

@register.filter(name="rest_pending_orders_active")
def rest_pending_orders_active(page_name):
    return page_name == "Pending orders"

@register.filter(name="rest_cat_active")
def is_cat_active(page_name):
    return page_name == "Categories"





@register.filter(name="is_index_active")
def is_index_active(page_name):
    return page_name == "Dashboard"

@register.filter(name="is_blocked_active")
def is_blocked_active(page_name):
    return page_name == "Blocked restaurants"

@register.filter(name="is_rest_active")
def is_rest_active(page_name):
    return page_name == "Restaurants"

@register.filter(name="is_pending_req_active")
def is_pending_req_active(page_name):
    return page_name == "Pending requests"

@register.filter(name="is_cust_active")
def is_cust_active(page_name):
    return page_name == "Customers"

@register.filter(name="get_user_name")
def get_user_name(request):
    cust_id = request.session.get("customer_id")
    if cust_id:
        return Customer.objects.get(pk=cust_id)
    return "No name ;)"
    

@register.filter(name="calculate_total")
def calculate_total(order):
    return order.qty * order.price

@register.filter(name="currency")
def currency(value):
    return f"₹{value}"

