from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView

from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer
from paginations import CustomPageNumberPagination


@extend_schema(tags=['Appointments'])
class AppointmentListCreateAPIView(ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pagination_class = CustomPageNumberPagination


@extend_schema(tags=['Appointments'])
class AppointmentDetailAPIView(RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = 'pk'
