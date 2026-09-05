from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.doctors,
        name='doctors'
    ),

    path(
        'doctor-save/',
        views.doctor_save,
        name='doctor_save'
    ),

    path(
        'doctor-edit/<int:id>/',
        views.doctor_edit,
        name='doctor_edit'
    ),

    path(
        'doctor-update/<int:id>/',
        views.doctor_update,
        name='doctor_update'
    ),

    path(
        'doctor-delete/<int:id>/',
        views.doctor_delete,
        name='doctor_delete'
    ),

]