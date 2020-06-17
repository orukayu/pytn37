from django.shortcuts import render
from .models import Postlar

# APİ için eklemeler

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostlarSerializer

# Talep formu için eklemeler

from .forms import TalepFormu
from django.shortcuts import redirect

# Create your views here.

def hepsi(request):

    # Bu kısım Talepformunun kaydedilebilmesi için eklenmiştir.
    
    if request.method == "POST":
        form = TalepFormu(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/')
    else:

    # Buradan aşağısı postların ve talep formunun anasayfada gözükmesi içindir.

        posts = Postlar.objects.all()
        form = TalepFormu()
    return render(request, 'uygpostblog/hepsi.html', {'posts': posts, 'form': form})

# APİ için eklemeler

class PostlarListesi(APIView):
    def get(self, request):
        Listele = Postlar.objects.all()
        serializer = PostlarSerializer(Listele, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PostlarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# mecra sayfası için views tanımlama

def mecralar(request, mecra):
    if request.method == "POST":
        form = TalepFormu(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            redirect(end)
    else:
        posts = Postlar.objects.filter(mecra=mecra,)
        form = TalepFormu()
    return render(request, 'uygpostblog/mecra.html', {'posts': posts, 'form': form})

# profil sayfası için views tanımlama

def profiller(request, profil):
    if request.method == "POST":
        form = TalepFormu(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            redirect(end)
    else:
        posts = Postlar.objects.filter(profil=profil,)
        form = TalepFormu()
    return render(request, 'uygpostblog/profil.html', {'posts': posts, 'form': form})