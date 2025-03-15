from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from patients.models import Patient


class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    def validate_phone_number(self, value):
        """Telefon raqam xalqaro formatda ekanligini tekshiramiz"""
        if not value.startswith('+998'):
            raise serializers.ValidationError("Telefon raqami xalqaro formatda bo‘lishi kerak. Masalan: +998901234567")
        return value

    def validate_age(self, value):
        """Bemor yoshi 0 dan kichik bo‘lishi mumkin emas"""
        if value < 0:
            raise serializers.ValidationError("Yosh manfiy bo‘lishi mumkin emas.")
        return value
