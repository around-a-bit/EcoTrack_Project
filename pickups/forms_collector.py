from django import forms
from .models import PickupRequest

class UpdatePickupStatusForm(forms.ModelForm):
    class Meta:
        model = PickupRequest
        fields = ["status"]
