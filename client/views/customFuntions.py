from client.models import Dish

def get_auth_creds(request):
    return {
        "customer_id": request.session.get("customer_id"),
        "restaurant_id": request.session.get("restaurant_id"),
        "cust_navbar": request.session.get("cust_navbar")
    }

def isInCart(cart, dish_id):
    cart_keys = [ cart_key for cart_key in cart.keys() if cart[cart_key] != 0]
    return True if str(dish_id ) in cart_keys else False


def calc_grand_total(cart):
    if cart:
        grand_total = 0
        dishes = Dish.objects.filter(id__in=cart.keys())
        for dish in dishes:
            grand_total += dish.price * cart.get(str(dish.id))
        if grand_total == 0:
            return grand_total
        return grand_total
    return 0

def remove_null(cart):
    if "null" in cart:
        cart.pop("null")

def get_item_count_from_cart(request):
    cart = request.session.get('cart')
    try:
        return len([cart_key for cart_key in list(cart.keys()) if cart_key != 'null' and cart[cart_key] >= 1])
    except:
        return 0