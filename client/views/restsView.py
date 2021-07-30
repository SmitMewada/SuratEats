from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from client.models import Restaurant, Area

class RestsView(View):

    def get(self, request):
        area_id = request.GET.get("area-id")
        if area_id:
            area = get_object_or_404(Area, pk=area_id)
            rests = Restaurant.objects.filter(area=area)
            return render(request, "client/rests.html", {"rests": rests, "area": area})
            
        rests = Restaurant.objects.filter(blocked=False, active_status=True)
        return render(request, "client/rests.html", {"rests": rests})