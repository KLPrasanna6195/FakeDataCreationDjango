from django.contrib import admin
from .models import users


# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display=['id','real_name','tz','activity_periods','start_time','End_time']

admin.site.register(users,UsersAdmin)