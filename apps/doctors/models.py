from django.db.models import Model, CharField, DateTimeField


class Doctor(Model):
    first_name = CharField(max_length=250)
    last_name = CharField(max_length=250)
    specialization = CharField(max_length=250) #Mutaxasislik
    phone_number = CharField(max_length=250)
    email = CharField(max_length=250)
    experience = CharField(max_length=250) #Tajriba
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

