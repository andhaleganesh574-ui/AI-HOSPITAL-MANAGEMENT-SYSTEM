from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.pharmacy,
        name='pharmacy'
    ),

    path(
        'medicine-save/',
        views.medicine_save,
        name='medicine_save'
    ),

    path(
        'medicine-edit/<int:id>/',
        views.medicine_edit,
        name='medicine_edit'
    ),

    path(
        'medicine-update/<int:id>/',
        views.medicine_update,
        name='medicine_update'
    ),

    path(
        'medicine-delete/<int:id>/',
        views.medicine_delete,
        name='medicine_delete'
    ),

    path(
    'stock-in/<int:id>/',
    views.stock_in,
    name='stock_in'
    ),

    path(
    'stock-out/<int:id>/',
    views.stock_out,
    name='stock_out'
    ),

    ]