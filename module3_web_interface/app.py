"""
Flask web application for fake job detection.
Provides web interface and API endpoints for predictions.
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent.parent))

from prediction_service import PredictionService
from config.config import FLASK_HOST, FLASK_PORT, FLASK_DEBUG

# Module 4 imports
from module4_dashboard.database import init_db, log_prediction, db
from module4_dashboard.auth import init_auth
from module4_dashboard.admin_routes import admin_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'  # Change in production!
CORS(app)

# Initialize database (Module 4)
init_db(app)

# Initialize authentication (Module 4)
init_auth(app)

# Register admin blueprint (Module 4)
app.register_blueprint(admin_bp)

# Initialize prediction service
try:
    prediction_service = PredictionService()
except Exception as e:
    print(f"Warning: Could not initialize prediction service: {e}")
    prediction_service = None


@app.route('/')
def index():
    """Render the home page with prediction form."""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint for making predictions.
    
    Expected JSON payload:
    {
        "job_description": "string",
        "requirements": "string" (optional),
        "benefits": "string" (optional)
    }
    """
    if prediction_service is None:
        return jsonify({
            'error': 'Prediction service not available. Please train models first.'
        }), 503
    
    try:
        # Get data from request
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        job_description = data.get('job_description', '')
        requirements = data.get('requirements', '')
        benefits = data.get('benefits', '')
        
        if not job_description:
            return jsonify({'error': 'Job description is required'}), 400
        
        # Make prediction
        result = prediction_service.predict(job_description, requirements, benefits)
        
        if 'error' in result:
            return jsonify(result), 400
        
        # Log prediction to database (Module 4)
        try:
            ip_address = request.remote_addr
            log_prediction(job_description, requirements, benefits, result, ip_address)
        except Exception as e:
            print(f"Warning: Could not log prediction: {e}")
        
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    status = {
        'status': 'healthy',
        'service_available': prediction_service is not None
    }
    return jsonify(status), 200


if __name__ == '__main__':
    print("="*60)
    print("Starting Fake Job Detection Web Application")
    print("="*60)
    print(f"Server running on http://{FLASK_HOST}:{FLASK_PORT}")
    print(f"Debug mode: {FLASK_DEBUG}")
    print("\nAccess the application at:")
    print(f"  http://localhost:{FLASK_PORT}")
    print("\nAPI Endpoints:")
    print(f"  POST http://localhost:{FLASK_PORT}/predict")
    print(f"  GET  http://localhost:{FLASK_PORT}/health")
    print("="*60)
    
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
