
from django.contrib import admin
from .models import Incident


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = (
        "incident_id",
        "title",
        "pillar",
        "severity",
        "status",
        "created_at",
    )

    list_filter = ("pillar", "severity", "status")
    search_fields = ("incident_id", "title", "description")