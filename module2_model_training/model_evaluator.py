"""
Model evaluation module.
Evaluates models using accuracy, precision, recall, and F1-score.
"""

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)
import pandas as pd


def evaluate_model(model, X_test, y_test, model_name="Model"):
    """
    Evaluate a trained model on test data.
    
    Args:
        model: Trained model
        X_test: Test features
        y_test: Test labels
        model_name: Name of the model for display
    
    Returns:
        dict: Dictionary containing evaluation metrics
    """
    print(f"\n{'='*50}")
    print(f"Evaluating {model_name}")
    print(f"{'='*50}")
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
    
    # Display metrics
    print(f"\nMetrics:")
    print(f"  Accuracy:  {accuracy:.4f} ({accuracy*100:.2f}%)")
    print(f"  Precision: {precision:.4f}")
    print(f"  Recall:    {recall:.4f}")
    print(f"  F1-Score:  {f1:.4f}")
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print(f"\nConfusion Matrix:")
    print(f"  True Negatives:  {cm[0][0]}")
    print(f"  False Positives: {cm[0][1]}")
    print(f"  False Negatives: {cm[1][0]}")
    print(f"  True Positives:  {cm[1][1]}")
    
    # Classification report
    print(f"\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Real', 'Fake']))
    
    # Return metrics dictionary
    metrics = {
        'model_name': model_name,
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'confusion_matrix': cm
    }
    
    return metrics


def compare_models(metrics_list):
    """
    Compare multiple models and display comparison table.
    
    Args:
        metrics_list: List of metrics dictionaries from evaluate_model()
    
    Returns:
        pd.DataFrame: Comparison dataframe
    """
    print(f"\n{'='*60}")
    print("MODEL COMPARISON")
    print(f"{'='*60}")
    
    # Create comparison dataframe
    comparison_data = []
    for metrics in metrics_list:
        comparison_data.append({
            'Model': metrics['model_name'],
            'Accuracy': f"{metrics['accuracy']:.4f}",
            'Precision': f"{metrics['precision']:.4f}",
            'Recall': f"{metrics['recall']:.4f}",
            'F1-Score': f"{metrics['f1_score']:.4f}"
        })
    
    df_comparison = pd.DataFrame(comparison_data)
    print("\n" + df_comparison.to_string(index=False))
    
    # Find best model
    best_model_idx = max(range(len(metrics_list)), 
                         key=lambda i: metrics_list[i]['f1_score'])
    best_model = metrics_list[best_model_idx]
    
    print(f"\n✓ Best Model: {best_model['model_name']}")
    print(f"  F1-Score: {best_model['f1_score']:.4f}")
    print(f"  Accuracy: {best_model['accuracy']:.4f}")
    
    return df_comparison, best_model


if __name__ == "__main__":
    # Example usage
    print("Model Evaluator Module")
    print("Import this module in main.py to evaluate trained models")
