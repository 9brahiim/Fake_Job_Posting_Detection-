# Module 4: Administrative Dashboard & Analytics

## Overview

This module provides an administrative dashboard for system monitoring, prediction analytics, and administrative management functions.

## Components

- `database.py`: Database schema and model definitions
- `auth.py`: Authentication and authorization implementation
- `dashboard.py`: Analytics and visualization functions
- `admin_routes.py`: Administrative route handlers
- `templates/admin/`: Administrative dashboard HTML templates
- `static/admin/`: Administrative panel CSS and JavaScript assets

## Features

- Secure administrative authentication using JWT (JSON Web Tokens)
- Prediction analytics and statistical visualization
- Real vs Fake job posting distribution analysis
- Daily prediction trend monitoring
- Data export functionality (CSV, PDF formats)
- Model retraining interface
- Prediction logging and audit trail database

## Execution

```bash
# Administrative dashboard (integrated with Module 3)
python module3_web_interface/app.py

# Access administrative panel at:
# http://localhost:5000/admin
```

## Database Configuration

Default database: SQLite. Database configuration can be modified in `config/config.py` to support MySQL or PostgreSQL.
