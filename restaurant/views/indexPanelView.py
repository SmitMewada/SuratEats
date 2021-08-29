from client.models.tax import Tax
import json
from django.views import View
from django.shortcuts import render
from client.views.customFuntions import get_auth_creds
from client.models import Restaurant, Order
from django.http import JsonResponse
from django.core import serializers

class IndexPanelView(View):

    def get(self, request):
        auth_creds = get_auth_creds(request)
        restaurant = Restaurant.objects.get(pk=auth_creds.get("restaurant_id"))
        tax_rate = Tax.objects.get(pk=1)
        
        income_dataset = []
        order_dataset = []
        date_list = []
        
        order_dates = Order.objects.filter(restaurant=restaurant, status=True).order_by().values("order_date").distinct()
        for order in order_dates:
            date_list.append(order.get("order_date"))

        for date in date_list:
            income = 0
            orders_by_date = Order.objects.filter(order_date=date, restaurant=restaurant)
            orders_count_date = orders_by_date.count()

            for order in orders_by_date:
                commission_rate = (order.price * 15) / 100
                income = income + (order.price - commission_rate) * order.qty

            order_dataset.append({
                "order_date": str(order.order_date),
                "orders": orders_count_date
            })
            income_dataset.append({
                    "order_date": str(order.order_date),
                    "income":income
            })

         

        order_count = Order.objects.filter(restaurant=restaurant).count()

        pending_orders = Order.objects.filter(restaurant=restaurant, status=False).count()

        total_income = 0
        orders = Order.objects.filter(restaurant=restaurant, status=True)
        for order in orders:
            commission_rate = (order.price * 15) / 100
            total_income = total_income + (order.price - commission_rate) * order.qty

        return render(request, 'restaurant/index-page.html', {
            "order_count" : order_count,
            "pending_orders": pending_orders,
            "income": total_income,
            "income_dataset": income_dataset,
            "order_dataset": order_dataset,
            "page_name": "Dashboard",
            "tax_rate": tax_rate

        })