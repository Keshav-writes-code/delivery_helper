from django.contrib import admin
from .models import user_types,Profile,location,customer_order

admin.site.register(user_types)
admin.site.register(Profile)
admin.site.register(location)
admin.site.register(customer_order)

