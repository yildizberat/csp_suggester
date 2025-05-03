from flask import Flask, jsonify
import json
from pathlib import Path

app = Flask(__name__)
CSP_FILE = Path("csp_suggestions.json")

@app.route("/csp-suggestions", methods=["GET"])
def get_suggestions():
    if not CSP_FILE.exists():
        return jsonify({})
    return jsonify(json.loads(CSP_FILE.read_text()))

if __name__ == "__main__":
    app.run(port=5000, debug=True)