# Module 3: Web Interface & Prediction API

## Overview

This module provides a RESTful API and web-based user interface for real-time fake job posting detection and classification.

## Components

- `app.py`: Flask/FastAPI application server
- `prediction_service.py`: Prediction service implementation
- `templates/`: HTML template files for web interface
- `static/`: CSS stylesheets, JavaScript files, and static assets

## Execution

```bash
# Flask application
python module3_web_interface/app.py

# FastAPI alternative (if implemented)
uvicorn module3_web_interface.app:app --reload
```

## API Endpoints

- `GET /`: Web interface home page with prediction form
- `POST /predict`: Prediction API endpoint
- `GET /health`: Application health check endpoint

## Features

- Web-based job description input form
- Real-time prediction with confidence score calculation
- Preprocessing pipeline consistency with training phase
