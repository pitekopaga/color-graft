from flask import Flask, request, jsonify
from color_engine import cvd_transform, CVDType
from diagnostic import diagnose_user, TEST_PLATES

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend is running"

@app.route('/api/diagnostic/plates', methods=['GET'])
def get_test_plates():
    """Return the test plates for frontend to display"""
    return jsonify(TEST_PLATES)

@app.route('/api/diagnostic/result', methods=['POST'])
def submit_diagnosis():
    """Receive user responses and return diagnosis"""
    data = request.json
    responses = data.get('responses', [])
    cvd_type, severity = diagnose_user(responses)
    return jsonify({
        "cvd_type": cvd_type,
        "severity": severity,
        "confidence": 0.8
    })

@app.route('/api/transform/palette', methods=['POST'])
def transform_palette_endpoint():
    """Apply CVD transformation to a palette"""
    data = request.json
    palette = data.get('palette', [])
    cvd_type = CVDType(data.get('cvd_type', 'deutan'))
    severity = data.get('severity', 0.7)
    
    transformed = [cvd_transform(color, cvd_type, severity) for color in palette]
    return jsonify({"transformed_palette": transformed})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
