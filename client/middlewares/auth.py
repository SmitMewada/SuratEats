from client.models import Customer, Authorization
from django.http import response
from django.shortcuts import redirect
from client.views.customFuntions import get_auth_creds

def AuthMiddleware(get_response):
    # One time configuration and intialo=ization
    def middleware(request):
        return_url = request.META["PATH_INFO"]
        auth_details = get_auth_creds(request)
        auth = Authorization.objects.get(pk=1)

        try:
            customer = Customer.objects.get(pk=auth_details.get("customer_id"))
            if not auth_details.get("customer_id"):
                request.session["cust_navbar"] = False
                return redirect(f"/login?return_url={return_url}")

            if customer:
                if not auth.id == customer.auth.id :
                    request.session["cust_navbar"] = False
                    return redirect(f"/login?return_url={return_url}")
                
            response = get_response(request)
            request.session["cust_navbar"] = True
            return response
        except:
            return redirect("/login")


    return middleware



def ParameterizedMiddleware(get_response):
    def middleware(request, id):
        return_url = request.META["PATH_INFO"]
        auth_details = get_auth_creds(request)
        customer = Customer.objects.get(pk=auth_details.get("customer_id"))
        auth = Authorization.objects.get(pk=1)

        if not auth_details.get("customer_id"):
            request.session["cust_navbar"] = False
            return redirect(f"/login?return_url={return_url}")

        if customer:
            if not auth.id == customer.auth.id :
                request.session["cust_navbar"] = False
                return redirect(f"/login?return_url={return_url}")
                
        response = get_response(request, id)
        request.session["cust_navbar"] = True
        return response

    return middleware


def AdminAuthMiddleware(get_response):
    def middleware(request):
        return_url = request.META["PATH_INFO"]
        auth_details = get_auth_creds(request)
        customer = Customer.objects.get(pk=auth_details.get("customer_id"))
        auth = Authorization.objects.get(pk=3)

        if not auth_details.get("customer_id"):
            return redirect(f"/login?return_url={return_url}")

        if customer:
            if not auth.id == customer.auth.id :
                return redirect(f"/login?return_url={return_url}")

        response = get_response(request)
        return response
    return middleware

def ParaAdminAuthMiddleware(get_response):
    def middleware(request, id):
        return_url = request.META["PATH_INFO"]
        auth_details = get_auth_creds(request)
        customer = Customer.objects.get(pk=auth_details.get("customer_id"))
        auth = Authorization.objects.get(pk=3)

        if not auth_details.get("customer_id"):
            return redirect(f"/login?return_url={return_url}")

        if customer:
            if not auth.id == customer.auth.id :
                return redirect(f"/login?return_url={return_url}")

        response = get_response(request, id)
        return response
    return middleware


def RestAuthMiddleware(get_response):
    def middleware(request):
        return_url = request.META["PATH_INFO"]
        auth_details = get_auth_creds(request)
        customer = Customer.objects.get(pk=auth_details.get("customer_id"))
        auth = Authorization.objects.get(pk=2)

        if not auth_details.get("customer_id"):
            return redirect(f"/login?return_url={return_url}")

        if customer:
            if not auth.id == customer.auth.id :
                return redirect(f"/login?return_url={return_url}")

        response = get_response(request)
        return response
    return middleware


def ParaRestAuthMiddleware(get_response):
    def middleware(request, id):
        return_url = request.META["PATH_INFO"]
        auth_details = get_auth_creds(request)
        customer = Customer.objects.get(pk=auth_details.get("customer_id"))
        auth = Authorization.objects.get(pk=2)

        if not auth_details.get("customer_id"):
            return redirect(f"/login?return_url={return_url}")

        if customer:
            if not auth.id == customer.auth.id :
                return redirect(f"/login?return_url={return_url}")

        response = get_response(request, id)
        return response
    return middleware


def SimpleAuth(get_response):

    def middleware(request):
        auth_details = get_auth_creds(request)
        
        if not auth_details.get("customer_id"):
            return redirect('/login/')

        response = get_response(request)
        return response
        
    return middleware