from django.db.models import Model, CharField, DateField, DateTimeField, SlugField


class Patient(Model):
    first_name = CharField(max_length=250)
    last_name = CharField(max_length=250)
    date_of_birth = DateField()
    phone_number = CharField(max_length=250)
    email = CharField(max_length=250)
    address = CharField(max_length=250)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
