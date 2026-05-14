"""
URL configuration for ai_interview project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('interview_app.urls')),
]
