from django import forms
from django.forms import SelectDateWidget 
from . import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"