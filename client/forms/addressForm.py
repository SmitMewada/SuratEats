from django import forms
from client.models import Address

class AddressForm(forms.ModelForm):
    house_no = forms.CharField(max_length=14, widget=forms.TextInput(attrs={
        "placeholder": "House no",
        "class": "form-input",
        "label": "House no"
    }))
    street = forms.CharField(max_length=14, widget=forms.TextInput(attrs={
        "placeholder": "Street",
        "class": "form-input",
        "label": "Street"
    }))
    area = forms.CharField(max_length=14, widget=forms.TextInput(attrs={
        "placeholder": "Area",
        "class": "form-input",
        "label": "Area"
    }))
    pincode = forms.IntegerField(widget=forms.TextInput(attrs={
        "placeholder": "Pincode",
        "class": "form-input",
        "label": "Pincode"
    }))

    class Meta():
        model = Address
        fields = ["house_no", "street", "area", "pincode"]

    @staticmethod
    def addAddress(post_data):
        try:
            new_address = AddressForm(post_data)
            if new_address.is_valid():
               new_address = new_address.save(commit=False)
               return new_address
        except Exception as e:
            return None
            