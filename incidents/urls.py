
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),

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
