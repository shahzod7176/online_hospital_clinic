from django.urls import path

from appointments.views import AppointmentListCreateAPIView, AppointmentDetailAPIView

urlpatterns = [
    path('appointments', AppointmentListCreateAPIView.as_view(), name='appointment_list'),
    path('appointments/<int:pk>', AppointmentDetailAPIView.as_view(), name='appointment_detail'),
]