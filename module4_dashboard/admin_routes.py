"""
Admin panel routes and views.
"""

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from werkzeug.security import check_password_hash
import csv
import io
from datetime import datetime
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from module4_dashboard.database import (
    db, PredictionLog, AdminUser, 
    get_prediction_stats, log_prediction
)
from module4_dashboard.dashboard import (
    get_daily_predictions, 
    get_recent_predictions,
    get_prediction_trends
)
from module4_dashboard.auth import authenticate, admin_required_web

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        success, token = authenticate(username, password)
        
        if success:
            session['admin_logged_in'] = True
            session['admin_username'] = username
            return redirect(url_for('admin.dashboard'))
        else:
            return render_template('admin/login.html', error='Invalid credentials')
    
    return render_template('admin/login.html')


@admin_bp.route('/logout')
def admin_logout():
    """Admin logout."""
    session.pop('admin_logged_in', None)
    session.pop('admin_username', None)
    return redirect(url_for('admin.admin_login'))


@admin_bp.route('/dashboard')
@admin_required_web
def dashboard():
    """Admin dashboard."""
    stats = get_prediction_stats()
    recent_predictions = get_recent_predictions(limit=10)
    trends = get_prediction_trends()
    
    return render_template(
        'admin/dashboard.html',
        stats=stats,
        recent_predictions=recent_predictions,
        trends=trends
    )


@admin_bp.route('/api/stats')
@admin_required_web
def api_stats():
    """API endpoint for prediction statistics."""
    stats = get_prediction_stats()
    return jsonify(stats)


@admin_bp.route('/api/predictions')
@admin_required_web
def api_predictions():
    """API endpoint for recent predictions."""
    limit = request.args.get('limit', 10, type=int)
    predictions = get_recent_predictions(limit=limit)
    return jsonify(predictions)


@admin_bp.route('/api/trends')
@admin_required_web
def api_trends():
    """API endpoint for prediction trends."""
    trends = get_prediction_trends()
    return jsonify(trends)


@admin_bp.route('/export/csv')
@admin_required_web
def export_csv():
    """Export predictions to CSV."""
    try:
        predictions = PredictionLog.query.order_by(PredictionLog.timestamp.desc()).all()
        
        output = io.StringIO()
        writer = csv.writer(output)
        
        # Write header
        writer.writerow([
            'ID', 'Prediction', 'Confidence', 'Real Probability', 
            'Fake Probability', 'Timestamp', 'IP Address'
        ])
        
        # Write data
        for pred in predictions:
            writer.writerow([
                pred.id,
                'Fake' if pred.prediction == 1 else 'Real',
                pred.confidence,
                pred.probability_real,
                pred.probability_fake,
                pred.timestamp.isoformat(),
                pred.ip_address or ''
            ])
        
        output.seek(0)
        
        from flask import Response
        return Response(
            output.getvalue(),
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=predictions.csv'}
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/retrain', methods=['POST'])
@admin_required_web
def retrain_model():
    """Trigger model retraining."""
    # This would call Module 2's training pipeline
    # For now, return a placeholder response
    return jsonify({
        'message': 'Model retraining initiated',
        'status': 'pending'
    }), 202
