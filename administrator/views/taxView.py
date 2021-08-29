from django.http.response import JsonResponse
from django.views import View
from django.shortcuts import redirect, render
from client.views.customFuntions import get_auth_creds
from client.models import customer, Tax, tax


class TaxView(View):
    def get(self, request):
        tax_rate_count = Tax.objects.count()
        tax_message = ""
        update_tax = request.GET.get("update_tax")
        
        if tax_rate_count == 0:
            tax_message = "No tax is set"
        else:
            tax_message = str(Tax.objects.get(pk=1).tax_rate)

        if update_tax:
            tax_rate_to_update = request.GET.get("tax_rate")
            auth_creds = get_auth_creds(request)

            try:
                tax_count = Tax.objects.count()
                if tax_count == 0:
                    tax_rate = Tax(tax_rate=tax_rate_to_update, customer=customer.Customer.objects.get(pk=auth_creds.get("customer_id")))
                    tax_rate.save()
                else:
                    tax_rate = Tax.objects.get(pk=1)
                    tax_rate.tax_rate = int(tax_rate_to_update)
                    tax_rate.save()
                
                return JsonResponse({
                    "success": "Tax rate updated successfully!"
                })
            except Exception as e:
                return JsonResponse({
                    "error": str(e)
                })

        return render(request, "administrator/tax.html", {
            "page_name": "Manage Tax Rate",
            "tax_message": tax_message if tax_rate_count == 0 else tax_message + "%"
        })

    
        