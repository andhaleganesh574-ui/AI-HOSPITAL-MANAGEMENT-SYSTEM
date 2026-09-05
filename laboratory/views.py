from django.shortcuts import render

# Create your views here.from django.shortcuts import render, redirect, get_object_or_404

from .models import LabTest
from patients.models import Patient
from doctors.models import Doctor


def laboratory(request):

    data = LabTest.objects.select_related(
        'patient',
        'doctor'
    ).all().order_by('-test_date')

    patients = Patient.objects.all().order_by('name')
    doctors = Doctor.objects.all().order_by('name')

    return render(
        request,
        'laboratory/laboratory.html',
        {
            'data': data,
            'patients': patients,
            'doctors': doctors
        }
    )


def lab_test_save(request):

    if request.method == 'POST':

        patient = get_object_or_404(
            Patient,
            id=request.POST.get('patient')
        )

        doctor_id = request.POST.get('doctor')

        doctor = None

        if doctor_id:
            doctor = get_object_or_404(
                Doctor,
                id=doctor_id
            )

        LabTest.objects.create(
            patient=patient,
            doctor=doctor,
            test_name=request.POST.get('test_name'),
            test_category=request.POST.get('test_category'),
            sample_type=request.POST.get('sample_type'),
            test_date=request.POST.get('test_date'),
            result=request.POST.get('result'),
            normal_range=request.POST.get('normal_range'),
            remarks=request.POST.get('remarks'),
            status=request.POST.get('status'),
            report_number=request.POST.get('report_number')
        )

        return redirect('laboratory')

    return redirect('laboratory')


def lab_test_edit(request, id):

    lab_test = get_object_or_404(
        LabTest,
        id=id
    )

    patients = Patient.objects.all().order_by('name')
    doctors = Doctor.objects.all().order_by('name')

    return render(
        request,
        'laboratory/lab_test_edit.html',
        {
            'lab_test': lab_test,
            'patients': patients,
            'doctors': doctors
        }
    )


def lab_test_update(request, id):

    lab_test = get_object_or_404(
        LabTest,
        id=id
    )

    if request.method == 'POST':

        lab_test.patient = get_object_or_404(
            Patient,
            id=request.POST.get('patient')
        )

        doctor_id = request.POST.get('doctor')

        if doctor_id:
            lab_test.doctor = get_object_or_404(
                Doctor,
                id=doctor_id
            )
        else:
            lab_test.doctor = None

        lab_test.test_name = request.POST.get('test_name')
        lab_test.test_category = request.POST.get('test_category')
        lab_test.sample_type = request.POST.get('sample_type')
        lab_test.test_date = request.POST.get('test_date')
        lab_test.result = request.POST.get('result')
        lab_test.normal_range = request.POST.get('normal_range')
        lab_test.remarks = request.POST.get('remarks')
        lab_test.status = request.POST.get('status')
        lab_test.report_number = request.POST.get('report_number')

        lab_test.save()

        return redirect('laboratory')

    return redirect(
        'lab_test_edit',
        id=id
    )


def lab_test_delete(request, id):

    lab_test = get_object_or_404(
        LabTest,
        id=id
    )

    lab_test.delete()

    return redirect('laboratory')
