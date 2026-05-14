"""
Setup script for AI Interview Preparation System
"""
import os
import sys
import subprocess

def create_env_file():
    """Create .env file if it doesn't exist"""
    if not os.path.exists('.env'):
        print("Creating .env file...")
        with open('.env', 'w') as f:
            f.write("GROQ_API_KEY=your_groq_api_key_here\n")
            f.write("SECRET_KEY=django-insecure-change-this-in-production\n")
            f.write("DEBUG=True\n")
        print("✓ .env file created. Please add your Groq API key.")
    else:
        print("✓ .env file already exists.")

def install_dependencies():
    """Install required packages"""
    print("\nInstalling dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully.")
    except subprocess.CalledProcessError:
        print("✗ Error installing dependencies.")
        return False
    return True

def run_migrations():
    """Run Django migrations"""
    print("\nRunning database migrations...")
    try:
        subprocess.check_call([sys.executable, "manage.py", "makemigrations"])
        subprocess.check_call([sys.executable, "manage.py", "migrate"])
        print("✓ Migrations completed successfully.")
    except subprocess.CalledProcessError:
        print("✗ Error running migrations.")
        return False
    return True

def main():
    """Main setup function"""
    print("=" * 60)
    print("AI Interview Preparation System - Setup")
    print("=" * 60)
    
    # Create .env file
    create_env_file()
    
    # Install dependencies
    if not install_dependencies():
        print("\nSetup failed. Please check the errors above.")
        return
    
    # Run migrations
    if not run_migrations():
        print("\nSetup failed. Please check the errors above.")
        return
    
    print("\n" + "=" * 60)
    print("Setup completed successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Add your Groq API key to the .env file")
    print("2. Run: python manage.py runserver")
    print("3. Open: http://127.0.0.1:8000/")
    print("\nGet Groq API key from: https://console.groq.com/")
    print("=" * 60)

if __name__ == "__main__":
    main()
