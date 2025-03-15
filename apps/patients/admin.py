from django.contrib import admin
from django.contrib.admin import ModelAdmin

from patients.models import Patient


@admin.register(Patient)
class PatientModelAdmin(ModelAdmin):
    pass
