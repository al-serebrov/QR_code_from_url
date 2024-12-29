from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.json
    long_url = data.get("url")

    if not long_url:
        return jsonify({"error": "URL is required"}), 400

    isgd_api = f"https://is.gd/create.php?format=simple&url={long_url}"

    try:
        response = requests.get(isgd_api)
        if response.status_code != 200:
            return jsonify({"error": "Failed to shorten URL"}), response.status_code

        shortened_url = response.text
        return jsonify({"shortened_url": shortened_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
