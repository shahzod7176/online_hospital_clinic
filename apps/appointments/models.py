from django.db.models import Model, ForeignKey, CASCADE, DateField, BooleanField, IntegerField, DateTimeField, CharField


class Appointment(Model):  # Qabul
    patient = ForeignKey('patients.Patient', CASCADE, related_name='appointments')
    doctor = ForeignKey('doctors.Doctor', CASCADE, related_name='appointments')
    appointment_date = DateField()
    status = BooleanField(default=False)


class Payment(Model):
    appointment = ForeignKey('appointments.Appointment', CASCADE, related_name='payments')
    amount = IntegerField(default=0, null=False, blank=False)
    payment_method = IntegerField(default=0, null=False, blank=False)
    status = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)  # tolov sanasi

    def __str__(self):
        return str(self.id)


class Prescription(Model):  # Dori retsept
    appointment = ForeignKey('appointments.Appointment', CASCADE)
    medicines = CharField(max_length=255)  # Dori nomlari
    instructions = CharField(max_length=255)  # Qanday ichish bo‘yicha yo‘riqnoma
