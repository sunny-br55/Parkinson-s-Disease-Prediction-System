from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array(data["features"]).reshape(1, -1)
    result = model.predict(features)[0]

    if result == 1:
        return jsonify({"result": "⚠ Parkinson’s Disease Detected"})
    else:
        return jsonify({"result": "✅ Healthy Person"})

if __name__ == "__main__":
    app.run(debug=True)
