"""
Main URL configuration for the Maternal Care Management System.
"""

from django.contrib import admin
from django.urls import path

# Import our Django Ninja API instance
from config.api import api

urlpatterns = [
    # Django admin panel
    path("admin/", admin.site.urls),

    # API routes
    path("api/", api.urls),
]