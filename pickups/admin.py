from django.contrib import admin
from .models import PickupRequest

@admin.register(PickupRequest)
class PickupRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "waste_type", "status", "created_at")
    list_filter = ("waste_type", "status", "created_at")
    search_fields = ("user__username", "pickup_address")
