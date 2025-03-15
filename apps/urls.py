from django.urls import path, include

urlpatterns = [
    path('appointments/', include('appointments.urls')),
    path('doctors/', include('doctors.urls')),
    path('patients/', include('patients.urls')),
]