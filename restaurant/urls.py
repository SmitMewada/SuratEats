from restaurant.views.pendingOrdersView import PendingOrdersView
from restaurant.views.catFormView import CatFormView
from restaurant.views.categoryView import CategoryView
from restaurant.views.addDishView import AddDishView
from restaurant.views.editDishView import EditDishView
from restaurant.views.dishView import DishView
from client.views.logoutView import LogoutView
from restaurant.views.ordersView import OrdersView
from django.urls import path
from restaurant.views import IndexPanelView
from client.middlewares import RestAuthMiddleware, ParaRestAuthMiddleware

urlpatterns = [
    path('', RestAuthMiddleware(IndexPanelView.as_view()), name="rest-panel"),
    path('orders/', RestAuthMiddleware(OrdersView.as_view()), name="panel-orders"),
    path('logout', RestAuthMiddleware(LogoutView.as_view()), name="rest-logout"),
    path('dishes/', RestAuthMiddleware(DishView.as_view()), name="rest-dishes"),
    path('edit-dish/<int:id>', ParaRestAuthMiddleware(EditDishView.as_view()), name="edit-dish"),
    path('add-dish/', RestAuthMiddleware(AddDishView.as_view()), name="add-dish"),
    path('categories/', RestAuthMiddleware(CategoryView.as_view()), name="rest-categories"),
    path('category/<int:id>', ParaRestAuthMiddleware(CatFormView.as_view()), name="cat-form"),
    path("pending-orders/", RestAuthMiddleware(PendingOrdersView.as_view()), name="pending-orders")

]