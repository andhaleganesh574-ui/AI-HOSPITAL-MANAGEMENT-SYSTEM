from django.shortcuts import render, redirect, get_object_or_404

from .models import Appointment
from doctors.models import Doctor
from patients.models import Patient


def appointments(request):

    data = Appointment.objects.select_related(
        'patient',
        'doctor',
        'doctor__department'
    ).all().order_by(
        '-appointment_date',
        '-appointment_time'
    )

    patients = Patient.objects.all().order_by('name')

    # Show all doctors
    doctors = Doctor.objects.select_related(
        'department'
    ).all().order_by('name')

    return render(
        request,
        'appointments/appointments.html',
        {
            'data': data,
            'patients': patients,
            'doctors': doctors
        }
    )


def appointment_save(request):

    if request.method == 'POST':

        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        reason = request.POST.get('reason')
        status = request.POST.get('status')

        patient = get_object_or_404(
            Patient,
            id=patient_id
        )

        doctor = get_object_or_404(
            Doctor,
            id=doctor_id
        )

        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            reason=reason,
            status=status
        )

        return redirect('appointments')

    return redirect('appointments')


def appointment_edit(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    patients = Patient.objects.all().order_by('name')

    # Show all doctors
    doctors = Doctor.objects.select_related(
        'department'
    ).all().order_by('name')

    return render(
        request,
        'appointments/appointment_edit.html',
        {
            'appointment': appointment,
            'patients': patients,
            'doctors': doctors
        }
    )


def appointment_update(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    if request.method == 'POST':

        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')

        appointment.patient = get_object_or_404(
            Patient,
            id=patient_id
        )

        appointment.doctor = get_object_or_404(
            Doctor,
            id=doctor_id
        )

        appointment.appointment_date = request.POST.get(
            'appointment_date'
        )

        appointment.appointment_time = request.POST.get(
            'appointment_time'
        )

        appointment.reason = request.POST.get(
            'reason'
        )

        appointment.status = request.POST.get(
            'status'
        )

        appointment.save()

        return redirect('appointments')

    return redirect(
        'appointment_edit',
        id=id
    )


def appointment_delete(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    appointment.delete()

    return redirect('appointments')