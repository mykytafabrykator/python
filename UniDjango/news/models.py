from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Title', max_length= 50)
    anons = models.CharField('Anons', max_length= 250)
    full_text = models.TextField('Article Text')
    date = models.DateTimeField('Date')

    def __str__(self):
        return f'News: {self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'