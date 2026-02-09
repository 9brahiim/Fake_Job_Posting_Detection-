# Module 4: Dashboard & Admin Panel

## Overview
This module provides an admin dashboard for monitoring predictions, analyzing data, and managing the system.

## Files
- `database.py`: Database models and setup
- `auth.py`: Authentication and authorization
- `dashboard.py`: Dashboard routes and analytics
- `admin_routes.py`: Admin panel routes
- `templates/admin/`: Admin dashboard HTML templates
- `static/admin/`: Admin panel CSS and JavaScript

## Features
- Secure admin login (JWT authentication)
- Prediction analytics and visualization
- Real vs Fake job distribution charts
- Daily prediction trends
- Export functionality (CSV/PDF)
- Model retraining capabilities
- Prediction logs database

## Usage

```bash
# Run admin dashboard (integrated with Module 3)
python module3_web_interface/app.py

# Access admin panel at:
# http://localhost:5000/admin
```

## Database
Uses SQLite by default. Can be configured to use MySQL/PostgreSQL in `config/config.py`.
