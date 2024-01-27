from django.contrib import admin
from .models import UserAccount, UserProfile

admin.site.register(UserAccount)
admin.site.register(UserProfile)
