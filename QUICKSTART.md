# Quick Start Guide

This document provides step-by-step instructions for setting up and running the Fake Job Detection system.

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Git version control system

## Installation Procedure

### Step 1: Repository Cloning

```bash
git clone https://github.com/9brahiim/Fake_Job_Posting_Detection-.git
cd Fake_Job_Detection_NLP
```

### Step 2: Virtual Environment Setup

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

### Step 3: Dependency Installation

```bash
pip install -r requirements.txt
```

### Step 4: Environment Initialization

```bash
python setup.py
```

This script performs the following operations:
- Creates required directory structure
- Validates package installation
- Downloads NLTK language resources

### Step 5: Dataset Acquisition

1. Access the [Kaggle Dataset](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)
2. Download the dataset file
3. Place the CSV file in the `data/` directory with filename `fake_job_postings.csv`

## Module Execution

### Module 1: Data Preprocessing

```bash
python module1_data_preprocessing/main.py
```

**Output Artifacts**:
- Processed dataset: `data/processed_data.csv`
- TF-IDF vectorizer: `models/tfidf_vectorizer.pkl`

### Module 2: Model Training

```bash
python module2_model_training/main.py
```

**Output Artifacts**:
- Trained models in `models/` directory
- Best performing model selection
- Evaluation metrics report

### Module 3: Web Interface Deployment

```bash
python module3_web_interface/app.py
```

**Service Endpoints**:
- Web Interface: http://localhost:5000
- Prediction API: http://localhost:5000/predict
- Health Check: http://localhost:5000/health

### Module 4: Administrative Dashboard

The administrative dashboard is integrated with Module 3.

**Access Points**:
- Admin Login: http://localhost:5000/admin/login
- Admin Dashboard: http://localhost:5000/admin/dashboard

**Default Credentials**:
- Username: `admin`
- Password: `admin123`

**Security Note**: Change default credentials before production deployment.

## API Testing

### cURL Request Example

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "job_description": "We are seeking a software engineer...",
    "requirements": "Python, Machine Learning",
    "benefits": "Health insurance, Remote work"
  }'
```

### Python Client Example

```python
import requests

response = requests.post('http://localhost:5000/predict', json={
    'job_description': 'We are seeking a software engineer...',
    'requirements': 'Python, Machine Learning',
    'benefits': 'Health insurance, Remote work'
})

print(response.json())
```

## Development Workflow

1. **Weeks 1-2**: Complete Module 1 (Data Preprocessing)
2. **Weeks 3-4**: Complete Module 2 (Model Training)
3. **Weeks 5-6**: Complete Module 3 (Web Interface)
4. **Weeks 7-8**: Complete Module 4 (Administrative Dashboard)

## Troubleshooting

### Import Errors

Verify the following:
- Current working directory is the project root
- Virtual environment is activated
- All dependencies are installed correctly

### Dataset Not Found

Ensure the dataset file is named `fake_job_postings.csv` and located in the `data/` directory.

### Model Not Found

Execute Module 2 (Model Training) before running Module 3 (Web Interface).

### Database Errors

The database is automatically initialized on first application run. If errors occur, delete `jobcheck.db` and restart the application.

## Additional Resources

- Refer to `CONTRIBUTING.md` for collaboration guidelines
- Review `README.md` for comprehensive project documentation
- Consult module-specific README files in each module directory

## Support

For technical issues or inquiries, please create an issue in the GitHub repository.
