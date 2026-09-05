from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import UserProfile

from doctors.models import Doctor
from patients.models import Patient
from admin_panel.models import Department


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            # Admin / Superuser
            if user.is_superuser:
                return redirect('dashboard')

            # Doctor / Patient
            try:

                profile = user.userprofile

                if profile.role == 'Doctor':
                    return redirect('doctor_dashboard')

                elif profile.role == 'Patient':
                    return redirect('patient_dashboard')

            except UserProfile.DoesNotExist:

                messages.error(
                    request,
                    'User profile not found.'
                )

                logout(request)

                return redirect('login')

        else:

            messages.error(
                request,
                'Invalid username or password.'
            )

    return render(
        request,
        'accounts/login.html'
    )


def register_view(request):

    # Get departments for registration page
    departments = Department.objects.all().order_by('name')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get(
            'confirm_password'
        )

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        role = request.POST.get('role')

        phone = request.POST.get('phone')
        address = request.POST.get('address')


        # Doctor fields
        gender = request.POST.get('gender')
        specialization = request.POST.get('specialization')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        department_id = request.POST.get('department')
        consultation_fee = request.POST.get(
            'consultation_fee'
        )


        # Password check

        if password != confirm_password:

            messages.error(
                request,
                'Passwords do not match.'
            )

            return redirect('register')


        # Username check

        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                'Username already exists.'
            )

            return redirect('register')


        # Email check for Doctor

        if role == 'Doctor':

            if Doctor.objects.filter(
                email=email
            ).exists():

                messages.error(
                    request,
                    'Doctor with this email already exists.'
                )

                return redirect('register')


        # Email check for Patient

        if role == 'Patient':

            if Patient.objects.filter(
                email=email
            ).exists():

                messages.error(
                    request,
                    'Patient with this email already exists.'
                )

                return redirect('register')


        # Create User

        user = User.objects.create_user(

            username=username,

            password=password,

            email=email,

            first_name=first_name,

            last_name=last_name
        )


        # Create User Profile

        UserProfile.objects.create(

            user=user,

            role=role,

            phone=phone,

            address=address
        )


        # =====================================
        # CREATE DOCTOR RECORD
        # =====================================

        if role == 'Doctor':

            if not gender:
                messages.error(
                    request,
                    'Please select doctor gender.'
                )

                user.delete()

                return redirect('register')


            if not specialization:
                messages.error(
                    request,
                    'Please enter specialization.'
                )

                user.delete()

                return redirect('register')


            if not qualification:
                messages.error(
                    request,
                    'Please enter qualification.'
                )

                user.delete()

                return redirect('register')


            if not department_id:

                messages.error(
                    request,
                    'Please select department.'
                )

                user.delete()

                return redirect('register')


            department = Department.objects.get(
                id=department_id
            )


            Doctor.objects.create(

                name=f"{first_name} {last_name}",

                email=email,

                phone=phone,

                gender=gender,

                specialization=specialization,

                qualification=qualification,

                experience=int(experience or 0),

                department=department,

                consultation_fee=consultation_fee or 0,

                available=True
            )


        # =====================================
        # CREATE PATIENT RECORD
        # =====================================

        elif role == 'Patient':

            # Patient model requires these fields.
            # They are not currently present in your
            # registration form.

            messages.success(
                request,
                'Account created successfully. Please login.'
            )

            return redirect('login')


        messages.success(
            request,
            'Registration successful. Please login.'
        )

        return redirect('login')


    return render(
        request,
        'accounts/register.html',
        {
            'departments': departments
        }
    )


def logout_view(request):

    logout(request)

    return redirect('login')