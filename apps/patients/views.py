from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from paginations import CustomPageNumberPagination
from patients.models import Patient
from patients.serializers import PatientSerializer


@extend_schema(tags=['Patients'])
class PatientsListCreateApiView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    pagination_class = CustomPageNumberPagination


@extend_schema(tags=['Patients'])
class PatientsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'pk'
