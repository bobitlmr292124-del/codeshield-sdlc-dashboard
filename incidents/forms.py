
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "placeholder": "Enter your email address"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "An account with this email already exists."
            )

        return email
