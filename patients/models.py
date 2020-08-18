from django.db import models


class Condition(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Patient(models.Model):
    MALE = 'm'
    FEMALE = 'f'
    UNDISCLOSED = 'u'
    GENDERS = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNDISCLOSED, 'Undisclosed')]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=1,
        choices=GENDERS)
    conditions = models.ManyToManyField(Condition)

    class Meta:
        ordering = [
            'last_name',
            'first_name',
            'pk']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
