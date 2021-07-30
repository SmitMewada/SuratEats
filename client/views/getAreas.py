from django.views import View
from django.http import HttpResponse
from django.core import serializers
from client.models import Area


class GetAreas(View):
    def get(self, request):
        message = request.GET.get('value')
        areas = serializers.serialize('json', Area.objects.filter(area__startswith=message), fields=['area', 'id'])
        return HttpResponse(areas, content_type='application/json')