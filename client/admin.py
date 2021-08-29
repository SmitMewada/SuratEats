from client.models.rating import Rating
from client.models.order import Order
from client.models.dish import Dish
from client.models.transaction import Transaction
from client.models.area import Area
from client.models.restaurant import Restaurant
from client.models.authorization import Authorization
from django.contrib import admin
from client.models import Customer, Address, Category

admin.site.register(Customer)
admin.site.register(Authorization)
admin.site.register(Restaurant)
admin.site.register(Area)
admin.site.register(Transaction)
admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Rating)

