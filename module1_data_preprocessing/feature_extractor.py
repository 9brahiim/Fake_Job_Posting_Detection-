"""
Feature extraction module using TF-IDF vectorization.
Converts cleaned text into numerical feature vectors.
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))
from config.config import (
    TFIDF_VECTORIZER_PATH, 
    MAX_FEATURES, 
    NGRAM_RANGE, 
    MIN_DF, 
    MAX_DF
)


def create_tfidf_vectorizer(max_features=None, ngram_range=None, min_df=None, max_df=None):
    """
    Create and configure TF-IDF vectorizer.
    
    Args:
        max_features (int): Maximum number of features
        ngram_range (tuple): Range of n-grams to use
        min_df (float): Minimum document frequency
        max_df (float): Maximum document frequency
    
    Returns:
        TfidfVectorizer: Configured vectorizer
    """
    if max_features is None:
        max_features = MAX_FEATURES
    if ngram_range is None:
        ngram_range = NGRAM_RANGE
    if min_df is None:
        min_df = MIN_DF
    if max_df is None:
        max_df = MAX_DF
    
    vectorizer = TfidfVectorizer(
        max_features=max_features,
        ngram_range=ngram_range,
        min_df=min_df,
        max_df=max_df,
        stop_words='english'
    )
    
    return vectorizer


def extract_features(df, text_column='text_cleaned', vectorizer=None, fit=True):
    """
    Extract TF-IDF features from text data.
    
    Args:
        df (pd.DataFrame): Dataframe with cleaned text
        text_column (str): Name of the text column
        vectorizer (TfidfVectorizer, optional): Pre-fitted vectorizer
        fit (bool): Whether to fit the vectorizer (True for training, False for prediction)
    
    Returns:
        tuple: (feature_matrix, vectorizer)
    """
    if text_column not in df.columns:
        print(f"✗ Error: Column '{text_column}' not found")
        return None, None
    
    if vectorizer is None:
        vectorizer = create_tfidf_vectorizer()
    
    print(f"\nExtracting TF-IDF features from '{text_column}'...")
    print(f"  Rows: {len(df)}")
    
    if fit:
        print("  Fitting vectorizer on training data...")
        feature_matrix = vectorizer.fit_transform(df[text_column])
        print(f"✓ Vectorizer fitted. Vocabulary size: {len(vectorizer.vocabulary_)}")
    else:
        print("  Transforming using pre-fitted vectorizer...")
        feature_matrix = vectorizer.transform(df[text_column])
        print(f"✓ Features extracted.")
    
    print(f"  Feature matrix shape: {feature_matrix.shape}")
    
    return feature_matrix, vectorizer


def save_vectorizer(vectorizer, file_path=None):
    """
    Save TF-IDF vectorizer to disk.
    
    Args:
        vectorizer (TfidfVectorizer): Vectorizer to save
        file_path (str, optional): Path to save file
    """
    if file_path is None:
        file_path = TFIDF_VECTORIZER_PATH
    
    joblib.dump(vectorizer, file_path)
    print(f"✓ Vectorizer saved to {file_path}")


def load_vectorizer(file_path=None):
    """
    Load TF-IDF vectorizer from disk.
    
    Args:
        file_path (str, optional): Path to vectorizer file
    
    Returns:
        TfidfVectorizer: Loaded vectorizer
    """
    if file_path is None:
        file_path = TFIDF_VECTORIZER_PATH
    
    try:
        vectorizer = joblib.load(file_path)
        print(f"✓ Vectorizer loaded from {file_path}")
        return vectorizer
    except FileNotFoundError:
        print(f"✗ Error: Vectorizer not found at {file_path}")
        return None


if __name__ == "__main__":
    # Test feature extraction
    test_data = pd.DataFrame({
        'text_cleaned': [
            'software engineer python machine learning',
            'data scientist python sql',
            'machine learning engineer python'
        ]
    })
    
    X, vectorizer = extract_features(test_data)
    print(f"\nFeature matrix:\n{X.toarray()}")
    print(f"\nFeature names (first 10): {vectorizer.get_feature_names_out()[:10]}")
