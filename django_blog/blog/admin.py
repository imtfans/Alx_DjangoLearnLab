
from django.contrib import admin
from .models import Profile  # <-- import from models.py directly
admin.site.register(Profile)
