
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path(
        "incident/<int:pk>/edit/",
        views.edit_incident,
        name="edit_incident",
    ),
    path(
        "incident/<int:pk>/delete/",
        views.delete_incident,
        name="delete_incident",
    ),
]