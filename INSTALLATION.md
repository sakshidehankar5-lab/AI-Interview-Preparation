# Installation Guide - AI Interview Preparation System

## Quick Start (Automated Setup)

### Windows

1. **Open Command Prompt or PowerShell**

2. **Navigate to project directory**
   ```bash
   cd ai_interview_system
   ```

3. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

4. **Activate virtual environment**
   ```bash
   venv\Scripts\activate
   ```

5. **Run setup script**
   ```bash
   python setup.py
   ```

6. **Add Groq API Key**
   - Open `.env` file
   - Replace `your_groq_api_key_here` with your actual API key
   - Get API key from: https://console.groq.com/

7. **Start the server**
   ```bash
   python manage.py runserver
   ```

8. **Open browser**
   ```
   http://127.0.0.1:8000/
   ```

---

## Manual Installation

### Step 1: Prerequisites

Make sure you have:
- Python 3.8 or higher
- pip (Python package manager)
- Internet connection

Check Python version:
```bash
python --version
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**Windows (CMD):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Create .env File

Create a file named `.env` in the project root with:

```env
GROQ_API_KEY=your_groq_api_key_here
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=True
```

### Step 6: Get Groq API Key

1. Visit https://console.groq.com/
2. Sign up for a free account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key and paste it in your `.env` file

### Step 7: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 8: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 9: Run Development Server

```bash
python manage.py runserver
```

### Step 10: Access Application

Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

---

## Verification

After installation, verify everything works:

1. **Home Page**: Should load without errors
2. **Register**: Create a test account
3. **Login**: Sign in with test account
4. **Dashboard**: Should display empty state
5. **Start Interview**: Select interview type
6. **Question Generation**: AI should generate a question
7. **Submit Answer**: Should receive evaluation

---

## Common Issues

### Issue 1: Module Not Found Error

**Error**: `ModuleNotFoundError: No module named 'django'`

**Solution**:
```bash
pip install -r requirements.txt
```

### Issue 2: Groq API Error

**Error**: `GROQ_API_KEY not found`

**Solution**:
- Verify `.env` file exists
- Check API key is correct
- Ensure no extra spaces in `.env` file

### Issue 3: Database Locked

**Error**: `database is locked`

**Solution**:
```bash
python manage.py migrate --run-syncdb
```

### Issue 4: Port Already in Use

**Error**: `Error: That port is already in use`

**Solution**:
```bash
python manage.py runserver 8001
```

### Issue 5: Static Files Not Loading

**Solution**:
```bash
python manage.py collectstatic
```

---

## Testing the Application

### Test User Registration
1. Go to http://127.0.0.1:8000/register/
2. Fill in the form
3. Submit and verify redirect to dashboard

### Test Interview Flow
1. Click "New Interview"
2. Select interview type
3. Wait for question generation
4. Type or speak an answer
5. Submit and check evaluation

### Test Dashboard
1. Complete multiple interviews
2. Check statistics update
3. Verify recent interviews list
4. Download PDF report

---

## Production Deployment

For production deployment:

1. **Set DEBUG to False**
   ```env
   DEBUG=False
   ```

2. **Set Allowed Hosts**
   ```python
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

3. **Use PostgreSQL** (recommended)
   ```bash
   pip install psycopg2-binary
   ```

4. **Collect Static Files**
   ```bash
   python manage.py collectstatic
   ```

5. **Use Production Server**
   ```bash
   pip install gunicorn
   gunicorn ai_interview.wsgi:application
   ```

6. **Set Up HTTPS** (required for voice recording)

---

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| GROQ_API_KEY | Groq AI API key | Yes |
| SECRET_KEY | Django secret key | Yes |
| DEBUG | Debug mode (True/False) | Yes |

---

## System Requirements

- **OS**: Windows 10+, Linux, macOS
- **Python**: 3.8 or higher
- **RAM**: 2GB minimum
- **Disk Space**: 500MB
- **Browser**: Chrome (recommended), Firefox, Safari, Edge

---

## Getting Help

If you encounter issues:

1. Check this installation guide
2. Review the README.md file
3. Check Django documentation: https://docs.djangoproject.com/
4. Check Groq documentation: https://console.groq.com/docs

---

## Next Steps

After successful installation:

1. Explore the dashboard
2. Try different interview types
3. Test voice recording feature
4. Download PDF reports
5. Track your progress

---

**Congratulations! Your AI Interview Preparation System is ready to use! 🎉**
