"""
Database models for the interview application.
"""
from django.db import models
from django.contrib.auth.models import User


class UserInterview(models.Model):
    """
    Model to store interview sessions and results.
    """
    INTERVIEW_TYPES = [
        ('HR', 'HR Interview'),
        ('Technical', 'Technical Interview'),
        ('Behavioral', 'Behavioral Interview'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interviews')
    interview_type = models.CharField(max_length=20, choices=INTERVIEW_TYPES)
    question = models.TextField()
    answer = models.TextField()
    score = models.IntegerField(default=0)
    feedback = models.TextField(blank=True)
    strengths = models.TextField(blank=True)
    weaknesses = models.TextField(blank=True)
    suggestions = models.TextField(blank=True)
    confidence_level = models.CharField(max_length=20, default='Medium')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.interview_type} - {self.created_at.strftime('%Y-%m-%d')}"
