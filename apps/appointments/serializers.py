from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from appointments.models import Appointment


class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    def validate_date(self, value):
        """ Faqat kelajakdagi sanalarni qabul qilish """
        from django.utils.timezone import now
        if value < now():
            raise serializers.ValidationError("Appointment faqat kelajakdagi sana bo‘lishi kerak.")
        return value
