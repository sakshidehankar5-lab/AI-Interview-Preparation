# Quick Start Guide - AI Interview Preparation System

## 🚀 Get Started in 5 Minutes

### Prerequisites
- Python 3.8+ installed
- Internet connection
- Web browser (Chrome recommended)

---

## Windows Users - Easiest Method

### 1. Double-click `start.bat`

That's it! The script will:
- Create virtual environment
- Install dependencies
- Set up database
- Start the server

### 2. Get Groq API Key

1. Visit: https://console.groq.com/
2. Sign up (free)
3. Create API key
4. Open `.env` file
5. Replace `your_groq_api_key_here` with your key

### 3. Open Browser

Go to: http://127.0.0.1:8000/

---

## Manual Setup (All Platforms)

### Step 1: Create Virtual Environment
```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create .env File
```bash
copy .env.example .env
```

Add your Groq API key to `.env`

### Step 5: Setup Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Run Server
```bash
python manage.py runserver
```

### Step 7: Open Browser
```
http://127.0.0.1:8000/
```

---

## First Time Usage

### 1. Register
- Click "Get Started"
- Fill in username, email, password
- Click "Register"

### 2. Start Interview
- Click "New Interview"
- Choose interview type (HR/Technical/Behavioral)
- Wait for AI to generate question

### 3. Answer
- Type your answer (100+ words recommended)
- OR use voice recording
- Click "Submit Answer"

### 4. View Results
- See your score out of 10
- Read strengths and weaknesses
- Review improvement suggestions
- Download PDF report

---

## Common Commands

### Start Server
```bash
python manage.py runserver
```

### Create Admin User
```bash
python manage.py createsuperuser
```

### Run Tests
```bash
python manage.py test
```

### Access Admin Panel
```
http://127.0.0.1:8000/admin/
```

---

## Troubleshooting

### Problem: Module not found
**Solution:**
```bash
pip install -r requirements.txt
```

### Problem: Groq API error
**Solution:**
- Check `.env` file exists
- Verify API key is correct
- Check internet connection

### Problem: Port already in use
**Solution:**
```bash
python manage.py runserver 8001
```

### Problem: Database error
**Solution:**
```bash
python manage.py migrate --run-syncdb
```

---

## File Locations

| File | Purpose |
|------|---------|
| `.env` | API keys and settings |
| `db.sqlite3` | Database file |
| `manage.py` | Django management |
| `requirements.txt` | Dependencies |

---

## Important URLs

| URL | Description |
|-----|-------------|
| `/` | Home page |
| `/register/` | Sign up |
| `/login/` | Sign in |
| `/dashboard/` | Your dashboard |
| `/interview/select/` | Choose interview type |
| `/admin/` | Admin panel |

---

## Tips for Success

✅ **DO:**
- Practice regularly (2-3 interviews daily)
- Read feedback carefully
- Use specific examples in answers
- Structure answers with STAR method
- Track your progress

❌ **DON'T:**
- Give one-word answers
- Skip reading the question
- Submit without reviewing
- Ignore the feedback
- Rush through interviews

---

## Getting Help

1. **README.md** - Project overview
2. **INSTALLATION.md** - Detailed setup
3. **USER_GUIDE.md** - How to use the system
4. **PROJECT_DOCUMENTATION.md** - Technical details

---

## What's Next?

After setup:
1. ✅ Complete 3 practice interviews
2. ✅ Try all interview types
3. ✅ Review your dashboard
4. ✅ Download a PDF report
5. ✅ Track your improvement

---

## Support

Need help?
- Check documentation files
- Review error messages
- Verify API key setup
- Check Python version

---

## System Requirements

- **OS**: Windows 10+, Linux, macOS
- **Python**: 3.8 or higher
- **RAM**: 2GB minimum
- **Browser**: Chrome, Firefox, Safari, Edge
- **Internet**: Required for AI features

---

**Ready to start? Run the server and open your browser!**

```bash
python manage.py runserver
```

Then visit: **http://127.0.0.1:8000/**

---

*Happy Interview Preparation! 🎯*
