from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/analyze", methods=["POST", "OPTIONS"])
def analyze():
    if request.method == "OPTIONS":
        return jsonify({}), 200

    try:
        from bias_engine import analyze_bias
        data = request.json
        article = data.get("article", "")

        if not article:
            return jsonify({"error": "No article provided"}), 400

        result = analyze_bias(article)
        return jsonify(result)

    except Exception as e:
        # Print the FULL error in terminal
        print("FULL ERROR:")
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)