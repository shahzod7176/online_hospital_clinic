from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
import re
from doctors.models import Doctor


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_phone_number(self, value):
        """Telefon raqam xalqaro formatda ekanligini tekshiramiz"""
        if not value.startswith('+998'):
            raise serializers.ValidationError("Telefon raqami xalqaro formatda bo‘lishi kerak. Masalan: +998901234567")
        return value

    def validate_specialization(self, value):
        print(f"Validating specialization: {value}")  # Bu ishlayotganini tekshirish uchun
        """Mutaxassislik faqat harflardan iborat bo‘lishi kerak"""
        if not re.match(r'^[A-Za-z\s]+$', value):  # Faqat harflar va bo‘sh joylarga ruxsat
            raise serializers.ValidationError("Mutaxassislik faqat harflardan iborat bo‘lishi kerak.")
        return value
