# Contributing Guidelines

Thank you for your interest in contributing to the Fake Job Detection project! This document provides guidelines for collaborating on different modules.

## Project Structure

The project is divided into 4 main modules:

- **Module 1**: `module1_data_preprocessing/` - Data collection and preprocessing
- **Module 2**: `module2_model_training/` - ML model training and evaluation
- **Module 3**: `module3_web_interface/` - Web interface and API
- **Module 4**: `module4_dashboard/` - Admin dashboard and analytics

## Getting Started

1. **Fork the repository** and clone it locally
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run setup script**:
   ```bash
   python setup.py
   ```

## Module Assignment

Each collaborator should work on their assigned module:

### Module 1: Data Preprocessing
**Files to work on:**
- `module1_data_preprocessing/data_loader.py`
- `module1_data_preprocessing/text_preprocessor.py`
- `module1_data_preprocessing/feature_extractor.py`
- `module1_data_preprocessing/main.py`

**Tasks:**
- Implement data loading and inspection
- Complete text cleaning and normalization
- Implement TF-IDF feature extraction
- Test preprocessing pipeline

### Module 2: Model Training
**Files to work on:**
- `module2_model_training/model_trainer.py`
- `module2_model_training/model_evaluator.py`
- `module2_model_training/main.py`

**Tasks:**
- Train Logistic Regression model
- Train Random Forest model
- Implement evaluation metrics
- Compare models and select best one
- Ensure accuracy > 90%

### Module 3: Web Interface
**Files to work on:**
- `module3_web_interface/app.py`
- `module3_web_interface/prediction_service.py`
- `module3_web_interface/templates/index.html`
- `module3_web_interface/static/css/style.css`
- `module3_web_interface/static/js/main.js`

**Tasks:**
- Implement Flask/FastAPI backend
- Create user-friendly web form
- Integrate prediction service
- Display results with confidence scores

### Module 4: Dashboard & Admin
**Files to work on:**
- `module4_dashboard/database.py`
- `module4_dashboard/auth.py`
- `module4_dashboard/dashboard.py`
- `module4_dashboard/admin_routes.py`
- `module4_dashboard/templates/admin/*.html`

**Tasks:**
- Implement database models
- Create authentication system
- Build admin dashboard
- Add visualizations (charts)
- Implement export functionality

## Git Workflow

1. **Create a branch** for your module:
   ```bash
   git checkout -b module1-data-preprocessing
   # or
   git checkout -b module2-model-training
   # etc.
   ```

2. **Make your changes** and test thoroughly

3. **Commit your changes** with clear messages:
   ```bash
   git add .
   git commit -m "Module 1: Implement text preprocessing pipeline"
   ```

4. **Push to your fork**:
   ```bash
   git push origin module1-data-preprocessing
   ```

5. **Create a Pull Request** with:
   - Clear description of changes
   - Which module you worked on
   - Any issues or questions

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Comment complex logic
- Keep functions focused and small

## Testing

Before submitting your code:

1. **Test your module independently**
2. **Test integration** with other modules if applicable
3. **Check for errors** and handle edge cases
4. **Verify output** matches expected format

## Communication

- Use GitHub Issues for bugs and feature requests
- Use Pull Request comments for code review discussions
- Update README.md if you add new features or change setup

## Questions?

If you have questions about:
- **Module 1**: Data preprocessing and NLP
- **Module 2**: Machine learning models
- **Module 3**: Web development and APIs
- **Module 4**: Database and admin features

Feel free to open an issue or contact the project maintainer.

## Thank You!

Your contributions make this project better. Happy coding! 🚀
