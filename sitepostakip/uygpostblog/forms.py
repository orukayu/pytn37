from django import forms
from .models import Talepler

class TalepFormu(forms.ModelForm):

    class Meta:
        model = Talepler
        # fields olmadan kabul etmiyor
        fields = ('Talep',)
        # labels ile de text alanının başında ki Talep yazısını boşluk ile değiştirmiş oluyoruz
        labels = {"Talep" : ""}
        # widgets ile de placeholder olarak text kutusunun içinde ki metni yazıyoruz
        widgets = {
        	'Talep': forms.TextInput(attrs={'placeholder': 'youtube/güldürgüldür, instagram/@mosalah vb. profil önerilerini'}),
        }