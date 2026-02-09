# Contributing Guidelines

This document outlines the contribution process and development standards for the Fake Job Detection project.

## Project Architecture

The project is organized into four independent modules:

- **Module 1**: `module1_data_preprocessing/` - Data collection and preprocessing
- **Module 2**: `module2_model_training/` - Machine learning model training and evaluation
- **Module 3**: `module3_web_interface/` - Web interface and API implementation
- **Module 4**: `module4_dashboard/` - Administrative dashboard and analytics

## Initial Setup

1. Fork the repository and clone your fork locally
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
  pip install -r requirements.txt
   ```
4. Run the setup script:
   ```bash
   python setup.py
   ```

## Module Responsibilities

### Module 1: Data Preprocessing

**Primary Files**:
- `module1_data_preprocessing/data_loader.py`
- `module1_data_preprocessing/text_preprocessor.py`
- `module1_data_preprocessing/feature_extractor.py`
- `module1_data_preprocessing/main.py`

**Responsibilities**:
- Implement data loading and validation procedures
- Develop text cleaning and normalization algorithms
- Implement TF-IDF feature extraction pipeline
- Create comprehensive test suite for preprocessing operations

### Module 2: Model Training

**Primary Files**:
- `module2_model_training/model_trainer.py`
- `module2_model_training/model_evaluator.py`
- `module2_model_training/main.py`

**Responsibilities**:
- Implement Logistic Regression classifier
- Implement Random Forest classifier
- Develop evaluation metrics framework
- Perform comparative model analysis
- Ensure accuracy threshold ≥ 90%

### Module 3: Web Interface

**Primary Files**:
- `module3_web_interface/app.py`
- `module3_web_interface/prediction_service.py`
- `module3_web_interface/templates/index.html`
- `module3_web_interface/static/css/style.css`
- `module3_web_interface/static/js/main.js`

**Responsibilities**:
- Implement Flask/FastAPI backend architecture
- Design user interface components
- Integrate prediction service
- Implement result visualization with confidence metrics

### Module 4: Dashboard & Administration

**Primary Files**:
- `module4_dashboard/database.py`
- `module4_dashboard/auth.py`
- `module4_dashboard/dashboard.py`
- `module4_dashboard/admin_routes.py`
- `module4_dashboard/templates/admin/*.html`

**Responsibilities**:
- Design database schema and models
- Implement authentication and authorization system
- Develop administrative dashboard interface
- Create data visualization components
- Implement data export functionality

## Version Control Workflow

1. Create a feature branch for your module:
   ```bash
   git checkout -b module1-data-preprocessing
   # or
   git checkout -b module2-model-training
   # etc.
   ```

2. Implement changes and conduct thorough testing

3. Commit changes with descriptive messages:
   ```bash
   git add .
   git commit -m "Module 1: Implement text preprocessing pipeline"
   ```

4. Push to your fork:
   ```bash
   git push origin module1-data-preprocessing
   ```

5. Create a Pull Request containing:
   - Detailed description of implemented changes
   - Module assignment information
   - Known issues or limitations
   - Testing methodology and results

## Code Standards

- Adhere to PEP 8 style guidelines for Python code
- Use descriptive variable and function names
- Include comprehensive docstrings for all functions and classes
- Add inline comments for complex algorithmic logic
- Maintain single responsibility principle for functions

## Testing Requirements

Before submitting code:

1. Execute module-specific test suite
2. Perform integration testing with dependent modules
3. Validate error handling and edge case coverage
4. Verify output format compliance with specifications

## Communication Protocol

- Use GitHub Issues for bug reports and feature requests
- Utilize Pull Request comments for code review discussions
- Update project documentation (README.md) when adding features or modifying setup procedures

## Technical Inquiries

For questions regarding:
- **Module 1**: Data preprocessing and NLP implementation
- **Module 2**: Machine learning model development
- **Module 3**: Web development and API architecture
- **Module 4**: Database design and administrative features

Please open an issue in the GitHub repository or contact the project maintainer.

## Code Review Process

All contributions require review before merging. Reviewers will evaluate:
- Code quality and adherence to standards
- Test coverage and validation
- Documentation completeness
- Integration compatibility

Thank you for contributing to this project.
