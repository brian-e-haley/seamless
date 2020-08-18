import json
import os

from django.core.management.base import BaseCommand, CommandError

from patients.models import Condition, Patient


class Command(BaseCommand):
    """
    Command to parse the provided json and populate Condition and Patient with
    all the available data.
    """
    FILENAME = 'patient.json'
    PATH = 'patients/source_data'
    help = f"Looks in the Patient app's source_data directory and attempts " \
           f"to load all patients from a {FILENAME} file."
    GENDERS = {key.lower(): value for value, key in Patient.GENDERS}

    def handle(self, *args, **options):
        self.stdout.write(
            f"Attempting to find a {self.FILENAME} file in the Patient app's "
            f"source_data directory.")
        if self.FILENAME in os.listdir(self.PATH):
            with open(f'{self.PATH}/{self.FILENAME}') as file:
                data = json.load(file)
                conditions = [
                    Condition.objects.create(name=condition)
                    for condition
                    in data['conditions']]
                patient = Patient.objects.create(
                    first_name=data['name'][0]['given'][0],
                    last_name=data['name'][0]['family'][0],
                    organization=data['managingOrganization']['display'],
                    gender=self.GENDERS.get(data['gender'].lower()))
                for condition in conditions:
                    patient.conditions.add(condition)
                patient.save()
                self.stdout.write(self.style.SUCCESS(
                    f"The data for {patient.first_name} {patient.last_name} "
                    f"was loaded successfully."))
        else:
            raise CommandError(
                f"There is no {self.FILENAME} in the Patient app's source_data "
                f"directory.")
