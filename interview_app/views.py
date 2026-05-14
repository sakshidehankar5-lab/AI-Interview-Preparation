"""
Views for the interview application.
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Count
from .models import UserInterview
from .ai_service import AIInterviewService
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
import json
from datetime import datetime


def home(request):
    """Home page view."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')


def register_view(request):
    """User registration view."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Validation
        if not all([username, email, password, confirm_password]):
            messages.error(request, 'All fields are required.')
            return render(request, 'register.html')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'register.html')
        
        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, 'Registration successful!')
        return redirect('dashboard')
    
    return render(request, 'register.html')


def login_view(request):
    """User login view."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')


@login_required
def logout_view(request):
    """User logout view."""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


@login_required
def dashboard(request):
    """User dashboard view."""
    interviews = UserInterview.objects.filter(user=request.user)
    
    # Calculate statistics
    total_interviews = interviews.count()
    avg_score = interviews.aggregate(Avg('score'))['score__avg'] or 0
    
    # Interview type breakdown
    interview_stats = interviews.values('interview_type').annotate(
        count=Count('id'),
        avg_score=Avg('score')
    )
    
    # Add progress width for each stat (score * 10 for percentage)
    interview_stats_list = []
    for stat in interview_stats:
        stat_dict = dict(stat)
        stat_dict['progress_width'] = int((stat['avg_score'] or 0) * 10)
        interview_stats_list.append(stat_dict)
    
    # Recent interviews
    recent_interviews = interviews[:5]
    
    context = {
        'total_interviews': total_interviews,
        'avg_score': round(avg_score, 1),
        'interview_stats': interview_stats_list,
        'recent_interviews': recent_interviews,
    }
    
    return render(request, 'dashboard.html', context)


@login_required
def interview_selection(request):
    """Interview type selection view."""
    return render(request, 'interview_selection.html')


@login_required
def start_interview(request, interview_type):
    """Start a new interview session."""
    if interview_type not in ['HR', 'Technical', 'Behavioral']:
        messages.error(request, 'Invalid interview type.')
        return redirect('interview_selection')
    
    # Store interview type in session
    request.session['interview_type'] = interview_type
    
    return render(request, 'interview.html', {'interview_type': interview_type})


@login_required
def get_question(request):
    """API endpoint to get a new interview question."""
    if request.method == 'GET':
        interview_type = request.session.get('interview_type', 'HR')
        
        try:
            ai_service = AIInterviewService()
            question = ai_service.generate_question(interview_type)
            
            return JsonResponse({
                'success': True,
                'question': question,
                'interview_type': interview_type
            })
        
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)


@login_required
def submit_answer(request):
    """API endpoint to submit and evaluate an answer."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question = data.get('question')
            answer = data.get('answer')
            interview_type = request.session.get('interview_type', 'HR')
            
            if not question or not answer:
                return JsonResponse({
                    'success': False,
                    'error': 'Question and answer are required'
                }, status=400)
            
            # Evaluate answer using AI
            ai_service = AIInterviewService()
            evaluation = ai_service.evaluate_answer(question, answer, interview_type)
            
            # Save to database
            interview = UserInterview.objects.create(
                user=request.user,
                interview_type=interview_type,
                question=question,
                answer=answer,
                score=evaluation['score'],
                strengths=evaluation['strengths'],
                weaknesses=evaluation['weaknesses'],
                suggestions=evaluation['suggestions'],
                confidence_level=evaluation['confidence']
            )
            
            return JsonResponse({
                'success': True,
                'interview_id': interview.id,
                'evaluation': evaluation
            })
        
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)


@login_required
def interview_result(request, interview_id):
    """Display interview result."""
    try:
        interview = UserInterview.objects.get(id=interview_id, user=request.user)
        return render(request, 'result.html', {'interview': interview})
    except UserInterview.DoesNotExist:
        messages.error(request, 'Interview not found.')
        return redirect('dashboard')


@login_required
def download_report(request, interview_id):
    """Download interview report as PDF."""
    try:
        interview = UserInterview.objects.get(id=interview_id, user=request.user)
        
        # Create PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="interview_report_{interview_id}.pdf"'
        
        doc = SimpleDocTemplate(response, pagesize=letter)
        story = []
        styles = getSampleStyleSheet()
        
        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1e3a8a'),
            spaceAfter=30,
            alignment=1
        )
        story.append(Paragraph('Interview Report', title_style))
        story.append(Spacer(1, 0.3*inch))
        
        # Interview details
        details_data = [
            ['Candidate:', request.user.username],
            ['Interview Type:', interview.interview_type],
            ['Date:', interview.created_at.strftime('%Y-%m-%d %H:%M')],
            ['Score:', f'{interview.score}/10'],
            ['Confidence Level:', interview.confidence_level],
        ]
        
        details_table = Table(details_data, colWidths=[2*inch, 4*inch])
        details_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e0e7ff')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ]))
        story.append(details_table)
        story.append(Spacer(1, 0.3*inch))
        
        # Question
        story.append(Paragraph('<b>Question:</b>', styles['Heading2']))
        story.append(Paragraph(interview.question, styles['BodyText']))
        story.append(Spacer(1, 0.2*inch))
        
        # Answer
        story.append(Paragraph('<b>Your Answer:</b>', styles['Heading2']))
        story.append(Paragraph(interview.answer, styles['BodyText']))
        story.append(Spacer(1, 0.2*inch))
        
        # Evaluation
        story.append(Paragraph('<b>Strengths:</b>', styles['Heading2']))
        story.append(Paragraph(interview.strengths, styles['BodyText']))
        story.append(Spacer(1, 0.2*inch))
        
        story.append(Paragraph('<b>Weaknesses:</b>', styles['Heading2']))
        story.append(Paragraph(interview.weaknesses, styles['BodyText']))
        story.append(Spacer(1, 0.2*inch))
        
        story.append(Paragraph('<b>Suggestions for Improvement:</b>', styles['Heading2']))
        story.append(Paragraph(interview.suggestions, styles['BodyText']))
        
        doc.build(story)
        return response
    
    except UserInterview.DoesNotExist:
        messages.error(request, 'Interview not found.')
        return redirect('dashboard')
