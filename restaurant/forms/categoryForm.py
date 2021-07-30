from django import forms
from client.models import Category

class CategoryForm(forms.ModelForm):
    category = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "label": "Category",
        "placeholder": "Category",
        "class": "form-input"
    }))

    class Meta():
        model = Category
        fields = ["category"]