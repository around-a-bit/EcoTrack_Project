from django import forms
from .models import PickupRequest

class PickupRequestForm(forms.ModelForm):
    class Meta:
        model = PickupRequest
        fields = ["waste_type", "description", "pickup_address"]
        widgets = {
            "waste_type": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "pickup_address": forms.TextInput(attrs={"class": "form-control"}),
        }
