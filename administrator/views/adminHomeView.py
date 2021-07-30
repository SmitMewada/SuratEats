from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from client.models import Customer, Restaurant, Order, Authorization


class AdminHomeView(View):
    def get(self, request):

        total_customers = Customer.objects.filter(auth=Authorization.objects.get(pk=1)).count()
        total_restaurants = Customer.objects.filter(auth=Authorization.objects.get(pk=2)).count()
        pending_requests = Restaurant.objects.filter(active_status=False).count()

        orders = Order.objects.all()
        total_income = 0
        for order in orders:
            total_income = total_income + ((order.price * 15) / 100) * order.qty

        
        income_dataset = []
        rest_dataset = []
        date_list = []
        
        order_dates = Order.objects.order_by().values("order_date").distinct()
        for order in order_dates:
            date_list.append(order.get("order_date"))

        for date in date_list:
            income = 0
            orders_by_date = Order.objects.filter(order_date=date)
            orders_count_date = orders_by_date.count()

            for order in orders_by_date:
                income = income + ((order.price * 15) / 100) * order.qty

            # rest_dataset.append({
            #     "order_date": str(order.order_date),
            #     "orders": orders_count_date
            # })
            income_dataset.append({
                    "order_date": str(order.order_date),
                    "income": income
            })
        
        return render(request, "administrator/admin-home.html", {
            "page_name": "Dashboard",
            "total_customers": total_customers,
            "total_restaurants": total_restaurants,
            "pending_requests": pending_requests,
            "total_income": total_income,
            "income_dataset": income_dataset
        })