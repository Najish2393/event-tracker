import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

event_counts = {}

@app.route('/')
def home():
    return "Event Tracking Service is running!"

@app.route('/event', methods=['POST'])
def track_event():
    data = request.get_json()
    event_name = data['event']
    event_counts[event_name] = event_counts.get(event_name, 0) + 1
    return jsonify({"message": f"Event '{event_name}' tracked successfully"}), 200

@app.route('/events', methods=['GET'])
def get_event_counts():
    return jsonify(event_counts), 200

@app.route('/reset', methods=['DELETE'])
def reset_events():
    event_counts.clear()
    return jsonify({"message": "All event counts reset successfully"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)
