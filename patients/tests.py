from django.test import TestCase

from .models import (
    Condition,
    Patient)


class PatientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        asthma = Condition.objects.create(name='Asthma')
        diabetes = Condition.objects.create(name='Diabetes')
        high_blood_pressure = Condition.objects.create(
            name='High blood pressure')
        patient = Patient.objects.create(
            first_name='Henry',
            last_name='Levin',
            gender='m',
            organization='University Health Network')
        patient.conditions.add(
            asthma,
            diabetes,
            high_blood_pressure)
        patient.save()

    def setUp(self):
        pass

    def test_patients_model(self):
        patients = Patient.objects.count()

        self.assertEqual(patients, 1)
