# Module 1: Data Collection & Preprocessing

## Overview
This module handles loading, cleaning, and preprocessing the Fake Job Postings dataset for machine learning.

## Files
- `data_loader.py`: Load and inspect the dataset
- `text_preprocessor.py`: Clean and normalize text data
- `feature_extractor.py`: Extract features using TF-IDF
- `main.py`: Main script to run the preprocessing pipeline

## Usage

```bash
python module1_data_preprocessing/main.py
```

## Output
- Cleaned dataset saved to `data/processed_data.csv`
- TF-IDF vectorizer saved to `models/tfidf_vectorizer.pkl`
