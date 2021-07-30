from django.db.models.fields import AutoField
from django.http.response import HttpResponseRedirect
from client.models import address
from client.models.restaurant import Restaurant
from client.models.address import Address
from client.models import Customer, Area, Authorization, customer
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from client.forms import RestaurantForm, AddressForm, SignupForm
from django.contrib.auth.hashers import make_password



class RestSignupView(View):
    def get(self, request):

        email = request.GET.get("email")
        if email:
            email_count = Customer.objects.filter(email=email).count()
            return JsonResponse({
                "isEmailExists": email_count != 0
            })

        rest_form = RestaurantForm()
        address_form = AddressForm()
        signup_form = SignupForm()

        return render(request, "client/restSignupForm.html",{
            "rest_form": rest_form,
            "address_form": address_form,
            "signup_form": signup_form
        })

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        
        house_no = request.POST.get("house_no")
        street = request.POST.get("street")
        area = Area.objects.get(pk=request.POST.get("area"))
        pincode = request.POST.get("pincode")

        name = request.POST.get("name")
        image = request.FILES.get("image")

        # Creating a customer object
        new_customer = Customer(
            first_name=first_name, 
            last_name=last_name,
            email=email,
            password=make_password(password),
            phone=phone,
            auth=Authorization.objects.get(pk=2)
        )
        new_customer.save()

        # Creating an address object
        new_address = Address(
            house_no=house_no,
            street=street,
            area=area.area,
            pincode=pincode
        )
        new_address.save()

        # Creating a restaurant object finally
        new_restaurant = Restaurant(
            name=name,
            image=image,
            customer=new_customer,
            address=new_address,
            area=area
        )
        new_restaurant.save()
        

        return HttpResponseRedirect("login")