from flask import Flask, render_template, request
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load model and preprocessors once
model = load_model("ann_removal_model_v3.keras")
preprocessor = joblib.load("preprocessor_v3.pkl")
y_scaler = joblib.load("y_scaler_v3.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            adsorbent = request.form["adsorbent"].strip()
            time = float(request.form["time"])
            initial_concentration = float(request.form["initial_concentration"])
            ph = float(request.form["ph"])
            dosage = float(request.form["dosage"])
            temperature = float(request.form["temperature"])

            # Backend validation
            if adsorbent == "":
                error = "Adsorbent name cannot be empty."
            elif not (0 <= ph <= 14):
                error = "pH must be between 0 and 14."
            elif time < 0:
                error = "Time cannot be negative."
            elif initial_concentration < 0:
                error = "Initial concentration cannot be negative."
            elif dosage < 0:
                error = "Dosage cannot be negative."
            elif temperature < 0:
                error = "Temperature cannot be negative."
            else:
                new_data = pd.DataFrame([{
                    "Adsorbent": adsorbent,
                    "Time": time,
                    "Initial_Concentration": initial_concentration,
                    "pH": ph,
                    "Dosage": dosage,
                    "Temperature": temperature
                }])

                X_new = preprocessor.transform(new_data)
                if hasattr(X_new, "toarray"):
                    X_new = X_new.toarray()

                y_pred_scaled = model.predict(X_new)
                y_pred = y_scaler.inverse_transform(y_pred_scaled)
                prediction = round(float(y_pred[0][0]), 2)

        except Exception as e:
            error = str(e)

    return render_template("index.html", prediction=prediction, error=error)


if __name__ == "__main__":
    app.run(debug=True)