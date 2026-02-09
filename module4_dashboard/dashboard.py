"""
Dashboard analytics and visualization module.
"""

from datetime import datetime, timedelta
from sqlalchemy import func
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from module4_dashboard.database import PredictionLog, db


def get_daily_predictions(days=30):
    """
    Get daily prediction counts for the last N days.
    
    Args:
        days: Number of days to retrieve
    
    Returns:
        list: List of dictionaries with date and counts
    """
    try:
        start_date = datetime.utcnow() - timedelta(days=days)
        
        # Query daily predictions
        daily_stats = db.session.query(
            func.date(PredictionLog.timestamp).label('date'),
            func.count(PredictionLog.id).label('total'),
            func.sum(func.cast(PredictionLog.prediction == 0, db.Integer)).label('real'),
            func.sum(func.cast(PredictionLog.prediction == 1, db.Integer)).label('fake')
        ).filter(
            PredictionLog.timestamp >= start_date
        ).group_by(
            func.date(PredictionLog.timestamp)
        ).order_by(
            func.date(PredictionLog.timestamp)
        ).all()
        
        # Format results
        result = []
        for stat in daily_stats:
            result.append({
                'date': stat.date.isoformat() if isinstance(stat.date, datetime) else str(stat.date),
                'total': stat.total,
                'real': stat.real or 0,
                'fake': stat.fake or 0
            })
        
        return result
    except Exception as e:
        print(f"Error getting daily predictions: {e}")
        return []


def get_recent_predictions(limit=10):
    """
    Get recent predictions.
    
    Args:
        limit: Number of recent predictions to retrieve
    
    Returns:
        list: List of prediction dictionaries
    """
    try:
        predictions = PredictionLog.query.order_by(
            PredictionLog.timestamp.desc()
        ).limit(limit).all()
        
        return [pred.to_dict() for pred in predictions]
    except Exception as e:
        print(f"Error getting recent predictions: {e}")
        return []


def get_prediction_trends():
    """
    Get prediction trends for visualization.
    
    Returns:
        dict: Dictionary with chart data
    """
    stats = get_daily_predictions(days=30)
    
    dates = [item['date'] for item in stats]
    real_counts = [item['real'] for item in stats]
    fake_counts = [item['fake'] for item in stats]
    total_counts = [item['total'] for item in stats]
    
    return {
        'dates': dates,
        'real': real_counts,
        'fake': fake_counts,
        'total': total_counts
    }
