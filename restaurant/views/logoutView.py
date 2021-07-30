from django.views import View
from django.shortcuts import redirect, HttpResponseRedirect

class LogoutView(View):
    
    def get(self, request):
        request.session.pop("customer_id")
        request.session.pop("restaurant_id")
        return HttpResponseRedirect('login')