from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Fake News Detector API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    # Placeholder for prediction logic
    prediction = "Fake" if "fake" in text.lower() else "Real"
    confidence = 0.9 if prediction == "Fake" else 0.8
    return jsonify({"prediction": prediction, "confidence": confidence})

if __name__ == '__main__':
    app.run(debug=True)