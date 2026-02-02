from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.decorators import role_required
from .models import PickupRequest
from .forms import PickupRequestForm
from .forms_admin import AssignCollectorForm
from .forms_collector import UpdatePickupStatusForm
from .ai_utils import suggest_waste_type, calculate_segregation_score
from .ai_utils import get_tips
from django.db.models import Count
from django.db import models


def home(request):
    return render(request, "pickups/home.html")


@login_required
def create_pickup(request):
    if request.method == "POST":
        form = PickupRequestForm(request.POST)
        if form.is_valid():
            pickup = form.save(commit=False)
            pickup.user = request.user
            pickup.status = "PENDING"

            # AI suggestion + scoring
            pickup.suggested_waste_type = suggest_waste_type(pickup.description)
            pickup.segregation_score = calculate_segregation_score(
                pickup.waste_type,
                pickup.suggested_waste_type
            )

            pickup.save()
            return redirect("pickups:my_requests")
    else:
        form = PickupRequestForm()

    # return render(request, "pickups/create_pickup.html", {"form": form})
    tip = None
    if request.method == "POST" and form.is_valid():
        tip = get_tips(pickup.suggested_waste_type)

    return render(request, "pickups/create_pickup.html", {"form": form, "tip": tip})


# @login_required
# def my_requests(request):
#     requests = PickupRequest.objects.filter(user=request.user).order_by("-created_at")
#     return render(request, "pickups/my_requests.html", {"requests": requests})


@login_required
def my_requests(request):
    requests = PickupRequest.objects.filter(user=request.user).order_by("-created_at")

    for r in requests:
        r.tip = get_tips(r.suggested_waste_type)

    return render(request, "pickups/my_requests.html", {"requests": requests})


# ✅ ADMIN FLOW
# @login_required
# @role_required(["ADMIN"])
# def admin_dashboard(request):
#     pickups = PickupRequest.objects.all().order_by("-created_at")
#     return render(request, "pickups/admin_dashboard.html", {"pickups": pickups})

@login_required
@role_required(["ADMIN"])
def admin_dashboard(request):
    pickups = PickupRequest.objects.all().order_by("-created_at")

    stats = PickupRequest.objects.aggregate(
        total=Count("id"),
        pending=Count("id", filter=models.Q(status="PENDING")),
        assigned=Count("id", filter=models.Q(status="ASSIGNED")),
        picked=Count("id", filter=models.Q(status="PICKED")),
        completed=Count("id", filter=models.Q(status="COMPLETED")),
        cancelled=Count("id", filter=models.Q(status="CANCELLED")),
    )

    waste_stats = PickupRequest.objects.values("waste_type").annotate(count=Count("id"))

    return render(request, "pickups/admin_dashboard.html", {
        "pickups": pickups,
        "stats": stats,
        "waste_stats": waste_stats,
    })


@login_required
@role_required(["ADMIN"])
def assign_collector(request, pickup_id):
    pickup = get_object_or_404(PickupRequest, id=pickup_id)

    if request.method == "POST":
        form = AssignCollectorForm(request.POST, instance=pickup)
        if form.is_valid():
            pickup = form.save(commit=False)
            pickup.status = "ASSIGNED"
            pickup.save()
            messages.success(request, "Collector assigned successfully.")
            return redirect("pickups:admin_dashboard")
    else:
        form = AssignCollectorForm(instance=pickup)

    return render(request, "pickups/assign_collector.html", {"form": form, "pickup": pickup})


# ✅ COLLECTOR FLOW
@login_required
@role_required(["COLLECTOR"])
def collector_dashboard(request):
    pickups = PickupRequest.objects.filter(assigned_collector=request.user).order_by("-created_at")
    return render(request, "pickups/collector_dashboard.html", {"pickups": pickups})


@login_required
@role_required(["COLLECTOR"])
def update_pickup_status(request, pickup_id):
    pickup = get_object_or_404(PickupRequest, id=pickup_id, assigned_collector=request.user)

    if request.method == "POST":
        form = UpdatePickupStatusForm(request.POST, instance=pickup)
        if form.is_valid():
            pickup = form.save(commit=False)

            # safety logic: collector can't set back to PENDING
            if pickup.status == "PENDING":
                pickup.status = "ASSIGNED"

            pickup.save()
            messages.success(request, "Pickup status updated.")
            return redirect("pickups:collector_dashboard")
    else:
        form = UpdatePickupStatusForm(instance=pickup)

    return render(request, "pickups/update_status.html", {"form": form, "pickup": pickup})
