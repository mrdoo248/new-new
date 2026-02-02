import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# حفظ آخر أمر
last_cmd = {}

@app.route("/", methods=["GET"])
def home():
    return "Server is running ✅"

@app.route("/send", methods=["POST"])
def send_cmd():
    global last_cmd
    data = request.get_json(force=True)  # استخدام force=True لتفادي مشاكل Content-Type
    last_cmd = data
    print("📥 CMD received:", data)
    return jsonify({"status": "ok", "received": data})

@app.route("/receive", methods=["GET"])
def receive_cmd():
    return jsonify(last_cmd)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))  # Replit يعطي PORT تلقائي
    # debug=True مفيد للتجربة
    app.run(host="0.0.0.0", port=port, debug=True)
