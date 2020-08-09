from django import forms
from .models import Talepler

class TalepFormu(forms.ModelForm):

    class Meta:
        model = Talepler
        fields = ('talep',)
        labels = {"talep" : ""}
        widgets = {
        	'talep': forms.TextInput(attrs={'placeholder': 'youtube/güldürgüldür, instagram/@mosalah vb. önerilerini'}),
        }