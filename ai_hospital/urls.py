from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', include('admin_panel.urls')),

    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),

    path('admin-panel/', include('admin_panel.urls')),

    path('doctors/', include('doctors.urls')),

    path('patients/', include('patients.urls')),

    path('appointments/', include('appointments.urls')),

    path('pharmacy/', include('pharmacy.urls')),

    path('billing/', include('billing.urls')),

    path('ai/', include('ai_prediction.urls')),

    path('prescriptions/', include('prescriptions.urls')),

    path('laboratory/', include('laboratory.urls')),

    path('patient-panel/', include('patient_panel.urls')),

    path('doctor-panel/', include('doctor_panel.urls')),
    ]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )