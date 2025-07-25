from django.urls import path
from . import views

urlpatterns = [
    path(
        "/api/get_delivery_location",
        views.get_delivery_location,
    ),
    path("/api/get_customer_locations", views.get_customer_locations),
    path("/api/delete_customer_locations", views.delete_customer_locations),
    path("/api/add_or_modify_location", views.add_or_modify_location),
]
