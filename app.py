from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_event():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON provided"}), 400
    # Simulating logging the event to a data pipeline
    return jsonify({"status": "success", "logged_event": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
