from django.urls import path
from . import views

urlpatterns = [
    path("/api/get_delivery_location",views.get_delivery_location),
    path("show_orders/", views.show_orders),
    path("api/customer_order_location",views.get_customer_locations),
    path("api/add_modify_locations",views.add_or_modify_location),

]
