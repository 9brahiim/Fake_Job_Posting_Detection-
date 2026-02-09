# Module 3: Web Interface & Prediction API

## Overview
This module provides a web interface and API for real-time fake job detection.

## Files
- `app.py`: Flask/FastAPI application
- `prediction_service.py`: Service for making predictions
- `templates/`: HTML templates for the web interface
- `static/`: CSS, JavaScript, and static assets

## Usage

```bash
# Run Flask app
python module3_web_interface/app.py

# Or with FastAPI
uvicorn module3_web_interface.app:app --reload
```

## API Endpoints
- `GET /`: Home page with prediction form
- `POST /predict`: Prediction API endpoint
- `GET /health`: Health check endpoint

## Features
- User-friendly web form for job description input
- Real-time prediction with confidence scores
- Preprocessing pipeline matching training phase
