from django.contrib import admin
from .models import MyUser,UserOTP

# Register your models here.
@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
	list_display=['username']
	date_hierarchy='date_joined'