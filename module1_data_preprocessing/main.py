"""
Main script for Module 1: Data Collection & Preprocessing
Runs the complete preprocessing pipeline.
"""

import pandas as pd
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from data_loader import load_dataset, inspect_dataset, merge_text_columns
from text_preprocessor import preprocess_dataframe
from feature_extractor import extract_features, save_vectorizer
from config.config import PROCESSED_DATA_PATH, DATA_DIR


def main():
    """
    Main preprocessing pipeline.
    """
    print("="*60)
    print("MODULE 1: DATA COLLECTION & PREPROCESSING")
    print("="*60)
    
    # Step 1: Load dataset
    print("\n[Step 1/4] Loading dataset...")
    df = load_dataset()
    if df is None:
        return
    
    # Step 2: Inspect dataset
    print("\n[Step 2/4] Inspecting dataset...")
    inspect_dataset(df)
    
    # Step 3: Merge text columns
    print("\n[Step 3/4] Merging text columns...")
    df = merge_text_columns(df)
    
    # Step 4: Clean and preprocess text
    print("\n[Step 4/5] Cleaning and preprocessing text...")
    df = preprocess_dataframe(df, text_column='text')
    
    # Step 5: Extract features (optional - can be done in Module 2)
    print("\n[Step 5/5] Extracting TF-IDF features...")
    X, vectorizer = extract_features(df, text_column='text_cleaned', fit=True)
    
    # Save vectorizer
    save_vectorizer(vectorizer)
    
    # Save processed dataframe
    print(f"\nSaving processed data to {PROCESSED_DATA_PATH}...")
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"✓ Processed data saved successfully")
    
    print("\n" + "="*60)
    print("PREPROCESSING COMPLETE!")
    print("="*60)
    print(f"\nOutput files:")
    print(f"  - Processed data: {PROCESSED_DATA_PATH}")
    print(f"  - TF-IDF vectorizer: {vectorizer}")
    print(f"\nReady for Module 2: Model Training")


if __name__ == "__main__":
    main()
