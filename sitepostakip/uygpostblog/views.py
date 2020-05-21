from django.shortcuts import render
from .models import Postlar
from django.utils import timezone

# Create your views here.

def anasayfa(request):
    posts = Postlar.objects.all()
    return render(request, 'uygpostblog/anasayfa.html', {'posts': posts})
