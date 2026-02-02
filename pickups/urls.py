from django.urls import path
from . import views

app_name = "pickups"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_pickup, name="create_pickup"),
    path("my-requests/", views.my_requests, name="my_requests"),

    path("collector/", views.collector_dashboard, name="collector_dashboard"),
    path("collector/update/<int:pickup_id>/", views.update_pickup_status, name="update_pickup_status"),

    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("admin-dashboard/assign/<int:pickup_id>/", views.assign_collector, name="assign_collector"),
]
