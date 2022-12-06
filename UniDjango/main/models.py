from django.db import models

# Create your models here.
class Contacts(models.Model):
    email = models.CharField('Email', max_length= 50)
    telegram = models.CharField('Telegram', max_length= 50)
    phone_number = models.CharField('Phone number', max_length= 12)

    def __str__(self):
        return f'Contact: {self.email}'

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class Certificates(models.Model):
    name_surname = models.CharField('Name and Surname', max_length= 100)
    course_name = models.TextField('Course name')
    date = models.DateField('Date')
    place = models.CharField('Place', max_length= 100)
    course_director = models.CharField('Course director', max_length= 100)

    def __str__(self):
        return f'{self.id}: {self.name_surname}: {self.course_name}'
    

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'