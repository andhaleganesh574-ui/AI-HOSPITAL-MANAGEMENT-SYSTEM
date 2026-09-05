from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.billing,
        name='billing'
    ),

    path(
        'bill-save/',
        views.bill_save,
        name='bill_save'
    ),

    path(
        'bill-edit/<int:id>/',
        views.bill_edit,
        name='bill_edit'
    ),

    path(
        'bill-update/<int:id>/',
        views.bill_update,
        name='bill_update'
    ),

    path(
        'bill-delete/<int:id>/',
        views.bill_delete,
        name='bill_delete'
    ),

]