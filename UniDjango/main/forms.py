from .models import Contacts, Certificates
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['email', 'telegram', 'phone_number']

        widgets = {
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'telegram': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telegram'
            }),
            'phone_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            })
        }


class CertificatesForm(ModelForm):
    class Meta:
        model = Certificates
        fields = ['name_surname', 'course_name', 'date', 'place', 'course_director']


        widgets = {
            'name_surname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name and surname',
            }),
            'course_name': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Course name'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date'
            }),
            'place': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Place'
            }),
            'course_director': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Course director'
            })
        }