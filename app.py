from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    confidence = None
    input_text = ""
    if request.method == 'POST':
        input_text = request.form.get('text', '')
        prediction = "Fake" if "fake" in input_text.lower() else "Real"
        confidence = 0.9 if prediction == "Fake" else 0.8
        result = "Noticia falsa" if prediction == "Fake" else "Noticia verdadera"
    return render_template('index.html', result=result, confidence=confidence, input_text=input_text)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    prediction = "Fake" if "fake" in text.lower() else "Real"
    confidence = 0.9 if prediction == "Fake" else 0.8
    return jsonify({"prediction": prediction, "confidence": confidence})

if __name__ == '__main__':
    app.run(debug=True)