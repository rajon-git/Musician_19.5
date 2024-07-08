from django import forms 
from . import models
from django.forms import SelectDateWidget 

class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = "__all__"
    
    release_date = forms.DateField(
    widget=SelectDateWidget(),
    label="Assign Date",
    help_text="Please select the assign date"
    )