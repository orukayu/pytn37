from django.shortcuts import render
from .models import Postlar

# APİ için eklemeler

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostlarSerializer

# Talep formu için eklemeler

from .forms import TalepFormu

# Create your views here.

def anasayfa(request):
    posts = Postlar.objects.all()

    # Talep formunu anasayfada göstermek için form satırı ve return e bilgisi eklenir.

    form = TalepFormu()
    return render(request, 'uygpostblog/anasayfa.html', {'posts': posts, 'form': form})

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
"""
# Talep formunu başka bir sayfada göstermek için

def Talep(request):
    form = TalepFormu()
    return render(request,'uygpostblog/formsayfa.html',{'form': form})
"""