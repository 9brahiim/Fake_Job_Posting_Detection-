# JobCheck – Detecting Fake Job Posts Using NLP

A comprehensive NLP-based system for detecting fraudulent job postings using machine learning and web technologies.

## 📋 Project Overview

This project is divided into 4 main modules, each focusing on a specific aspect of the fake job detection system:

- **Module 1**: Data Collection & Preprocessing
- **Module 2**: Fake Job Classification Model
- **Module 3**: Web Interface & Prediction API
- **Module 4**: Dashboard & Admin Panel

## 🗂️ Project Structure

```
Fake_Job_Detection_NLP/
├── module1_data_preprocessing/    # Data collection and preprocessing
├── module2_model_training/        # ML model development and evaluation
├── module3_web_interface/         # Flask/FastAPI backend and frontend
├── module4_dashboard/             # Admin panel and analytics dashboard
├── data/                          # Dataset storage
├── models/                        # Saved ML models and vectorizers
├── logs/                          # Application logs
├── config/                        # Configuration files
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip or conda

### Installation

1. Clone the repository:
```bash
git clone https://github.com/9brahiim/Fake_Job_Posting_Detection-.git
cd Fake_Job_Detection_NLP
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction) and place it in the `data/` directory.

## 📚 Module Descriptions

### Module 1: Data Collection & Preprocessing
**Location**: `module1_data_preprocessing/`

- Load and inspect the Fake Job Postings dataset
- Merge textual fields (Job Description + Requirements + Benefits)
- Clean and normalize text (lowercase, remove HTML, punctuation, stopwords)
- Extract features using TF-IDF vectorization
- Output: Cleaned and vectorized data ready for ML models

### Module 2: Fake Job Classification Model
**Location**: `module2_model_training/`

- Train baseline models: Logistic Regression and Random Forest
- Evaluate models using Accuracy, Precision, Recall, F1-Score
- Compare model performance
- Save best model and TF-IDF vectorizer as `.pkl` files
- Target: Accuracy > 90%

### Module 3: Web Interface & Prediction API
**Location**: `module3_web_interface/`

- Flask/FastAPI backend for prediction API
- Web form for user input
- Real-time prediction with confidence scores
- Preprocessing pipeline matching training phase

### Module 4: Dashboard & Admin Panel
**Location**: `module4_dashboard/`

- Secure admin authentication (JWT)
- Prediction analytics and visualization
- Export functionality (CSV/PDF)
- Model retraining capabilities
- Database integration for prediction logs

## 🗓️ Week-Wise Execution Strategy

- **Weeks 1–2**: Data & NLP (Module 1)
- **Weeks 3–4**: Model Development (Module 2)
- **Weeks 5–6**: Web Application (Module 3)
- **Weeks 7–8**: Admin & Dashboard (Module 4)

## 👥 Contributing

Each module is designed to be worked on independently. Please follow these guidelines:

1. Create a branch for your module: `git checkout -b module1-data-preprocessing`
2. Work on your assigned module
3. Test your code thoroughly
4. Submit a pull request with a clear description

## 📝 Dataset

The project uses the **Fake Job Postings** dataset from Kaggle:
- [Dataset Link](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)

Key attributes:
- Job Title
- Company Profile
- Job Description
- Requirements
- Benefits
- Fraudulent label (0 – Real, 1 – Fake)

## 🛠️ Technology Stack

- **NLP**: NLTK, spaCy, scikit-learn
- **ML**: scikit-learn, TensorFlow/PyTorch (optional)
- **Backend**: Flask/FastAPI
- **Frontend**: HTML, CSS, Bootstrap (React optional)
- **Database**: SQLite/MySQL/PostgreSQL
- **Visualization**: Chart.js

## 📊 Expected Results

- **Accuracy**: > 90%
- **F1-Score**: Strong balanced performance
- **Real-time Prediction**: < 2 seconds response time

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

9brahiim

## 🙏 Acknowledgments

- Kaggle for providing the dataset
- Open source community for tools and libraries
