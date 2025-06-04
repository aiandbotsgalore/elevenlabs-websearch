from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

SERP_API_KEY = os.environ.get("SERP_API_KEY", "10e37cfdd86e2021eff92fee73efba2937ebf20bd8a99098ecbcb577b948de25")
SEARCH_ENDPOINT = "https://serpapi.com/search.json"

@app.route("/websearch", methods=["POST"])
def websearch():
    data = request.get_json()
    query = data.get("query", "")

    if not query:
        return jsonify({"error": "Missing 'query' parameter"}), 400

    params = {
        "q": query,
        "api_key": SERP_API_KEY,
        "engine": "google"
    }

    response = requests.get(SEARCH_ENDPOINT, params=params)
    results = []

    if response.status_code == 200:
        data = response.json()
        organic_results = data.get("organic_results", [])
        for result in organic_results[:3]:
            results.append({
                "title": result.get("title"),
                "url": result.get("link"),
                "snippet": result.get("snippet")
            })

    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
