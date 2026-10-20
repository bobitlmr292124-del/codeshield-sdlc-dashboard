
from django.db import models


class Incident(models.Model):
    SEVERITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Critical", "Critical"),
    ]

    STATUS_CHOICES = [
        ("Open", "Open"),
        ("Investigating", "Investigating"),
        ("Resolved", "Resolved"),
    ]

    PILLAR_CHOICES = [
        ("Endpoint / IDE", "Endpoint / IDE"),
        ("Version Control", "Version Control"),
        ("CI/CD Pipeline", "CI/CD Pipeline"),
        ("Package Registry", "Package Registry"),
        ("Production", "Production"),
    ]

    incident_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    pillar = models.CharField(max_length=50, choices=PILLAR_CHOICES)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Open"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.incident_id} - {self.title}"