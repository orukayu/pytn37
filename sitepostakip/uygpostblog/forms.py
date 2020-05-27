from django import forms
from .models import Talepler
"""
class TalepFormu(forms.Form): 
      kullanici = forms.CharField(required=False, widget=forms.Textarea)
"""
class TalepFormu(forms.ModelForm):

    class Meta:
        model = Talepler
        fields = ('kullanici',)