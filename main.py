import os
from flask import Flask, request, jsonify

app = Flask(__name__)

last_cmd = {}

@app.route("/")
def home():
    return "Server is running ✅"

@app.route("/send", methods=["POST"])
def send_cmd():
    global last_cmd
    data = request.json
    last_cmd = data
    print("📥 CMD received:", data)
    return jsonify({"status": "ok", "received": data})

@app.route("/receive", methods=["GET"])
def receive_cmd():
    return jsonify(last_cmd)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
