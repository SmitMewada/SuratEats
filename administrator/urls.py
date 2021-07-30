from administrator.views.restBlockView import RestBlockView
from administrator.views.PendingResquestsView import PendingRequestsView
from administrator.views.adminRestsView import AdminRestView
from administrator.views.customersView import CustomersView
from django.urls import path
from administrator.views import AdminHomeView
from client.middlewares import AdminAuthMiddleware, ParaAdminAuthMiddleware

urlpatterns = [
    path('', AdminAuthMiddleware(AdminHomeView.as_view()), name="admin-home"),
    path('customers/', AdminAuthMiddleware(CustomersView.as_view()), name="admin-custs"),
    path('restaurants/', AdminAuthMiddleware(AdminRestView.as_view()), name="admin-rests"),
    path('pending-request/', AdminAuthMiddleware(PendingRequestsView.as_view()), name="pending-requests"),
    path('restaurant-blocked/', AdminAuthMiddleware(RestBlockView.as_view()), name="rest-blocked")
]