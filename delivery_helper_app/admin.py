from django.contrib import admin
from .models import user_types, Profile, customer_order, UserManager

# Register your models here.
admin.site.register(user_types)
admin.site.register(Profile)
admin.site.register(customer_order)
