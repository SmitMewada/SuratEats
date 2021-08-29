from client.views.dishRatingView import DishRating
from client.views.paymentView import PaymentsView
from client.views.dishDetailsView import DishDetailsView
from client.views.invoiceGenerator import render_invoice
from client.views.getAreas import GetAreas
from client.views.ordersView import OrdersView
from client.views.restSignupView import RestSignupView
from client.views.logoutView import LogoutView
from client.views.orderEssentialsView import OrderEssentialsView
from client.views.signupView import SignupView
from client.views.cartView import CartView
from client.views.demoView import DemoView
from client.views.loginView import LoginView
from client.views.restDetailsView import RestDetailsView
from client.views.restsView import RestsView
from django.urls import path
from client.views import IndexView
from client.middlewares import AuthMiddleware, SimpleAuth, ParameterizedMiddleware

urlpatterns = [
    path('', IndexView.as_view(), name="index-page"),
    path('restaurants/', AuthMiddleware(RestsView.as_view()), name="restaurants"),
    path('restaurant/<int:id>', ParameterizedMiddleware(RestDetailsView.as_view()), name="rest-details"),
    path('login/', LoginView.as_view(), name="login"),
    path('cart/', AuthMiddleware(CartView.as_view()), name="cart"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('order-procedure', SimpleAuth(OrderEssentialsView.as_view()), name="order-essen"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('demo/', DemoView.as_view()),
    path("restaurant-signup/", RestSignupView.as_view(), name="rest-signup"),
    path('orders/', AuthMiddleware(OrdersView.as_view()), name="client-orders"),
    path('get-areas/', GetAreas.as_view(), name="get-areas"),
    path('invoice/<int:id>', render_invoice, name="invoice"),
    path('dish/<int:id>', ParameterizedMiddleware(DishDetailsView.as_view()), name="dish-details"),
    path('payment/', PaymentsView.as_view(), name="payment"),
    path('dish-rating/<int:id>', DishRating.as_view(),name="dish-rating")
]