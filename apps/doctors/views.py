from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from doctors.models import Doctor
from doctors.serializers import DoctorSerializer
from paginations import CustomPageNumberPagination


@extend_schema(tags=['Doctors'])
class DoctorListAPIView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = CustomPageNumberPagination


@extend_schema(tags=['Doctors'])
class DoctorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'pk'
