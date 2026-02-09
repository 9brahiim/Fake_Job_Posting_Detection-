"""
Configuration file for the Fake Job Detection project.
Contains all settings and constants used across modules.
"""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Data paths
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_PATH = DATA_DIR / "fake_job_postings.csv"
PROCESSED_DATA_PATH = DATA_DIR / "processed_data.csv"

# Model paths
MODELS_DIR = PROJECT_ROOT / "models"
TFIDF_VECTORIZER_PATH = MODELS_DIR / "tfidf_vectorizer.pkl"
LOGISTIC_REGRESSION_MODEL_PATH = MODELS_DIR / "logistic_regression_model.pkl"
RANDOM_FOREST_MODEL_PATH = MODELS_DIR / "random_forest_model.pkl"
BEST_MODEL_PATH = MODELS_DIR / "best_model.pkl"

# Logs path
LOGS_DIR = PROJECT_ROOT / "logs"

# ML Model Configuration
TEST_SIZE = 0.2
RANDOM_STATE = 42
TARGET_ACCURACY = 0.90

# TF-IDF Configuration
MAX_FEATURES = 5000
NGRAM_RANGE = (1, 2)
MIN_DF = 2
MAX_DF = 0.95

# Text Preprocessing Configuration
REMOVE_STOPWORDS = True
LOWERCASE = True
REMOVE_PUNCTUATION = True
REMOVE_HTML = True

# Web Application Configuration
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
FLASK_DEBUG = True

# Database Configuration
DATABASE_PATH = PROJECT_ROOT / "jobcheck.db"
DATABASE_URI = f"sqlite:///{DATABASE_PATH}"

# JWT Configuration
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "your-secret-key-change-in-production")
JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour

# Admin Credentials (Change in production!)
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin123")
