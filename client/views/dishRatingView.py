from django.views import View
from django.shortcuts import render, get_object_or_404
from client.models import Dish, Rating, Customer
from client.views.customFuntions import get_auth_creds
from django.http import JsonResponse

class DishRating(View):
    def get(self, request, id):
        no_of_stars = request.GET.get("no_of_stars")
        auth_creds = get_auth_creds(request)
        customer = auth_creds.get("customer_id")
        dish_id = request.GET.get("dish_id")

        if no_of_stars:
            try:
                rating_count = Rating.objects.filter(customer=customer, dish=Dish.objects.get(pk=dish_id)).count()
            
                if rating_count == 0:
                    new_rating = Rating(rating=no_of_stars, customer=Customer.objects.get(pk=customer), dish=Dish.objects.get(pk=dish_id))
                    new_rating.save()
                    return JsonResponse({
                        "success": "Ratings created successfully!"
                    })
                else: 
                    updated_rating = Rating.objects.get(customer=customer, dish=Dish.objects.get(pk=dish_id))
                    updated_rating.rating = no_of_stars
                    updated_rating.save()
                    return JsonResponse({
                        "success": "Ratings updated successfully!"
                    })
            except Exception as e:
                return JsonResponse({
                    "error": str(e)
                })

        dish = get_object_or_404(Dish, pk=id)
        try:
            rating = Rating.objects.get(dish=Dish.objects.get(pk=id), customer=customer)

            return render(request, "client/dish-rating.html", {
                "dish": dish,
                "rating": int(rating.rating),
                "isRated": True
            })
        except Exception as e:
            return render(request, "client/dish-rating.html", {
                "dish": dish,
                "rating": -1,
                "isRated": False
            })