from django.shortcuts import render
from .models import Postlar

# APİ için eklemeler

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostlarSerializer

# Create your views here.

def anasayfa(request):
    posts = Postlar.objects.all()
    return render(request, 'uygpostblog/anasayfa.html', {'posts': posts})

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
