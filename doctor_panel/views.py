from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from appointments.models import Appointment
from doctors.models import Doctor
from patients.models import Patient


@login_required
def doctor_dashboard(request):

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

        # Doctor's appointments
        appointments = Appointment.objects.filter(
            doctor=doctor
        ).order_by(
            '-appointment_date',
            '-appointment_time'
        )

        # Doctor's patients
        patient_ids = appointments.values_list(
            'patient_id',
            flat=True
        ).distinct()

        patients = Patient.objects.filter(
            id__in=patient_ids
        )

        # Counts
        total_patients = patients.count()

        pending_appointments = appointments.filter(
            status='Pending'
        ).count()

        completed_appointments = appointments.filter(
            status='Completed'
        ).count()

        today_appointments = appointments.filter(
            appointment_date=timezone.localdate()
        ).count()

    except Doctor.DoesNotExist:

        appointments = []
        patients = []
        total_patients = 0
        pending_appointments = 0
        completed_appointments = 0
        today_appointments = 0

    return render(
        request,
        'doctor_panel/dashboard.html',
        {
            'appointments': appointments,
            'patients': patients,
            'total_patients': total_patients,
            'pending_appointments': pending_appointments,
            'completed_appointments': completed_appointments,
            'today_appointments': today_appointments,
        }
    )


@login_required
def update_appointment_status(request, id, status):

    if request.method == 'POST':

        try:

            doctor = Doctor.objects.get(
                name=f"{request.user.first_name} {request.user.last_name}"
            )

            appointment = Appointment.objects.get(
                id=id,
                doctor=doctor
            )

            if status in [
                'Confirmed',
                'Completed',
                'Cancelled'
            ]:

                appointment.status = status
                appointment.save()

        except (
            Doctor.DoesNotExist,
            Appointment.DoesNotExist
        ):
            pass

    return redirect('doctor_dashboard')