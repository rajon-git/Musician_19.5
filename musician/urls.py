
from django.urls import path
from . import views

urlpatterns = [
    path("add_musician/",views.add_musicians, name="add_musicians"),
    path("edit-musician/<int:id>", views.edit_musician, name="edit_musician"),
]
