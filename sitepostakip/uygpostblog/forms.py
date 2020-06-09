from django import forms
from .models import Talepler

class TalepFormu(forms.ModelForm):

    class Meta:
        model = Talepler
        fields = ('kullanici',)
        labels = {"kullanici" : ""}
        widgets = {
        	'kullanici': forms.TextInput(attrs={'placeholder': 'youtube/güldürgüldür, instagram/@mosalah vb.'}),
        }