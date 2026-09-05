from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.doctor_dashboard,
        name='doctor_dashboard'
    ),

    path(
        'dashboard/',
        views.doctor_dashboard,
        name='doctor_dashboard_page'
    ),

    path(
        'appointment/<int:id>/<str:status>/',
        views.update_appointment_status,
        name='update_appointment_status'
    ),

]