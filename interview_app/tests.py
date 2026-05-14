"""
Tests for the interview application.
"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import UserInterview


class UserInterviewModelTest(TestCase):
    """Test cases for UserInterview model"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_create_interview(self):
        """Test creating an interview record"""
        interview = UserInterview.objects.create(
            user=self.user,
            interview_type='HR',
            question='Tell me about yourself',
            answer='I am a software developer',
            score=8,
            strengths='Good communication',
            weaknesses='Could be more specific',
            suggestions='Add more details',
            confidence_level='High'
        )
        
        self.assertEqual(interview.user, self.user)
        self.assertEqual(interview.interview_type, 'HR')
        self.assertEqual(interview.score, 8)
        self.assertEqual(interview.confidence_level, 'High')


class ViewsTest(TestCase):
    """Test cases for views"""
    
    def setUp(self):
        """Set up test client and user"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_home_page(self):
        """Test home page loads"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_login_page(self):
        """Test login page loads"""
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_register_page(self):
        """Test register page loads"""
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
    
    def test_dashboard_requires_login(self):
        """Test dashboard requires authentication"""
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_dashboard_with_login(self):
        """Test dashboard loads for authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
    
    def test_user_registration(self):
        """Test user registration"""
        response = self.client.post('/register/', {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123',
            'confirm_password': 'newpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(User.objects.filter(username='newuser').exists())
    
    def test_user_login(self):
        """Test user login"""
        response = self.client.post('/login/', {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
