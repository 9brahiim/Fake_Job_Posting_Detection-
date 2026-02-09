"""
Authentication module for admin panel.
Handles JWT-based authentication.
"""

from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from functools import wraps
from flask import jsonify, session, redirect, url_for
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from module4_dashboard.database import AdminUser, db
from config.config import JWT_SECRET_KEY


def init_auth(app):
    """
    Initialize JWT authentication with Flask app.
    
    Args:
        app: Flask application instance
    """
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 1 hour
    
    jwt = JWTManager(app)
    return jwt


def authenticate(username, password):
    """
    Authenticate admin user.
    
    Args:
        username: Admin username
        password: Admin password
    
    Returns:
        tuple: (success: bool, token: str or None)
    """
    try:
        admin = AdminUser.query.filter_by(username=username).first()
        
        if admin and check_password_hash(admin.password_hash, password):
            # Update last login
            from datetime import datetime
            admin.last_login = datetime.utcnow()
            db.session.commit()
            
            # Create access token
            access_token = create_access_token(identity=username)
            return True, access_token
        
        return False, None
    except Exception as e:
        print(f"Authentication error: {e}")
        return False, None


def admin_required(f):
    """
    Decorator to require admin authentication.
    """
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        current_user = get_jwt_identity()
        admin = AdminUser.query.filter_by(username=current_user).first()
        
        if not admin:
            return jsonify({'error': 'Admin access required'}), 403
        
        return f(*args, **kwargs)
    
    return decorated_function


def admin_required_web(f):
    """
    Decorator for web routes requiring admin authentication.
    Uses session-based auth for web interface.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session or not session['admin_logged_in']:
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    
    return decorated_function
