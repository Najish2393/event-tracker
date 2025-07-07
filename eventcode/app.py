#Code for event tracking
from flask import Flask, request, jsonify

app = Flask(__name__)
events = {}

@app.route("/event", methods=["POST"])
def add_event():
    data = request.get_json()
    event_name = data.get("event")
    if not event_name:
        return jsonify({"error": "Missing event name"}), 400
    events[event_name] = events.get(event_name, 0) + 1
    return jsonify({"message": "Event added"}), 201

@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events)

@app.route("/reset", methods=["DELETE"])
def reset_events():
    events.clear()
    return jsonify({"message": "Events reset"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

