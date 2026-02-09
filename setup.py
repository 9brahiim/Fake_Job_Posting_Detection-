"""
Setup script for the Fake Job Detection project.
Helps initialize the project environment.
"""

import os
import sys
from pathlib import Path


def create_directories():
    """Create necessary directories if they don't exist."""
    directories = [
        'data',
        'models',
        'logs',
        'config',
        'module3_web_interface/static/css',
        'module3_web_interface/static/js',
        'module3_web_interface/templates',
        'module4_dashboard/templates/admin',
        'module4_dashboard/static/admin'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {directory}")


def check_dependencies():
    """Check if required dependencies are installed."""
    required_packages = [
        'pandas',
        'numpy',
        'sklearn',
        'flask',
        'nltk',
        'beautifulsoup4'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("\n⚠ Missing packages:")
        for package in missing_packages:
            print(f"  - {package}")
        print("\nInstall missing packages with:")
        print("  pip install -r requirements.txt")
        return False
    else:
        print("\n✓ All required packages are installed")
        return True


def download_nltk_data():
    """Download required NLTK data."""
    try:
        import nltk
        print("\nDownloading NLTK data...")
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        print("✓ NLTK data downloaded")
    except Exception as e:
        print(f"⚠ Warning: Could not download NLTK data: {e}")


def main():
    """Main setup function."""
    print("="*60)
    print("JobCheck - Project Setup")
    print("="*60)
    
    print("\n[Step 1/4] Creating directories...")
    create_directories()
    
    print("\n[Step 2/4] Checking dependencies...")
    deps_ok = check_dependencies()
    
    print("\n[Step 3/4] Downloading NLTK data...")
    download_nltk_data()
    
    print("\n[Step 4/4] Setup complete!")
    print("\n" + "="*60)
    print("Next steps:")
    print("1. Download the dataset from Kaggle:")
    print("   https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction")
    print("2. Place the dataset in the 'data/' directory")
    print("3. Run Module 1: python module1_data_preprocessing/main.py")
    print("4. Run Module 2: python module2_model_training/main.py")
    print("5. Run Module 3: python module3_web_interface/app.py")
    print("="*60)
    
    if not deps_ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
