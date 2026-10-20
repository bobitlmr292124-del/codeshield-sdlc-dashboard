
from django.test import TestCase
from django.urls import reverse
from .models import Incident


class IncidentModelTest(TestCase):
    def test_incident_can_be_created(self):
        incident = Incident.objects.create(
            incident_id="CS-TEST-001",
            title="Test Security Incident",
            description="Testing incident creation",
            pillar="CI/CD Pipeline",
            severity="High",
            status="Open",
        )

        self.assertEqual(incident.title, "Test Security Incident")
        self.assertEqual(Incident.objects.count(), 1)


class DashboardTest(TestCase):
    def test_dashboard_loads_successfully(self):
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)