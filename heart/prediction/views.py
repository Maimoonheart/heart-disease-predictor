import joblib
import os

from django.shortcuts import render

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'heart', 'heart_disease_model.pkl')
model = joblib.load(model_path)

def predict_heart(request):
    prediction = None
    probability = None
    risk_level = None

    if request.method == 'POST':
        try:
            features = [[
                int(request.POST['age']),
                int(request.POST['sex']),
                int(request.POST['cp']),
                float(request.POST['trestbps']),
                float(request.POST['chol']),
                int(request.POST['fbs']),
                int(request.POST['restecg']),
                float(request.POST['thalach']),
                int(request.POST['exang']),
                float(request.POST['oldpeak']),
                int(request.POST['slope']),
                int(request.POST['ca']),
                int(request.POST['thal']),
            ]]

            result = model.predict(features)[0]
            prob = model.predict_proba(features)[0][1]
            probability = round(prob * 100, 2)

            if result == 1:
                prediction = "High Risk of Heart Disease"
                risk_level = "high"
            else:
                prediction = "Low Risk of Heart Disease"
                risk_level = "low"

        except Exception as e:
            print("Prediction error:", e)

    return render(request, 'heart.html', {
        'prediction': prediction,
        'probability': probability,
        'risk_level': risk_level
    })