
from django import forms
from .models import Incident


class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = [
            "incident_id",
            "title",
            "description",
            "pillar",
            "severity",
            "status",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }