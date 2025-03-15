from django.contrib import admin
from django.contrib.admin import ModelAdmin

from doctors.models import Doctor


@admin.register(Doctor)
class DoctorModelAdmin(ModelAdmin):
    pass
