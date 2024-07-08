
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="homepage"),
    path("edit/<int:id>", views.edit_album, name="edit_album"),
    path("delete/<int:id>", views.delete_album, name="delete_album"),
    path("",include("musician.urls")),
    path("",include("album.urls")),
    path("author/",include("author.urls")),
]
