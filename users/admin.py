from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# Unregister the provided model admin

class CustomUserAdmin(UserAdmin):
    pass