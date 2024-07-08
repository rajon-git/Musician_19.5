from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def add_album(request):
    if request.method == 'POST':
        album_forms = forms.AlbumForm(request.POST)
        if album_forms.is_valid():
            album_forms.save()
            return redirect("add_album")
    else:
        album_forms = forms.AlbumForm()

    return render(request,"add_album.html", {'form':album_forms})