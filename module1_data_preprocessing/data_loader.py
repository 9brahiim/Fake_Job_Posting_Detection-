"""
Data loading and inspection module.
Handles loading the CSV dataset and performing initial data exploration.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))
from config.config import RAW_DATA_PATH, DATA_DIR


def load_dataset(file_path=None):
    """
    Load the Fake Job Postings dataset from CSV.
    
    Args:
        file_path (str, optional): Path to the CSV file. 
                                   Defaults to config.RAW_DATA_PATH
    
    Returns:
        pd.DataFrame: Loaded dataset
    """
    if file_path is None:
        file_path = RAW_DATA_PATH
    
    try:
        df = pd.read_csv(file_path)
        print(f"✓ Dataset loaded successfully: {len(df)} rows, {len(df.columns)} columns")
        return df
    except FileNotFoundError:
        print(f"✗ Error: Dataset not found at {file_path}")
        print(f"  Please download the dataset and place it in {DATA_DIR}/")
        return None
    except Exception as e:
        print(f"✗ Error loading dataset: {e}")
        return None


def inspect_dataset(df):
    """
    Perform basic data inspection and display statistics.
    
    Args:
        df (pd.DataFrame): Dataset to inspect
    """
    if df is None:
        return
    
    print("\n" + "="*50)
    print("DATASET INSPECTION")
    print("="*50)
    
    print(f"\nDataset Shape: {df.shape}")
    print(f"\nColumn Names:")
    for col in df.columns:
        print(f"  - {col}")
    
    print(f"\nMissing Values:")
    missing = df.isnull().sum()
    for col, count in missing.items():
        if count > 0:
            print(f"  - {col}: {count} ({count/len(df)*100:.2f}%)")
    
    print(f"\nData Types:")
    print(df.dtypes)
    
    print(f"\nFirst Few Rows:")
    print(df.head())
    
    if 'fraudulent' in df.columns:
        print(f"\nTarget Distribution:")
        print(df['fraudulent'].value_counts())
        print(f"\nTarget Percentage:")
        print(df['fraudulent'].value_counts(normalize=True) * 100)


def merge_text_columns(df, columns=None):
    """
    Merge important textual fields into a single column.
    
    Args:
        df (pd.DataFrame): Input dataframe
        columns (list, optional): List of column names to merge.
                                 Defaults to ['description', 'requirements', 'benefits']
    
    Returns:
        pd.DataFrame: Dataframe with merged 'text' column
    """
    if columns is None:
        columns = ['description', 'requirements', 'benefits']
    
    # Check which columns exist
    available_columns = [col for col in columns if col in df.columns]
    
    if not available_columns:
        print("✗ Warning: No text columns found to merge")
        return df
    
    print(f"\nMerging columns: {available_columns}")
    
    # Fill NaN values with empty strings and merge
    df['text'] = df[available_columns].fillna('').agg(' '.join, axis=1)
    
    print(f"✓ Text column created with {len(df)} entries")
    print(f"  Average text length: {df['text'].str.len().mean():.0f} characters")
    
    return df


if __name__ == "__main__":
    # Test the data loader
    df = load_dataset()
    if df is not None:
        inspect_dataset(df)
        df = merge_text_columns(df)
        print(f"\n✓ Preprocessing complete. Text column ready for cleaning.")
