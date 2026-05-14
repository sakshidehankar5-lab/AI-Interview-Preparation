"""
Admin configuration for interview app.
"""
from django.contrib import admin
from .models import UserInterview


@admin.register(UserInterview)
class UserInterviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'interview_type', 'score', 'created_at']
    list_filter = ['interview_type', 'created_at']
    search_fields = ['user__username', 'question', 'answer']
    readonly_fields = ['created_at']
