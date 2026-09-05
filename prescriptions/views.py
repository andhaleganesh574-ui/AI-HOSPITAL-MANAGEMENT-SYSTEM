from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from prescriptions.models import Prescription
from patients.models import Patient
from doctors.models import Doctor
from pharmacy.models import Medicine


@login_required
def add_prescription(request, patient_id):

    if not hasattr(request.user, 'userprofile'):
        return render(
            request,
            'doctor_panel/access_denied.html'
        )

    if request.user.userprofile.role != 'Doctor':
        return render(
            request,
            'doctor_panel/access_denied.html'
        )

    try:
        doctor = Doctor.objects.get(
            name=f"{request.user.first_name} {request.user.last_name}"
        )

        patient = Patient.objects.get(
            id=patient_id
        )

    except (
        Doctor.DoesNotExist,
        Patient.DoesNotExist
    ):
        return redirect('doctor_dashboard')


    medicines = Medicine.objects.all().order_by('name')


    if request.method == 'POST':

        medicine_id = request.POST.get('medicine')
        dosage = request.POST.get('dosage')
        frequency = request.POST.get('frequency')
        duration = request.POST.get('duration')
        instructions = request.POST.get('instructions')


        # Check required fields

        if not medicine_id:
            return render(
                request,
                'prescriptions/add_prescription.html',
                {
                    'patient': patient,
                    'medicines': medicines,
                    'error': 'Please select a medicine.'
                }
            )


        if not frequency:
            return render(
                request,
                'prescriptions/add_prescription.html',
                {
                    'patient': patient,
                    'medicines': medicines,
                    'error': 'Please select frequency.'
                }
            )


        if not dosage:
            return render(
                request,
                'prescriptions/add_prescription.html',
                {
                    'patient': patient,
                    'medicines': medicines,
                    'error': 'Please enter dosage.'
                }
            )


        if not duration:
            return render(
                request,
                'prescriptions/add_prescription.html',
                {
                    'patient': patient,
                    'medicines': medicines,
                    'error': 'Please enter duration.'
                }
            )


        medicine = Medicine.objects.get(
            id=medicine_id
        )


        Prescription.objects.create(

            patient=patient,

            doctor=doctor,

            medicine=medicine,

            dosage=dosage,

            frequency=frequency,

            duration=duration,

            instructions=instructions or ''

        )


        return redirect('doctor_dashboard')


    return render(
        request,
        'prescriptions/add_prescription.html',
        {
            'patient': patient,
            'medicines': medicines,
        }
    )


# ==========================================
# PRESCRIPTION LIST
# ==========================================

@login_required
def prescription_list(request):

    if not hasattr(request.user, 'userprofile'):
        return render(
            request,
            'doctor_panel/access_denied.html'
        )

    if request.user.userprofile.role != 'Doctor':
        return render(
            request,
            'doctor_panel/access_denied.html'
        )

    try:

        doctor = Doctor.objects.get(
            name=f"{request.user.first_name} {request.user.last_name}"
        )

    except Doctor.DoesNotExist:

        return redirect('doctor_dashboard')


    prescriptions = Prescription.objects.filter(
        doctor=doctor
    ).select_related(
        'patient',
        'medicine'
    ).order_by('-id')


    return render(
        request,
        'prescriptions/prescriptions.html',
        {
            'prescriptions': prescriptions
        }
    )