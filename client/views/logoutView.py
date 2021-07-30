from django.views import View
from django.shortcuts import redirect

class LogoutView(View):
    def get(self, request):
        request.session.pop("customer_id")
        return redirect("login")