"""
Main script for Module 2: Fake Job Classification Model
Trains, evaluates, and compares ML models.
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from model_trainer import (
    prepare_data,
    train_logistic_regression,
    train_random_forest,
    save_model
)
from model_evaluator import evaluate_model, compare_models
from config.config import (
    LOGISTIC_REGRESSION_MODEL_PATH,
    RANDOM_FOREST_MODEL_PATH,
    BEST_MODEL_PATH,
    TARGET_ACCURACY
)


def main():
    """
    Main training and evaluation pipeline.
    """
    print("="*60)
    print("MODULE 2: FAKE JOB CLASSIFICATION MODEL")
    print("="*60)
    
    # Step 1: Prepare data
    print("\n[Step 1/5] Preparing data...")
    X_train, X_test, y_train, y_test, vectorizer = prepare_data()
    
    if X_train is None:
        print("✗ Failed to prepare data. Exiting.")
        return
    
    # Step 2: Train Logistic Regression
    print("\n[Step 2/5] Training Logistic Regression...")
    lr_model = train_logistic_regression(X_train, y_train)
    save_model(lr_model, LOGISTIC_REGRESSION_MODEL_PATH, "Logistic Regression")
    
    # Step 3: Train Random Forest
    print("\n[Step 3/5] Training Random Forest...")
    rf_model = train_random_forest(X_train, y_train)
    save_model(rf_model, RANDOM_FOREST_MODEL_PATH, "Random Forest")
    
    # Step 4: Evaluate models
    print("\n[Step 4/5] Evaluating models...")
    lr_metrics = evaluate_model(lr_model, X_test, y_test, "Logistic Regression")
    rf_metrics = evaluate_model(rf_model, X_test, y_test, "Random Forest")
    
    # Step 5: Compare and select best model
    print("\n[Step 5/5] Comparing models...")
    comparison_df, best_model = compare_models([lr_metrics, rf_metrics])
    
    # Save best model
    if best_model['model_name'] == 'Logistic Regression':
        best_model_obj = lr_model
    else:
        best_model_obj = rf_model
    
    save_model(best_model_obj, BEST_MODEL_PATH, "Best Model")
    
    # Check if target accuracy achieved
    print("\n" + "="*60)
    print("TRAINING COMPLETE!")
    print("="*60)
    
    if best_model['accuracy'] >= TARGET_ACCURACY:
        print(f"✓ Target accuracy ({TARGET_ACCURACY*100}%) achieved!")
    else:
        print(f"⚠ Target accuracy ({TARGET_ACCURACY*100}%) not reached.")
        print(f"  Current best: {best_model['accuracy']*100:.2f}%")
    
    print(f"\nBest Model: {best_model['model_name']}")
    print(f"  Accuracy: {best_model['accuracy']*100:.2f}%")
    print(f"  F1-Score: {best_model['f1_score']:.4f}")
    print(f"\nModel saved to: {BEST_MODEL_PATH}")
    print("\nReady for Module 3: Web Interface & Prediction API")


if __name__ == "__main__":
    main()
