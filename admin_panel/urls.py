from django.urls import path
from . import views


urlpatterns = [

    # HOME
    path(
        '',
        views.home,
        name='home'
    ),

    # DASHBOARD
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'departments/',
        views.departments,
        name='departments'
    ),

    path(
        'department/save/',
        views.department_save,
        name='department_save'
    ),

    path(
        'department/edit/<int:id>/',
        views.department_edit,
        name='department_edit'
    ),

    path(
        'department/update/<int:id>/',
        views.department_update,
        name='department_update'
    ),

    path(
        'department/delete/<int:id>/',
        views.department_delete,
        name='department_delete'
    ),
]