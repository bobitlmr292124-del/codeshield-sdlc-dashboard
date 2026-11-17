
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import Incident
from .forms import IncidentForm, RegistrationForm


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = RegistrationForm()

    return render(request, "incidents/register.html", {"form": form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()

    return render(request, "incidents/login.html", {"form": form})


@login_required
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")

    return redirect("dashboard")


@login_required
def dashboard(request):
    if request.method == "POST":
        form = IncidentForm(request.POST)

        if form.is_valid():
            incident = form.save(commit=False)
            incident.owner = request.user
            incident.save()
            return redirect("dashboard")
    else:
        form = IncidentForm()

    incidents = Incident.objects.filter(
        owner=request.user
    ).order_by("-created_at")

    severity_data = list(
        incidents.values("severity").annotate(total=Count("pk"))
    )
    status_data = list(
        incidents.values("status").annotate(total=Count("pk"))
    )
    pillar_data = list(
        incidents.values("pillar").annotate(total=Count("pk"))
    )

    context = {
        "incidents": incidents,
        "form": form,
        "total_incidents": incidents.count(),
        "open_incidents": incidents.filter(status="Open").count(),
        "critical_incidents": incidents.filter(severity="Critical").count(),
        "resolved_incidents": incidents.filter(status="Resolved").count(),

        "severity_labels": [
            item["severity"] for item in severity_data
        ],
        "severity_values": [
            item["total"] for item in severity_data
        ],

        "status_labels": [
            item["status"] for item in status_data
        ],
        "status_values": [
            item["total"] for item in status_data
        ],

        "pillar_labels": [
            item["pillar"] for item in pillar_data
        ],
        "pillar_values": [
            item["total"] for item in pillar_data
        ],
    }

    return render(request, "incidents/dashboard.html", context)


@login_required
def edit_incident(request, pk):
    incident = get_object_or_404(
        Incident, pk=pk, owner=request.user
    )

    if request.method == "POST":
        form = IncidentForm(request.POST, instance=incident)

        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = IncidentForm(instance=incident)

    return render(
        request,
        "incidents/edit_incident.html",
        {
            "form": form,
            "incident": incident,
        },
    )


@login_required
def delete_incident(request, pk):
    incident = get_object_or_404(
        Incident, pk=pk, owner=request.user
    )

    if request.method == "POST":
        incident.delete()
        return redirect("dashboard")

    return render(
        request,
        "incidents/delete_incident.html",
        {"incident": incident},
    )
