from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.patients,
        name='patients'
    ),

    path(
        'patient-save/',
        views.patient_save,
        name='patient_save'
    ),

    path(
        'patient-edit/<int:id>/',
        views.patient_edit,
        name='patient_edit'
    ),

    path(
        'patient-update/<int:id>/',
        views.patient_update,
        name='patient_update'
    ),

    path(
        'patient-delete/<int:id>/',
        views.patient_delete,
        name='patient_delete'
    ),

]