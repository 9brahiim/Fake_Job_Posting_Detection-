"""
Database models and setup for prediction logging and admin features.
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from config.config import DATABASE_URI

db = SQLAlchemy()


class PredictionLog(db.Model):
    """
    Model for storing prediction logs.
    """
    __tablename__ = 'prediction_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    job_description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text)
    benefits = db.Column(db.Text)
    prediction = db.Column(db.Integer, nullable=False)  # 0 = Real, 1 = Fake
    confidence = db.Column(db.Float, nullable=False)
    probability_real = db.Column(db.Float, nullable=False)
    probability_fake = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    ip_address = db.Column(db.String(45))
    
    def to_dict(self):
        """Convert prediction log to dictionary."""
        return {
            'id': self.id,
            'prediction': 'Fake' if self.prediction == 1 else 'Real',
            'confidence': self.confidence,
            'timestamp': self.timestamp.isoformat(),
            'probability_real': self.probability_real,
            'probability_fake': self.probability_fake
        }


class AdminUser(db.Model):
    """
    Model for admin users.
    """
    __tablename__ = 'admin_users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    def to_dict(self):
        """Convert admin user to dictionary."""
        return {
            'id': self.id,
            'username': self.username,
            'created_at': self.created_at.isoformat(),
            'last_login': self.last_login.isoformat() if self.last_login else None
        }


def init_db(app):
    """
    Initialize database with Flask app.
    
    Args:
        app: Flask application instance
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        print("✓ Database initialized")
        
        # Create default admin user if it doesn't exist
        from config.config import ADMIN_USERNAME, ADMIN_PASSWORD
        from werkzeug.security import generate_password_hash
        
        admin = AdminUser.query.filter_by(username=ADMIN_USERNAME).first()
        if not admin:
            admin = AdminUser(
                username=ADMIN_USERNAME,
                password_hash=generate_password_hash(ADMIN_PASSWORD)
            )
            db.session.add(admin)
            db.session.commit()
            print(f"✓ Default admin user created: {ADMIN_USERNAME}")


def log_prediction(job_description, requirements, benefits, prediction_result, ip_address=None):
    """
    Log a prediction to the database.
    
    Args:
        job_description: Job description text
        requirements: Requirements text
        benefits: Benefits text
        prediction_result: Dictionary with prediction results
        ip_address: IP address of the requester
    """
    try:
        log = PredictionLog(
            job_description=job_description[:1000],  # Limit length
            requirements=requirements[:500] if requirements else None,
            benefits=benefits[:500] if benefits else None,
            prediction=prediction_result['prediction'],
            confidence=prediction_result['confidence'],
            probability_real=prediction_result['probabilities']['real'],
            probability_fake=prediction_result['probabilities']['fake'],
            ip_address=ip_address
        )
        db.session.add(log)
        db.session.commit()
        return log
    except Exception as e:
        print(f"Error logging prediction: {e}")
        db.session.rollback()
        return None


def get_prediction_stats():
    """
    Get statistics about predictions.
    
    Returns:
        dict: Statistics dictionary
    """
    try:
        total = PredictionLog.query.count()
        fake_count = PredictionLog.query.filter_by(prediction=1).count()
        real_count = PredictionLog.query.filter_by(prediction=0).count()
        
        return {
            'total_predictions': total,
            'fake_count': fake_count,
            'real_count': real_count,
            'fake_percentage': (fake_count / total * 100) if total > 0 else 0,
            'real_percentage': (real_count / total * 100) if total > 0 else 0
        }
    except Exception as e:
        print(f"Error getting prediction stats: {e}")
        return {
            'total_predictions': 0,
            'fake_count': 0,
            'real_count': 0,
            'fake_percentage': 0,
            'real_percentage': 0
        }
