from django.contrib import admin
from .models import UserProfile, Log

admin.site.register(UserProfile)
admin.site.register(Log)