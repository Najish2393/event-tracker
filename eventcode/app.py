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
    try:
        data = request.get_json()
        if not data or 'event' not in data:
            return jsonify({"error": "Missing 'event' field in JSON payload"}), 400

        event_name = data['event']
        event_counts[event_name] = event_counts.get(event_name, 0) + 1
        print(f"Event '{event_name}' tracked. Current count: {event_counts[event_name]}")
        return jsonify({"message": f"Event '{event_name}' tracked successfully"}), 200

    except Exception as e:
        print(f"Error tracking event: {e}")
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

@app.route('/events', methods=['GET'])
def get_event_counts():
    return jsonify(event_counts), 200

@app.route('/reset', methods=['DELETE'])
def reset_events():
    global event_counts
    event_counts = {}
    print("All event counts have been reset.")
    return jsonify({"message": "All event counts reset successfully"}), 200
#portmapping
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000)) # Changed default to 8000 for consistency
    app.run(debug=True, host='0.0.0.0', port=port)
