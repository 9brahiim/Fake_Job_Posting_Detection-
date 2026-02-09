"""
Prediction service module.
Handles preprocessing and prediction using the trained model.
"""

import pandas as pd
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from module1_data_preprocessing.text_preprocessor import clean_text
from module1_data_preprocessing.feature_extractor import load_vectorizer
from module2_model_training.model_trainer import load_model
from config.config import BEST_MODEL_PATH, TFIDF_VECTORIZER_PATH


class PredictionService:
    """
    Service class for making predictions on job postings.
    """
    
    def __init__(self):
        """Initialize the prediction service by loading model and vectorizer."""
        self.model = None
        self.vectorizer = None
        self._load_artifacts()
    
    def _load_artifacts(self):
        """Load the trained model and vectorizer."""
        print("Loading model and vectorizer...")
        self.model = load_model(BEST_MODEL_PATH, "Best Model")
        self.vectorizer = load_vectorizer(TFIDF_VECTORIZER_PATH)
        
        if self.model is None or self.vectorizer is None:
            raise FileNotFoundError(
                "Model or vectorizer not found. Please train models first using Module 2."
            )
        print("✓ Model and vectorizer loaded successfully")
    
    def preprocess_text(self, text):
        """
        Preprocess input text (same as training phase).
        
        Args:
            text (str): Raw job description text
        
        Returns:
            str: Cleaned text
        """
        cleaned = clean_text(
            text,
            lowercase=True,
            remove_punctuation=True,
            remove_html=True,
            remove_stopwords=True
        )
        return cleaned
    
    def predict(self, job_description, requirements="", benefits=""):
        """
        Predict if a job posting is fake or real.
        
        Args:
            job_description (str): Job description text
            requirements (str): Job requirements text
            benefits (str): Job benefits text
        
        Returns:
            dict: Prediction result with label and confidence
        """
        if self.model is None or self.vectorizer is None:
            return {
                'error': 'Model not loaded. Please ensure models are trained.'
            }
        
        # Merge text fields (same as training)
        combined_text = f"{job_description} {requirements} {benefits}".strip()
        
        if not combined_text:
            return {
                'error': 'No text provided for prediction.'
            }
        
        # Preprocess text
        cleaned_text = self.preprocess_text(combined_text)
        
        if not cleaned_text:
            return {
                'error': 'Text is empty after preprocessing.'
            }
        
        # Convert to dataframe format (for consistency)
        df = pd.DataFrame({'text_cleaned': [cleaned_text]})
        
        # Extract features
        try:
            X = self.vectorizer.transform(df['text_cleaned'])
        except Exception as e:
            return {
                'error': f'Error during feature extraction: {str(e)}'
            }
        
        # Make prediction
        try:
            prediction = self.model.predict(X)[0]
            probabilities = self.model.predict_proba(X)[0]
            
            # Get confidence score
            confidence = max(probabilities) * 100
            
            # Map prediction to label
            label = "Fake" if prediction == 1 else "Real"
            
            return {
                'prediction': int(prediction),
                'label': label,
                'confidence': round(confidence, 2),
                'probabilities': {
                    'real': round(probabilities[0] * 100, 2),
                    'fake': round(probabilities[1] * 100, 2)
                }
            }
        except Exception as e:
            return {
                'error': f'Error during prediction: {str(e)}'
            }


# Global instance
prediction_service = PredictionService()
