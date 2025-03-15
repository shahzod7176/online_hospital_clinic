from django.urls import path

from patients.views import PatientsListCreateApiView, PatientsRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('patients', PatientsListCreateApiView.as_view(), name='patients-list'),
    path('patients/<int:pk>', PatientsRetrieveUpdateDestroyAPIView.as_view(), name='patients-detail'),
]
