import flask
from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/api/extract-palette', methods=['POST'])
def extract_palette():
    """Extract color palette from image"""
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    file = request.files['image']
    # Placeholder: actual implementation would use OpenCV/scikit-learn
    return jsonify({"palette": []})

@app.route('/api/transform', methods=['POST'])
def transform_palette():
    """Transform palette for accessibility"""
    data = request.json
    # Placeholder: actual implementation would apply transformations
    return jsonify({"transformed": []})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
