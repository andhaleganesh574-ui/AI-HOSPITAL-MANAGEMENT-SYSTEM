from django.shortcuts import render, redirect, get_object_or_404

from .models import Doctor
from admin_panel.models import Department


def doctors(request):

    data = Doctor.objects.select_related(
        'department'
    ).all().order_by('name')

    departments = Department.objects.all().order_by('name')

    return render(
        request,
        'doctors/doctors.html',
        {
            'data': data,
            'departments': departments
        }
    )


def doctor_save(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        specialization = request.POST.get('specialization')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        department_id = request.POST.get('department')
        consultation_fee = request.POST.get('consultation_fee')
        available = request.POST.get('available')

        department = get_object_or_404(
            Department,
            id=department_id
        )

        Doctor.objects.create(
            name=name,
            email=email,
            phone=phone,
            gender=gender,
            specialization=specialization,
            qualification=qualification,
            experience=experience,
            department=department,
            consultation_fee=consultation_fee,
            available=True if available else False
        )

        return redirect('doctors')

    return redirect('doctors')


def doctor_edit(request, id):

    doctor = get_object_or_404(
        Doctor,
        id=id
    )

    departments = Department.objects.all().order_by('name')

    return render(
        request,
        'doctors/doctor_edit.html',
        {
            'doctor': doctor,
            'departments': departments
        }
    )


def doctor_update(request, id):

    doctor = get_object_or_404(
        Doctor,
        id=id
    )

    if request.method == 'POST':

        doctor.name = request.POST.get('name')
        doctor.email = request.POST.get('email')
        doctor.phone = request.POST.get('phone')
        doctor.gender = request.POST.get('gender')
        doctor.specialization = request.POST.get('specialization')
        doctor.qualification = request.POST.get('qualification')
        doctor.experience = request.POST.get('experience')
        doctor.consultation_fee = request.POST.get('consultation_fee')

        department_id = request.POST.get('department')

        doctor.department = get_object_or_404(
            Department,
            id=department_id
        )

        doctor.available = (
            True
            if request.POST.get('available')
            else False
        )

        doctor.save()

        return redirect('doctors')

    return redirect(
        'doctor_edit',
        id=id
    )


def doctor_delete(request, id):

    doctor = get_object_or_404(
        Doctor,
        id=id
    )

    doctor.delete()

    return redirect('doctors')
