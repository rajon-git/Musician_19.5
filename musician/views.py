from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_musicians(request):
    if request.method == 'POST':
        musician_forms = forms.MusicianForm(request.POST)
        if musician_forms.is_valid():
            musician_forms.save()
            return redirect("add_musicians")
    else:
        musician_forms = forms.MusicianForm()

    return render(request,"add_musicians.html", {'form':musician_forms})

@login_required
def edit_musician(request,id):
    album = models.Musician.objects.get(pk=id)
    musician_forms = forms.MusicianForm(instance=album)
    if request.method == 'POST':
        musician_forms = forms.MusicianForm(request.POST, instance= album)
        if musician_forms.is_valid():
            musician_forms.save()
            return redirect('homepage')
    return render(request, 'add_musicians.html' , {'form':musician_forms})