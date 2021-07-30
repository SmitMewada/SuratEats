import json
from django.http.response import HttpResponseRedirect, JsonResponse
from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from client.forms import SignupForm
from django.core import serializers
from client.models import Customer

class SignupView(View):

    def get(self, request):
        form = SignupForm()
        email = request.GET.get("email")
        if email:
            email_count = Customer.objects.filter(email=email).count()
            return JsonResponse({
                "isEmailExists": email_count != 0
            })
        return render(request, "client/signup.html", {"form": form, "signup": True})

    def post(self, request):
       
        message = SignupForm.register_user(request.POST, 1)  
        return HttpResponseRedirect("login")
       
        

        
        