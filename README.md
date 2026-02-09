# JobCheck – Fake Job Posting Detection System

An enterprise-grade Natural Language Processing (NLP) system for automated detection and classification of fraudulent job postings using machine learning algorithms and web-based interfaces.

## Project Overview

This system implements a comprehensive solution for identifying fraudulent job postings through a modular architecture consisting of four integrated components:

- **Module 1**: Data Collection & Preprocessing
- **Module 2**: Machine Learning Model Training & Evaluation
- **Module 3**: Web Interface & RESTful API
- **Module 4**: Administrative Dashboard & Analytics

## Architecture

```
Fake_Job_Detection_NLP/
├── module1_data_preprocessing/    # Data collection and preprocessing pipeline
├── module2_model_training/        # ML model development and evaluation
├── module3_web_interface/         # Flask/FastAPI backend and frontend
├── module4_dashboard/             # Administrative panel and analytics dashboard
├── data/                          # Dataset storage
├── models/                        # Serialized ML models and vectorizers
├── logs/                          # Application logs
├── config/                        # Configuration management
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Git version control system

## Installation

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

## Module Specifications

### Module 1: Data Collection & Preprocessing
**Directory**: `module1_data_preprocessing/`

**Functionality**:
- Dataset loading and validation
- Text field aggregation (Job Description, Requirements, Benefits)
- Text normalization and cleaning (case conversion, HTML tag removal, punctuation elimination, stopword removal)
- Feature extraction using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization
- Output: Preprocessed and vectorized dataset for machine learning pipeline

### Module 2: Machine Learning Model Training & Evaluation
**Directory**: `module2_model_training/`

**Functionality**:
- Implementation of baseline classification models: Logistic Regression and Random Forest
- Model evaluation using standard metrics: Accuracy, Precision, Recall, F1-Score
- Comparative performance analysis
- Model serialization (saved as `.pkl` files)
- Performance target: Accuracy ≥ 90%

### Module 3: Web Interface & Prediction API
**Directory**: `module3_web_interface/`

**Functionality**:
- RESTful API implementation using Flask/FastAPI framework
- Web-based user interface for job posting submission
- Real-time prediction with confidence score calculation
- Preprocessing pipeline consistency with training phase

### Module 4: Administrative Dashboard & Analytics
**Directory**: `module4_dashboard/`

**Functionality**:
- Secure authentication system using JWT (JSON Web Tokens)
- Prediction analytics and statistical visualization
- Data export capabilities (CSV, PDF formats)
- Model retraining interface
- Database integration for prediction logging and audit trails

## Development Timeline

- **Weeks 1–2**: Data preprocessing and NLP pipeline (Module 1)
- **Weeks 3–4**: Machine learning model development (Module 2)
- **Weeks 5–6**: Web application development (Module 3)
- **Weeks 7–8**: Administrative dashboard implementation (Module 4)

## Contributing

This project follows a modular development approach where each component can be developed independently. Contributors should adhere to the following guidelines:

1. Create a feature branch for your assigned module: `git checkout -b module1-data-preprocessing`
2. Implement functionality within your assigned module
3. Conduct comprehensive testing
4. Submit a pull request with detailed description of changes

For detailed contribution guidelines, refer to `CONTRIBUTING.md`.

## Dataset

This project utilizes the **Fake Job Postings** dataset available on Kaggle:
- [Dataset Repository](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)

**Dataset Schema**:
- Job Title
- Company Profile
- Job Description
- Requirements
- Benefits
- Fraudulent label (0 = Legitimate, 1 = Fraudulent)

## Technology Stack

- **Natural Language Processing**: NLTK, spaCy, scikit-learn
- **Machine Learning**: scikit-learn, TensorFlow/PyTorch (optional)
- **Backend Framework**: Flask/FastAPI
- **Frontend**: HTML5, CSS3, Bootstrap (React.js optional)
- **Database**: SQLite/MySQL/PostgreSQL
- **Data Visualization**: Chart.js

## Performance Metrics

- **Classification Accuracy**: ≥ 90%
- **F1-Score**: Balanced precision-recall performance
- **API Response Time**: < 2 seconds per prediction


## Acknowledgments

- Kaggle for providing the dataset
- Open source community for tools and libraries
