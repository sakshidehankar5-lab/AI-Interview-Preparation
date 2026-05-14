"""
URL configuration for interview app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('interview/select/', views.interview_selection, name='interview_selection'),
    path('interview/start/<str:interview_type>/', views.start_interview, name='start_interview'),
    path('api/get-question/', views.get_question, name='get_question'),
    path('api/submit-answer/', views.submit_answer, name='submit_answer'),
    path('interview/result/<int:interview_id>/', views.interview_result, name='interview_result'),
    path('interview/download/<int:interview_id>/', views.download_report, name='download_report'),
]
