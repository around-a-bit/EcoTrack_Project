from django.urls import path
from . import api_views

urlpatterns = [
    path("my-pickups/", api_views.my_pickups_api, name="my_pickups_api"),
]
