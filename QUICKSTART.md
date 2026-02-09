# Quick Start Guide

This guide will help you get started with the Fake Job Detection project quickly.

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for cloning the repository)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/9brahiim/Fake_Job_Posting_Detection-.git
cd Fake_Job_Detection_NLP
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Setup Script

```bash
python setup.py
```

This will:
- Create necessary directories
- Check for required packages
- Download NLTK data

### 5. Download Dataset

1. Visit [Kaggle Dataset](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)
2. Download the dataset
3. Place the CSV file in the `data/` directory as `fake_job_postings.csv`

## Running the Modules

### Module 1: Data Preprocessing

```bash
python module1_data_preprocessing/main.py
```

**Expected Output:**
- Processed data saved to `data/processed_data.csv`
- TF-IDF vectorizer saved to `models/tfidf_vectorizer.pkl`

### Module 2: Model Training

```bash
python module2_model_training/main.py
```

**Expected Output:**
- Trained models saved to `models/` directory
- Best model selected and saved
- Evaluation metrics displayed

### Module 3: Web Interface

```bash
python module3_web_interface/app.py
```

**Access:**
- Web Interface: http://localhost:5000
- API Endpoint: http://localhost:5000/predict
- Health Check: http://localhost:5000/health

### Module 4: Admin Dashboard

The admin dashboard is integrated with Module 3.

**Access:**
- Admin Login: http://localhost:5000/admin/login
- Admin Dashboard: http://localhost:5000/admin/dashboard

**Default Credentials:**
- Username: `admin`
- Password: `admin123`

⚠️ **Change these in production!**

## Testing the API

### Using cURL

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "job_description": "We are looking for a software engineer...",
    "requirements": "Python, Machine Learning",
    "benefits": "Health insurance, Remote work"
  }'
```

### Using Python

```python
import requests

response = requests.post('http://localhost:5000/predict', json={
    'job_description': 'We are looking for a software engineer...',
    'requirements': 'Python, Machine Learning',
    'benefits': 'Health insurance, Remote work'
})

print(response.json())
```

## Project Workflow

1. **Week 1-2**: Complete Module 1 (Data Preprocessing)
2. **Week 3-4**: Complete Module 2 (Model Training)
3. **Week 5-6**: Complete Module 3 (Web Interface)
4. **Week 7-8**: Complete Module 4 (Admin Dashboard)

## Troubleshooting

### Import Errors

If you encounter import errors, make sure:
- You're in the project root directory
- Virtual environment is activated
- All dependencies are installed

### Dataset Not Found

Ensure the dataset file is named `fake_job_postings.csv` and placed in the `data/` directory.

### Model Not Found

Run Module 2 (Model Training) before using Module 3 (Web Interface).

### Database Errors

The database will be created automatically on first run. If you encounter errors, delete `jobcheck.db` and restart the application.

## Next Steps

- Read `CONTRIBUTING.md` for collaboration guidelines
- Check `README.md` for detailed project information
- Review module-specific README files in each module directory

## Support

For issues or questions, please open an issue on GitHub.
