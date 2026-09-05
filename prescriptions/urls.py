from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.prescription_list,
        name='prescriptions'
    ),

    path(
        'add/<int:patient_id>/',
        views.add_prescription,
        name='add_prescription'
    ),

]