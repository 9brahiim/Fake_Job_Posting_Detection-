"""
Text preprocessing module.
Handles cleaning, normalization, and preparation of text data.
"""

import re
import string
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))
from config.config import LOWERCASE, REMOVE_PUNCTUATION, REMOVE_HTML, REMOVE_STOPWORDS

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

# Get stopwords
STOPWORDS = set(stopwords.words('english'))


def remove_html_tags(text):
    """
    Remove HTML tags from text.
    
    Args:
        text (str): Input text
    
    Returns:
        str: Text without HTML tags
    """
    if pd.isna(text) or text == '':
        return ''
    
    soup = BeautifulSoup(str(text), 'html.parser')
    return soup.get_text()


def clean_text(text, 
               lowercase=True, 
               remove_punctuation=True, 
               remove_html=True, 
               remove_stopwords=True):
    """
    Clean and normalize text data.
    
    Args:
        text (str): Input text to clean
        lowercase (bool): Convert to lowercase
        remove_punctuation (bool): Remove punctuation
        remove_html (bool): Remove HTML tags
        remove_stopwords (bool): Remove stopwords
    
    Returns:
        str: Cleaned text
    """
    if pd.isna(text) or text == '':
        return ''
    
    text = str(text)
    
    # Remove HTML tags
    if remove_html:
        text = remove_html_tags(text)
    
    # Convert to lowercase
    if lowercase:
        text = text.lower()
    
    # Remove punctuation
    if remove_punctuation:
        text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove stopwords
    if remove_stopwords:
        tokens = word_tokenize(text)
        tokens = [token for token in tokens if token not in STOPWORDS]
        text = ' '.join(tokens)
    
    return text


def preprocess_dataframe(df, text_column='text', **kwargs):
    """
    Preprocess text column in a dataframe.
    
    Args:
        df (pd.DataFrame): Input dataframe
        text_column (str): Name of the text column to preprocess
        **kwargs: Additional arguments passed to clean_text()
    
    Returns:
        pd.DataFrame: Dataframe with cleaned text column
    """
    if text_column not in df.columns:
        print(f"✗ Error: Column '{text_column}' not found in dataframe")
        return df
    
    print(f"\nPreprocessing '{text_column}' column...")
    print(f"  Rows to process: {len(df)}")
    
    # Apply cleaning function
    df[f'{text_column}_cleaned'] = df[text_column].apply(
        lambda x: clean_text(x, **kwargs)
    )
    
    # Remove empty cleaned texts
    initial_count = len(df)
    df = df[df[f'{text_column}_cleaned'].str.len() > 0]
    removed_count = initial_count - len(df)
    
    if removed_count > 0:
        print(f"  Removed {removed_count} rows with empty cleaned text")
    
    print(f"✓ Preprocessing complete: {len(df)} rows remaining")
    print(f"  Average cleaned text length: {df[f'{text_column}_cleaned'].str.len().mean():.0f} characters")
    
    return df


if __name__ == "__main__":
    # Test the preprocessor
    test_text = "<p>This is a TEST job description!!! It has HTML tags and PUNCTUATION.</p>"
    cleaned = clean_text(test_text)
    print(f"Original: {test_text}")
    print(f"Cleaned:  {cleaned}")
