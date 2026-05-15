# Render Deployment Guide - AI Interview System

## 🚀 Quick Deployment Steps

### Step 1: Push Changes to GitHub

```bash
git add .
git commit -m "Add Render deployment configuration with WhiteNoise for static files"
git push
```

### Step 2: Create Render Account

1. Go to https://render.com/
2. Sign up with GitHub account
3. Authorize Render to access your repositories

### Step 3: Create New Web Service

1. Click **"New +"** button
2. Select **"Web Service"**
3. Connect your GitHub repository: `AI-Interview-Preparation`
4. Configure the service:

**Basic Settings:**
- **Name:** `ai-interview-system` (or your choice)
- **Region:** Choose closest to you
- **Branch:** `main`
- **Root Directory:** Leave empty
- **Environment:** `Python 3`
- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn ai_interview.wsgi:application`

### Step 4: Add Environment Variables

Click **"Advanced"** and add these environment variables:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.0` |
| `SECRET_KEY` | Generate random string (use Django secret key generator) |
| `DEBUG` | `False` |
| `GROQ_API_KEY` | Your Groq API key from https://console.groq.com/ |
| `ALLOWED_HOSTS` | `your-app-name.onrender.com` |

**Generate SECRET_KEY:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 5: Deploy

1. Click **"Create Web Service"**
2. Wait 5-10 minutes for deployment
3. Render will automatically:
   - Install dependencies
   - Collect static files
   - Run migrations
   - Start the server

### Step 6: Access Your App

Your app will be live at:
```
https://your-app-name.onrender.com
```

---

## 🔧 What Was Fixed for Static Files

### 1. Added WhiteNoise
- Middleware for serving static files in production
- Compresses and caches static files
- No need for separate CDN or storage

### 2. Updated settings.py
```python
# Added WhiteNoise middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # NEW
    ...
]

# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'  # NEW

# WhiteNoise storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # NEW
```

### 3. Updated requirements.txt
```
whitenoise==6.6.0  # For static files
gunicorn==21.2.0   # Production server
```

### 4. Created build.sh
```bash
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

---

## 📋 Troubleshooting

### CSS Still Not Loading?

**1. Check Static Files Collected:**
```bash
python manage.py collectstatic --no-input
```

**2. Check Build Logs on Render:**
- Go to your service dashboard
- Click "Logs"
- Look for "Collecting static files"
- Should show: "X static files copied to '/opt/render/project/src/staticfiles'"

**3. Check Environment Variables:**
- Ensure `DEBUG=False`
- Ensure `ALLOWED_HOSTS` includes your Render domain

**4. Hard Refresh Browser:**
- Press `Ctrl + Shift + R` (Windows/Linux)
- Press `Cmd + Shift + R` (Mac)

**5. Check Network Tab:**
- Open browser DevTools (F12)
- Go to Network tab
- Refresh page
- Check if CSS files return 200 status

### Common Issues

**Issue 1: 404 on Static Files**
```
Solution: Run collectstatic and redeploy
```

**Issue 2: CSS Loads but Styles Don't Apply**
```
Solution: Clear browser cache and hard refresh
```

**Issue 3: Build Fails**
```
Solution: Check build.sh has execute permissions
chmod +x build.sh
```

**Issue 4: WhiteNoise Not Working**
```
Solution: Ensure WhiteNoise is AFTER SecurityMiddleware
and BEFORE all other middleware
```

---

## 🎯 Post-Deployment Checklist

- [ ] App loads without errors
- [ ] CSS and JavaScript load correctly
- [ ] Can register new user
- [ ] Can login
- [ ] Dashboard displays properly
- [ ] Can start interview
- [ ] Questions generate (if API key added)
- [ ] Can submit answers
- [ ] Results page displays correctly
- [ ] PDF download works

---

## 🔐 Security Notes

**For Production:**

1. **Set DEBUG=False** (already done)
2. **Use strong SECRET_KEY** (generate new one)
3. **Set proper ALLOWED_HOSTS** (your domain only)
4. **Use HTTPS** (Render provides this automatically)
5. **Keep .env file secure** (never commit to git)

---

## 📊 Performance Tips

**1. Enable Compression:**
WhiteNoise automatically compresses static files

**2. Browser Caching:**
WhiteNoise sets proper cache headers

**3. Database:**
For production, consider upgrading to PostgreSQL:
```python
# In settings.py
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}
```

**4. Add to requirements.txt:**
```
dj-database-url==2.1.0
psycopg2-binary==2.9.9
```

---

## 🔄 Continuous Deployment

Render automatically redeploys when you push to GitHub:

```bash
# Make changes
git add .
git commit -m "Your changes"
git push

# Render will automatically:
# 1. Detect the push
# 2. Run build.sh
# 3. Deploy new version
```

---

## 📱 Custom Domain (Optional)

1. Go to your service settings
2. Click "Custom Domains"
3. Add your domain
4. Update DNS records as shown
5. Update ALLOWED_HOSTS in environment variables

---

## 💰 Pricing

**Free Tier:**
- 750 hours/month
- Automatic sleep after 15 min inactivity
- Wakes up on request (takes ~30 seconds)

**Paid Tier ($7/month):**
- Always on
- No sleep
- Better performance

---

## 🆘 Need Help?

**Render Documentation:**
https://render.com/docs/deploy-django

**Django Static Files:**
https://docs.djangoproject.com/en/4.2/howto/static-files/

**WhiteNoise Documentation:**
http://whitenoise.evans.io/

---

**Your app should now have CSS working perfectly on Render! 🎉**
