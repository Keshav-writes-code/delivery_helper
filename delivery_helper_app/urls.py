from django.urls import path
from . import views

urlpatterns = [
    path("api/customer_order_location", views.get_customer_locations),
    path("api/delete_customer_locations", views.delete_customer_locations),
    path("api/add_modify_locations", views.add_or_modify_location),
    path("api/get_delivery_agent_orders/", views.get_delivery_agent_orders),
]
