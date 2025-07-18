from django.contrib import admin

# Register your models here.
#google_map_app/models

from .models import Student,user_table
admin.site.register(Student)
admin.site.register(user_table)

