from client.models.restaurant import Restaurant
from django import forms
from client.models import Dish, Category


class DishForm(forms.ModelForm):
    image = forms.ImageField()
    price = forms.FloatField(widget=forms.TextInput(attrs={
        "placeholder": "Price",
        "label": "Price",
        "class": "form-input"
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Description",
        "label": "Description",
         "class": "form-input"
    }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Name",
        "label": "Name",
        "class": "form-input"
    }))
    

    class Meta():
        model = Dish
        fields = ["name", "price", "image", "description", "category"]

    def __init__(self, load, *args, **kwrgs):
        initial = kwrgs.pop("initial", None)
        if initial:
            restaurant = initial.pop("restaurant", None)
            if restaurant:
                super(DishForm, self).__init__(*args, **kwrgs)
                self.fields['category'].queryset = Category.objects.filter(restaurant=Restaurant.objects.get(pk=restaurant))

        else:
            super(DishForm, self).__init__(*args, **kwrgs)

