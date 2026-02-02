from django.db import models
from django.contrib.auth.models import User

class PickupRequest(models.Model):

    WASTE_TYPE_CHOICES = [
        ("WET", "Wet Waste"),
        ("DRY", "Dry Waste"),
        ("EWASTE", "E-Waste"),
        ("MIXED", "Mixed Waste"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("ASSIGNED", "Assigned"),
        ("PICKED", "Picked"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pickup_requests")

    assigned_collector = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_pickups"
    )

    waste_type = models.CharField(max_length=10, choices=WASTE_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    pickup_address = models.CharField(max_length=255)

    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="PENDING")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    suggested_waste_type = models.CharField(max_length=10, blank=True, null=True)
    segregation_score = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.user.username} - {self.waste_type} - {self.status}"
