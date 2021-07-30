from django import forms
from client.models import Restaurant


class RestaurantForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "placeholder": "Name",
        "label": "Name",
        "class": "form-input"
    }))
    image = forms.ImageField()

    class Meta():
        model = Restaurant
        fields = ["name", "image", "area"]