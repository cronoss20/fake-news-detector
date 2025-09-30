import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import requests

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

def heuristic_analysis(text):
    # Simple keyword-based fake news heuristic
    red_flags = []
    keywords = [
        "breaking", "shocking", "unbelievable", "miracle", "banned", "censored",
        "you won't believe", "click here", "exclusive", "conspiracy", "scandal"
    ]
    for keyword in keywords:
        if keyword.lower() in text.lower():
            red_flags.append(keyword)
    confidence = 40 + 5*len(red_flags)
    confidence = min(confidence, 85)
    return {
        "is_fake": len(red_flags) > 0,
        "confidence": confidence,
        "red_flags": red_flags,
        "reasoning": "Heuristic analysis based on suspicious keywords."
    }

def gpt_analysis(text):
    import openai
    openai.api_key = OPENAI_API_KEY
    prompt = (
        "Given the following news content, determine if it's likely to be fake news. "
        "List any suspicious aspects, provide a confidence percentage (0-100), and explain your reasoning. "
        "News content:\n"
        f"{text}\n"
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.1,
        messages=[
            {"role": "system", "content": "You are a fake news detector assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    answer = response.choices[0].message.content
    # Try to extract confidence and red flags
    import re
    confidence = 60
    red_flags = []
    for line in answer.splitlines():
        if "confidence" in line.lower():
            match = re.search(r"(\d{1,3})%", line)
            if match:
                confidence = int(match.group(1))
        if "red flag" in line.lower() or "suspicious" in line.lower():
            red_flags.append(line)
    return {
        "is_fake": "fake" in answer.lower(),
        "confidence": confidence,
        "red_flags": red_flags,
        "reasoning": answer
    }

def fetch_url_content(url):
    if not BeautifulSoup:
        raise Exception("BeautifulSoup4 is not installed!")
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=7)
    soup = BeautifulSoup(r.text, "html.parser")
    # Try to get main article text
    texts = []
    for tag in soup.find_all(['h1', 'h2', 'p']):
        if tag.text.strip():
            texts.append(tag.text.strip())
    return "\n".join(texts[:40])

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        text = data.get("text", "")
        if not text.strip():
            return jsonify({"error": "No text provided."}), 400
        if OPENAI_API_KEY:
            result = gpt_analysis(text)
            result["mode"] = "gpt"
        else:
            result = heuristic_analysis(text)
            result["mode"] = "heuristic"
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json(force=True)
        url = data.get("url", "")
        if not url.startswith("http"):
            return jsonify({"error": "Invalid URL."}), 400
        text = fetch_url_content(url)
        if not text:
            return jsonify({"error": "Could not extract content."}), 400
        if OPENAI_API_KEY:
            result = gpt_analysis(text)
            result["mode"] = "gpt"
        else:
            result = heuristic_analysis(text)
            result["mode"] = "heuristic"
        result["extracted"] = text[:500] + "..." if len(text) > 500 else text
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return jsonify({"status": "Fake News Detector backend running."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
