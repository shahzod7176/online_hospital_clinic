from django.urls import path

from doctors.views import DoctorListAPIView, DoctorRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('Doctor', DoctorListAPIView.as_view(), name='doctor-list'),
    path('Doctor<int:pk>', DoctorRetrieveUpdateDestroyAPIView.as_view(), name='doctor-detail'),
]
