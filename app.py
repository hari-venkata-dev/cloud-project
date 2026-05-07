from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Cloud App Running!"

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/metrics")
def metrics():
    return jsonify({
        "service": "cloud-app",
        "status": "running",
        "version": "1.0",
        "environment": "local"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)