from django import forms

class HeartForm(forms.Form):
    age = forms.IntegerField(label="Age (years)")
    sex = forms.ChoiceField(choices=[(1, "Male"), (0, "Female")], label="Sex")

    cp = forms.ChoiceField(choices=[
        (0, "Typical Angina"),
        (1, "Atypical Angina"),
        (2, "Non-Anginal Pain"),
        (3, "Asymptomatic")
    ], label="Chest Pain Type")

    trestbps = forms.FloatField(label="Resting Blood Pressure (mmHg)")
    chol = forms.FloatField(label="Serum Cholesterol (mg/dL)")

    fbs = forms.ChoiceField(choices=[(1, "Yes"), (0, "No")],
                            label="Fasting Blood Sugar > 120 mg/dL")

    restecg = forms.ChoiceField(choices=[
        (0, "Normal"),
        (1, "ST-T Wave Abnormality"),
        (2, "Left Ventricular Hypertrophy")
    ], label="Resting ECG Results")

    thalach = forms.FloatField(label="Maximum Heart Rate Achieved (bpm)")

    exang = forms.ChoiceField(choices=[(1, "Yes"), (0, "No")],
                              label="Exercise-Induced Angina")

    oldpeak = forms.FloatField(label="ST Depression (Exercise vs Rest)")

    slope = forms.ChoiceField(choices=[
        (0, "Upsloping"),
        (1, "Flat"),
        (2, "Downsloping")
    ], label="Slope of Peak Exercise ST Segment")

    ca = forms.ChoiceField(choices=[
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3")
    ], label="Number of Major Vessels")

    thal = forms.ChoiceField(choices=[
        (1, "Normal"),
        (2, "Fixed Defect"),
        (3, "Reversible Defect")
    ], label="Thalassemia Test Result")