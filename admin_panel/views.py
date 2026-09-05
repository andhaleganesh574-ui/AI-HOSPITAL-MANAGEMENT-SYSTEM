from django.shortcuts import render, redirect, get_object_or_404

from appointments.models import Appointment
from doctors.models import Doctor
from patients.models import Patient
from pharmacy.models import Medicine
from admin_panel.models import Department


# ==========================================
# HOME
# ==========================================

def home(request):
    return render(
        request,
        'home.html'
    )


# ==========================================
# ADMIN DASHBOARD
# ==========================================

def dashboard(request):

    total_departments = Department.objects.count()
    total_doctors = Doctor.objects.count()
    total_patients = Patient.objects.count()
    total_appointments = Appointment.objects.count()
    total_medicines = Medicine.objects.count()

    # Appointment status counts

    pending_appointments = Appointment.objects.filter(
        status='Pending'
    ).count()

    confirmed_appointments = Appointment.objects.filter(
        status='Confirmed'
    ).count()

    completed_appointments = Appointment.objects.filter(
        status='Completed'
    ).count()

    cancelled_appointments = Appointment.objects.filter(
        status='Cancelled'
    ).count()

    # Monthly appointment data

    monthly_appointments = []

    for month in range(1, 13):

        count = Appointment.objects.filter(
            appointment_date__month=month
        ).count()

        monthly_appointments.append(count)

    # Recent appointments

    recent_appointments = Appointment.objects.select_related(
        'patient',
        'doctor'
    ).order_by(
        '-created_at'
    )[:5]

    context = {

        'total_departments': total_departments,

        'total_doctors': total_doctors,

        'total_patients': total_patients,

        'total_appointments': total_appointments,

        'total_medicines': total_medicines,

        'pending_appointments': pending_appointments,

        'confirmed_appointments': confirmed_appointments,

        'completed_appointments': completed_appointments,

        'cancelled_appointments': cancelled_appointments,

        'monthly_appointments': monthly_appointments,

        'recent_appointments': recent_appointments,

    }

    return render(
        request,
        'admin_panel/dashboard.html',
        context
    )


# ==========================================
# DEPARTMENT
# ==========================================

def departments(request):

    data = Department.objects.all().order_by(
        'name'
    )

    return render(
        request,
        'admin_panel/departments.html',
        {
            'data': data
        }
    )


def department_save(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        description = request.POST.get(
            'description'
        )

        Department.objects.create(

            name=name,

            description=description

        )

        return redirect(
            'departments'
        )

    return redirect(
        'departments'
    )


def department_edit(request, id):

    department = get_object_or_404(
        Department,
        id=id
    )

    return render(
        request,
        'admin_panel/department_edit.html',
        {
            'department': department
        }
    )


def department_update(request, id):

    department = get_object_or_404(
        Department,
        id=id
    )

    if request.method == 'POST':

        department.name = request.POST.get(
            'name'
        )

        department.description = request.POST.get(
            'description'
        )

        department.save()

        return redirect(
            'departments'
        )

    return redirect(
        'department_edit',
        id=id
    )


def department_delete(request, id):

    department = get_object_or_404(
        Department,
        id=id
    )

    department.delete()

    return redirect(
        'departments'
    )