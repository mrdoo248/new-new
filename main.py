from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Server is running ✅"

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True)
    return jsonify({
        "received": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
