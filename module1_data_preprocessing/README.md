# Module 1: Data Collection & Preprocessing

## Overview

This module implements the data ingestion and preprocessing pipeline for the Fake Job Postings dataset, preparing raw text data for machine learning model training.

## Components

- `data_loader.py`: Dataset loading and validation procedures
- `text_preprocessor.py`: Text cleaning and normalization algorithms
- `feature_extractor.py`: TF-IDF feature extraction implementation
- `main.py`: Main preprocessing pipeline execution script

## Execution

```bash
python module1_data_preprocessing/main.py
```

## Output Artifacts

- Processed dataset: `data/processed_data.csv`
- TF-IDF vectorizer: `models/tfidf_vectorizer.pkl`
