from django import forms
from .models import Talepler

class TalepFormu(forms.ModelForm):

    class Meta:
        model = Talepler
        fields = ('Talep',)
        labels = {"Talep" : ""}
        widgets = {
        	'Talep': forms.TextInput(attrs={'placeholder': 'youtube/güldürgüldür, instagram/@mosalah vb. profil önerilerini'}),
        }