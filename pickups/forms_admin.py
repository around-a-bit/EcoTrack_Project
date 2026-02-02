from django import forms
from django.contrib.auth.models import User
from .models import PickupRequest
from accounts.models import Profile

class AssignCollectorForm(forms.ModelForm):
    assigned_collector = forms.ModelChoiceField(
        queryset=User.objects.filter(profile__role="COLLECTOR"),
        required=True
    )

    class Meta:
        model = PickupRequest
        fields = ["assigned_collector"]
