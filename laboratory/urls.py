from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.laboratory,
        name='laboratory'
    ),

    path(
        'save/',
        views.lab_test_save,
        name='lab_test_save'
    ),

    path(
        'edit/<int:id>/',
        views.lab_test_edit,
        name='lab_test_edit'
    ),

    path(
        'update/<int:id>/',
        views.lab_test_update,
        name='lab_test_update'
    ),

    path(
        'delete/<int:id>/',
        views.lab_test_delete,
        name='lab_test_delete'
    ),

]