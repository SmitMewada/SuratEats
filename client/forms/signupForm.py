from client.models.authorization import Authorization
from django import forms
from client.models import Customer
from django.contrib.auth.hashers import make_password

class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "placeholder": "First name",
        "label": "First name",
        "class": "form-input"
    }))

    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "placeholder": "Last name",
        "label": "Last name",
        "class": "form-input"
    }))

    password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "placeholder": "Password",
        "label": "Password",
        "class": "form-input"
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "Email",
        "label": "E-mail",
        "class": "form-input"
    }))

    phone = forms.IntegerField(widget=forms.TextInput(attrs={
        "placeholder": "Phone",
        "label": "Phone",
        "class": "form-input"
    }))

    class Meta():
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']

    @staticmethod
    def create_user(post_data, auth_id):
        new_customer = SignupForm(post_data)
        if new_customer.is_valid():
            new_customer = new_customer.save(commit=False)
            new_customer.authorization = Authorization.objects.get(pk=auth_id)
            new_customer.password = make_password(new_customer.password)
            new_customer.save()
            return new_customer
        else:
            return None

    @staticmethod
    def register_user(post_data, auth_id):
        new_customer = SignupForm(post_data)
        if new_customer.is_valid():
            new_customer = new_customer.save(commit=False)
            new_customer.authorization = Authorization.objects.get(pk=auth_id)
            new_customer.password = make_password(new_customer.password)
            new_customer.save()
            return { "success": "Registered successfully!" }
        else:
            return {
                "error": new_customer.errors
            }