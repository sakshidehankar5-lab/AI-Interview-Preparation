# AI Interview Preparation System

A complete Django web application that simulates real interviews using AI and provides intelligent feedback on user answers.

## Features

- **User Authentication**: Register, login, and logout functionality
- **Multiple Interview Types**: HR, Technical, and Behavioral interviews
- **AI-Powered Questions**: Dynamic question generation using Groq AI
- **Flexible Answer Input**: Type or use voice recording
- **Intelligent Evaluation**: AI provides scores, strengths, weaknesses, and suggestions
- **Progress Dashboard**: Track interview history and performance
- **PDF Reports**: Download detailed interview reports

## Tech Stack

- **Backend**: Django 4.2.7, Python
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **AI**: Groq API (llama3-8b-8192 model)
- **PDF Generation**: ReportLab

## Installation

### 1. Clone or Download the Project

```bash
cd ai_interview_system
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
SECRET_KEY=your_django_secret_key_here
DEBUG=True
```

**Get Groq API Key:**
1. Visit https://console.groq.com/
2. Sign up for a free account
3. Generate an API key
4. Copy and paste it into your `.env` file

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

### 9. Access the Application

Open your browser and go to:
```
http://127.0.0.1:8000/
```

## Usage

1. **Register**: Create a new account
2. **Login**: Sign in with your credentials
3. **Select Interview Type**: Choose HR, Technical, or Behavioral
4. **Answer Questions**: Type or speak your answers
5. **Get Feedback**: Receive AI evaluation with scores and suggestions
6. **Track Progress**: View your dashboard for performance analytics
7. **Download Reports**: Export interview results as PDF

## Project Structure

```
ai_interview_system/
│
├── manage.py
├── requirements.txt
├── .env
├── .env.example
├── README.md
│
├── ai_interview/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── interview_app/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   └── ai_service.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── interview_selection.html
│   ├── interview.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── db.sqlite3
```

## Features Breakdown

### AI Service (`ai_service.py`)
- Question generation based on interview type
- Answer evaluation with detailed feedback
- Fallback mechanisms for API failures
- JSON response parsing and validation

### Models (`models.py`)
- UserInterview: Stores interview sessions and results
- Fields: user, interview_type, question, answer, score, feedback, etc.

### Views (`views.py`)
- Authentication views (register, login, logout)
- Dashboard with statistics
- Interview flow (selection, start, submit)
- API endpoints for AJAX requests
- PDF report generation

### Templates
- Responsive design with modern UI
- Dark blue and white theme
- Smooth animations and transitions
- Mobile-friendly layout

### JavaScript Features
- Voice recording using Web Speech API
- Real-time character counting
- Timer during interviews
- AJAX for seamless question loading and submission
- Form validation

## API Endpoints

- `GET /api/get-question/` - Get a new interview question
- `POST /api/submit-answer/` - Submit answer for evaluation

## Security Features

- CSRF protection
- Secure authentication
- Environment variables for sensitive data
- Password validation
- Login required decorators

## Browser Compatibility

- Chrome (recommended for voice recording)
- Firefox
- Safari
- Edge

**Note**: Voice recording feature requires HTTPS in production or localhost for development.

## Troubleshooting

### Issue: Groq API Error
**Solution**: Verify your API key in `.env` file and check your internet connection.

### Issue: Voice Recording Not Working
**Solution**: Use Chrome browser and ensure microphone permissions are granted.

### Issue: Database Errors
**Solution**: Run migrations again:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue: Static Files Not Loading
**Solution**: Run:
```bash
python manage.py collectstatic
```

## Future Enhancements

- Multiple interview rounds
- Video recording support
- Interview scheduling
- Email notifications
- Advanced analytics
- Multi-language support
- Mock interview with peers
- Industry-specific questions

## License

This project is open-source and available for educational purposes.

## Support

For issues or questions, please create an issue in the repository.

## Credits

- Built with Django
- Powered by Groq AI (llama3-8b-8192)
- Icons by Font Awesome
- PDF generation by ReportLab

---

**Happy Interview Preparation! 🚀**
