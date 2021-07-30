from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from client.models import Order, Transaction



def render_invoice(request, *args, **kwrgs):
   id = kwrgs.get('id')
   cust_id = request.session.get('customer_id')   
   orders = Order.objects.filter(transaction=id)
   template_path = 'client/invoice.html'
   transaction = Transaction.objects.get(pk=id)
   context = {'orders': orders, 'transaction': transaction}
  
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'filename="invoice.pdf"'

   template = get_template(template_path)
   html = template.render(context)

   pisa_status = pisa.CreatePDF(
      html, dest=response)

   if pisa_status.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')
   return response