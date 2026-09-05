from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Prediction


# ==========================================
# AI PREDICTION DASHBOARD
# ==========================================

@login_required
def ai_prediction(request):

    # ADMIN
    if request.user.is_superuser:
        pass

    # DOCTOR
    elif (
        hasattr(request.user, 'userprofile')
        and request.user.userprofile.role == 'Doctor'
    ):
        pass

    # PATIENT / OTHER USER
    else:
        return render(
            request,
            'doctor_panel/access_denied.html'
        )


    predictions = Prediction.objects.all().order_by(
        '-created_at'
    )


    return render(
        request,
        'ai/prediction.html',
        {
            'predictions': predictions
        }
    )


# ==========================================
# PREDICT DISEASE
# ==========================================

@login_required
def predict_disease(request):

    # ADMIN
    if request.user.is_superuser:
        pass

    # DOCTOR
    elif (
        hasattr(request.user, 'userprofile')
        and request.user.userprofile.role == 'Doctor'
    ):
        pass

    else:
        return render(
            request,
            'doctor_panel/access_denied.html'
        )


    if request.method == 'POST':

        patient_name = request.POST.get(
            'patient_name'
        )

        age = int(
            request.POST.get('age') or 0
        )

        gender = request.POST.get(
            'gender'
        )

        temperature = float(
            request.POST.get('temperature') or 0
        )

        blood_pressure = request.POST.get(
            'blood_pressure'
        )

        blood_sugar = float(
            request.POST.get('blood_sugar') or 0
        )

        heart_rate = int(
            request.POST.get('heart_rate') or 0
        )

        symptoms = (
            request.POST.get('symptoms') or ''
        ).lower()


        # DEFAULT RESULT

        disease = "General Infection"

        risk = "Low"

        confidence = 70

        recommendation = (
            "Take adequate rest and consult a doctor."
        )


        # CARDIAC CONDITION

        if (
            "chest pain" in symptoms
            or "shortness of breath" in symptoms
        ):

            disease = "Possible Cardiac Condition"

            risk = "High"

            confidence = 88

            recommendation = (
                "Immediate medical evaluation is recommended."
            )


        # RESPIRATORY INFECTION

        elif (
            "cough" in symptoms
            and "fever" in symptoms
        ):

            disease = "Possible Respiratory Infection"

            risk = "Medium"

            confidence = 84

            recommendation = (
                "Consult a physician and monitor temperature."
            )


        # VIRAL FEVER

        elif (
            "headache" in symptoms
            and "fever" in symptoms
        ):

            disease = "Possible Viral Fever"

            risk = "Medium"

            confidence = 82

            recommendation = (
                "Stay hydrated and consult a doctor if symptoms persist."
            )


        # GASTROINTESTINAL

        elif (
            "stomach pain" in symptoms
            or "vomiting" in symptoms
        ):

            disease = "Possible Gastrointestinal Infection"

            risk = "Medium"

            confidence = 79

            recommendation = (
                "Maintain hydration and seek medical advice."
            )


        # DIABETES

        elif (
            "high sugar" in symptoms
            or blood_sugar > 200
        ):

            disease = "Possible Diabetes Risk"

            risk = "High"

            confidence = 86

            recommendation = (
                "Blood glucose monitoring and medical consultation are recommended."
            )


        # HIGH FEVER

        elif temperature >= 102:

            disease = "High Fever"

            risk = "Medium"

            confidence = 80

            recommendation = (
                "Monitor temperature and consult a physician."
            )


        # SAVE PREDICTION

        Prediction.objects.create(

            patient_name=patient_name,

            age=age,

            gender=gender,

            temperature=temperature,

            blood_pressure=blood_pressure,

            blood_sugar=blood_sugar,

            heart_rate=heart_rate,

            symptoms=symptoms,

            predicted_disease=disease,

            risk_level=risk,

            confidence=confidence,

            recommendation=recommendation

        )


        return redirect(
            'ai_prediction'
        )


    return redirect(
        'ai_prediction'
    )


# ==========================================
# EDIT
# ==========================================

@login_required
def prediction_edit(request, id):

    prediction = get_object_or_404(
        Prediction,
        id=id
    )


    return render(
        request,
        'ai/prediction_edit.html',
        {
            'prediction': prediction
        }
    )


# ==========================================
# UPDATE
# ==========================================

@login_required
def prediction_update(request, id):

    prediction = get_object_or_404(
        Prediction,
        id=id
    )


    if request.method == 'POST':

        prediction.patient_name = request.POST.get(
            'patient_name'
        )

        prediction.age = int(
            request.POST.get('age') or 0
        )

        prediction.gender = request.POST.get(
            'gender'
        )

        prediction.temperature = float(
            request.POST.get('temperature') or 0
        )

        prediction.blood_pressure = request.POST.get(
            'blood_pressure'
        )

        prediction.blood_sugar = float(
            request.POST.get('blood_sugar') or 0
        )

        prediction.heart_rate = int(
            request.POST.get('heart_rate') or 0
        )

        prediction.symptoms = (
            request.POST.get('symptoms') or ''
        ).lower()


        symptoms = prediction.symptoms


        disease = "General Infection"

        risk = "Low"

        confidence = 70

        recommendation = (
            "Take adequate rest and consult a doctor."
        )


        if (
            "chest pain" in symptoms
            or "shortness of breath" in symptoms
        ):

            disease = "Possible Cardiac Condition"

            risk = "High"

            confidence = 88

            recommendation = (
                "Immediate medical evaluation is recommended."
            )


        elif (
            "cough" in symptoms
            and "fever" in symptoms
        ):

            disease = "Possible Respiratory Infection"

            risk = "Medium"

            confidence = 84

            recommendation = (
                "Consult a physician and monitor temperature."
            )


        elif (
            "headache" in symptoms
            and "fever" in symptoms
        ):

            disease = "Possible Viral Fever"

            risk = "Medium"

            confidence = 82

            recommendation = (
                "Stay hydrated and consult a doctor if symptoms persist."
            )


        elif (
            "stomach pain" in symptoms
            or "vomiting" in symptoms
        ):

            disease = "Possible Gastrointestinal Infection"

            risk = "Medium"

            confidence = 79

            recommendation = (
                "Maintain hydration and seek medical advice."
            )


        elif (
            "high sugar" in symptoms
            or prediction.blood_sugar > 200
        ):

            disease = "Possible Diabetes Risk"

            risk = "High"

            confidence = 86

            recommendation = (
                "Blood glucose monitoring and medical consultation are recommended."
            )


        elif prediction.temperature >= 102:

            disease = "High Fever"

            risk = "Medium"

            confidence = 80

            recommendation = (
                "Monitor temperature and consult a physician."
            )


        prediction.predicted_disease = disease

        prediction.risk_level = risk

        prediction.confidence = confidence

        prediction.recommendation = recommendation

        prediction.save()


        return redirect(
            'ai_prediction'
        )


    return redirect(
        'prediction_edit',
        id=id
    )


# ==========================================
# DELETE
# ==========================================

@login_required
def prediction_delete(request, id):

    prediction = get_object_or_404(
        Prediction,
        id=id
    )


    prediction.delete()


    return redirect(
        'ai_prediction'
    )