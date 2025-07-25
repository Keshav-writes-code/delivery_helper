from django.urls import path
from . import views

urlpatterns = [path("customer/", views.customer, name="Customer Page")]
