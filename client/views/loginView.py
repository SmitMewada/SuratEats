from client.models import customer
from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from client.models import Customer, Restaurant

class LoginView(View):
    return_url = None

    def get(self, request):
        LoginView.return_url = request.GET.get("return_url")
        return render(request, "client/login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        url = ""
        

        try: 
            customer = Customer.objects.get(email=email)
            if check_password(password, customer.password):
                request.session["customer_id"] = customer.id

                if LoginView.return_url:
                   
                    url = LoginView.return_url
                  
                    return JsonResponse({
                        "success": "Redirection successful!",
                        "url": url
                    })
                else:   
                                
                    if customer.auth.id == 2:
                        url = "/restaurant-panel"
                        restaurant = Restaurant.objects.get(customer=customer)
                        request.session["restaurant_id"] = restaurant.id
                        request.session["cust_navbar"] = False
                    elif customer.auth.id == 3:
                        url = "/admin-panel"
                        request.session["admin_id"] = customer.id
                        request.session["cust_navbar"] = False
                    else:
                        url = "/restaurants"
                        request.session["cust_navbar"] = True
                

                return JsonResponse({
                    "success": "Login successful!",
                    "url": url
                })
            raise Exception("Invalid credentials!")
       
        
        except Exception as e:
            return JsonResponse({
                "error": "Invalid credentials!"
            })
       