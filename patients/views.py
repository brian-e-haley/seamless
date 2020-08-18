from django.views.generic import ListView

from .models import Patient


class PatientListView(ListView):
    model = Patient
    context_object_name = 'patients'



