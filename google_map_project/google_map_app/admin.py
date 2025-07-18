from django.contrib import admin

# Register your models here.
#google_map_app/models

from .models import Student,user_table,location_table,customer_order,order_assign
admin.site.register(Student)
admin.site.register(user_table)
admin.site.register(location_table)
admin.site.register(customer_order)
admin.site.register(order_assign)

