from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.ai_prediction,
        name='ai_prediction'
    ),

    path(
        'predict/',
        views.predict_disease,
        name='predict_disease'
    ),

    path(
        'edit/<int:id>/',
        views.prediction_edit,
        name='prediction_edit'
    ),

    path(
        'update/<int:id>/',
        views.prediction_update,
        name='prediction_update'
    ),

    path(
        'delete/<int:id>/',
        views.prediction_delete,
        name='prediction_delete'
    ),

]