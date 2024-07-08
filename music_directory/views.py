from django.shortcuts import render,redirect 
from album.models import Album
from album.forms import AlbumForm
from django.contrib.auth.decorators import login_required

def home(request):
    data = Album.objects.all()
    return render(request , "home.html", {'data':data})

@login_required
def edit_album(request,id):
    album = Album.objects.get(pk=id)
    album_forms = AlbumForm(instance=album)
    if request.method == 'POST':
        album_forms = AlbumForm(request.POST, instance= album)
        if album_forms.is_valid():
            album_forms.save()
            return redirect('homepage')
    return render(request, 'add_album.html' , {'form':album_forms})

@login_required
def delete_album(request,id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('homepage')