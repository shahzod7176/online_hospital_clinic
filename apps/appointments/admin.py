from django.contrib import admin
from django.contrib.admin import ModelAdmin

from appointments.models import Appointment


@admin.register(Appointment)
class AppointmentModelAdmin(ModelAdmin):
    pass
