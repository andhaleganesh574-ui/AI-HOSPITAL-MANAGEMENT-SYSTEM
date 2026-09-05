from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.patient_dashboard,
        name='patient_dashboard'
    ),

    path(
        'book-appointment/',
        views.book_appointment,
        name='book_appointment'
    ),

]