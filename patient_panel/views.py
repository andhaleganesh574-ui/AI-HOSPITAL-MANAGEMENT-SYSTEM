from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from appointments.models import Appointment
from patients.models import Patient
from doctors.models import Doctor
from prescriptions.models import Prescription


@login_required
def patient_dashboard(request):

    # Check user profile
    if not hasattr(request.user, 'userprofile'):
        return render(
            request,
            'patient_panel/access_denied.html'
        )

    # Only Patient can access
    if request.user.userprofile.role != 'Patient':
        return render(
            request,
            'patient_panel/access_denied.html'
        )

    try:

        patient = Patient.objects.get(
            name=f"{request.user.first_name} {request.user.last_name}"
        )

        # Patient Appointments
        appointments = Appointment.objects.filter(
            patient=patient
        ).select_related(
            'doctor'
        ).order_by(
            '-appointment_date',
            '-appointment_time'
        )

        # Patient Prescriptions
        prescriptions = Prescription.objects.filter(
            patient=patient
        ).select_related(
            'doctor',
            'medicine'
        ).order_by(
            '-prescribed_date'
        )

    except Patient.DoesNotExist:

        appointments = []
        prescriptions = []

    return render(
        request,
        'patient_panel/dashboard.html',
        {
            'appointments': appointments,
            'prescriptions': prescriptions
        }
    )


@login_required
def book_appointment(request):

    # Check user profile
    if not hasattr(request.user, 'userprofile'):
        return render(
            request,
            'patient_panel/access_denied.html'
        )

    # Only Patient can book appointment
    if request.user.userprofile.role != 'Patient':
        return render(
            request,
            'patient_panel/access_denied.html'
        )

    try:

        patient = Patient.objects.get(
            name=f"{request.user.first_name} {request.user.last_name}"
        )

    except Patient.DoesNotExist:

        return render(
            request,
            'patient_panel/access_denied.html'
        )

    # Show all doctors
    doctors = Doctor.objects.all().select_related(
        'department'
    ).order_by('name')


    # Save Appointment
    if request.method == 'POST':

        doctor_id = request.POST.get('doctor')
        appointment_date = request.POST.get(
            'appointment_date'
        )
        appointment_time = request.POST.get(
            'appointment_time'
        )
        reason = request.POST.get('reason')


        doctor = Doctor.objects.get(
            id=doctor_id
        )


        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            reason=reason
        )


        return redirect(
            'patient_dashboard'
        )


    return render(
        request,
        'patient_panel/book_appointment.html',
        {
            'doctors': doctors
        }
    )