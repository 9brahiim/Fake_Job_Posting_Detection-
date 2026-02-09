"""
Model training module.
Handles training Logistic Regression and Random Forest classifiers.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import joblib
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))
from config.config import (
    TEST_SIZE,
    RANDOM_STATE,
    LOGISTIC_REGRESSION_MODEL_PATH,
    RANDOM_FOREST_MODEL_PATH
)
from module1_data_preprocessing.feature_extractor import load_vectorizer, extract_features
from module1_data_preprocessing.data_loader import load_dataset
from module1_data_preprocessing.text_preprocessor import preprocess_dataframe, merge_text_columns


def prepare_data():
    """
    Load and prepare data for training.
    
    Returns:
        tuple: (X_train, X_test, y_train, y_test, vectorizer)
    """
    print("Preparing data for training...")
    
    # Load dataset
    df = load_dataset()
    if df is None:
        return None, None, None, None, None
    
    # Merge text columns
    df = merge_text_columns(df)
    
    # Preprocess text
    df = preprocess_dataframe(df, text_column='text')
    
    # Extract features
    X, vectorizer = extract_features(df, text_column='text_cleaned', fit=True)
    
    # Get target variable
    if 'fraudulent' not in df.columns:
        print("✗ Error: 'fraudulent' column not found in dataset")
        return None, None, None, None, None
    
    y = df['fraudulent'].values
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )
    
    print(f"✓ Data prepared:")
    print(f"  Training set: {X_train.shape[0]} samples")
    print(f"  Test set: {X_test.shape[0]} samples")
    
    return X_train, X_test, y_train, y_test, vectorizer


def train_logistic_regression(X_train, y_train, random_state=None):
    """
    Train Logistic Regression model.
    
    Args:
        X_train: Training features
        y_train: Training labels
        random_state: Random state for reproducibility
    
    Returns:
        LogisticRegression: Trained model
    """
    if random_state is None:
        random_state = RANDOM_STATE
    
    print("\nTraining Logistic Regression...")
    model = LogisticRegression(random_state=random_state, max_iter=1000)
    model.fit(X_train, y_train)
    print("✓ Logistic Regression trained successfully")
    
    return model


def train_random_forest(X_train, y_train, n_estimators=100, random_state=None):
    """
    Train Random Forest classifier.
    
    Args:
        X_train: Training features
        y_train: Training labels
        n_estimators: Number of trees
        random_state: Random state for reproducibility
    
    Returns:
        RandomForestClassifier: Trained model
    """
    if random_state is None:
        random_state = RANDOM_STATE
    
    print("\nTraining Random Forest...")
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    print("✓ Random Forest trained successfully")
    
    return model


def save_model(model, file_path, model_name="Model"):
    """
    Save trained model to disk.
    
    Args:
        model: Trained model object
        file_path: Path to save the model
        model_name: Name of the model for logging
    """
    try:
        joblib.dump(model, file_path)
        print(f"✓ {model_name} saved to {file_path}")
    except Exception as e:
        print(f"✗ Error saving {model_name}: {e}")


def load_model(file_path, model_name="Model"):
    """
    Load trained model from disk.
    
    Args:
        file_path: Path to the model file
        model_name: Name of the model for logging
    
    Returns:
        Trained model object or None
    """
    try:
        model = joblib.load(file_path)
        print(f"✓ {model_name} loaded from {file_path}")
        return model
    except FileNotFoundError:
        print(f"✗ Error: {model_name} not found at {file_path}")
        return None
    except Exception as e:
        print(f"✗ Error loading {model_name}: {e}")
        return None


if __name__ == "__main__":
    # Test training pipeline
    X_train, X_test, y_train, y_test, vectorizer = prepare_data()
    
    if X_train is not None:
        # Train models
        lr_model = train_logistic_regression(X_train, y_train)
        rf_model = train_random_forest(X_train, y_train)
        
        # Save models
        save_model(lr_model, LOGISTIC_REGRESSION_MODEL_PATH, "Logistic Regression")
        save_model(rf_model, RANDOM_FOREST_MODEL_PATH, "Random Forest")
