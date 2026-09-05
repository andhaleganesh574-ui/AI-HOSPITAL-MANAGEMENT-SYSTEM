from django.shortcuts import render, redirect, get_object_or_404

from .models import Patient


def patients(request):

    data = Patient.objects.all().order_by('-registered_at')

    return render(
        request,
        'patients/patients.html',
        {'data': data}
    )


def patient_save(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        blood_group = request.POST.get('blood_group')
        address = request.POST.get('address')
        emergency_contact = request.POST.get('emergency_contact')

        Patient.objects.create(
            name=name,
            email=email,
            phone=phone,
            date_of_birth=date_of_birth,
            gender=gender,
            blood_group=blood_group,
            address=address,
            emergency_contact=emergency_contact
        )

        return redirect('patients')

    return redirect('patients')


def patient_edit(request, id):

    patient = get_object_or_404(
        Patient,
        id=id
    )

    return render(
        request,
        'patients/patient_edit.html',
        {'patient': patient}
    )


def patient_update(request, id):

    patient = get_object_or_404(
        Patient,
        id=id
    )

    if request.method == 'POST':

        patient.name = request.POST.get('name')
        patient.email = request.POST.get('email')
        patient.phone = request.POST.get('phone')
        patient.date_of_birth = request.POST.get('date_of_birth')
        patient.gender = request.POST.get('gender')
        patient.blood_group = request.POST.get('blood_group')
        patient.address = request.POST.get('address')
        patient.emergency_contact = request.POST.get(
            'emergency_contact'
        )

        patient.save()

        return redirect('patients')

    return redirect(
        'patient_edit',
        id=id
    )


def patient_delete(request, id):

    patient = get_object_or_404(
        Patient,
        id=id
    )

    patient.delete()

    return redirect('patients')