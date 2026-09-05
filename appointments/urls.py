from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.appointments,
        name='appointments'
    ),

    path(
        'appointment-save/',
        views.appointment_save,
        name='appointment_save'
    ),

    path(
        'appointment-edit/<int:id>/',
        views.appointment_edit,
        name='appointment_edit'
    ),

    path(
        'appointment-update/<int:id>/',
        views.appointment_update,
        name='appointment_update'
    ),

    path(
        'appointment-delete/<int:id>/',
        views.appointment_delete,
        name='appointment_delete'
    ),

]