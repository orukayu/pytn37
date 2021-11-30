from django.shortcuts import render
from .models import Postlar
from .models import Profiller
from .models import Talepler
from .models import Mecralar
from .models import Musteriler
from .models import Görünümler

# APİ için eklemeler

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostlarSerializer

# Talep formu için eklemeler

from .forms import TalepFormu
from django.shortcuts import redirect

# Tarih için eklemeler

import datetime

# Arama formu için eklemeler

from django.db.models import Q



# Ana sayfada yani Tüm Postlar sayfasının görünüm kodları,
# Sadece Görünümleri Açık olan ve Bitiş Tarihleri geçmemiş profillerin postları listelenir.

def hepsi(request):
    # şimdiki zamanı tanımlamak için zmn
    zmn = datetime.datetime.now()
    # Profiller tablosunda Görünümü 1 (Açık) olanlar ile Bitiş Tarihleri geçmemiş olanların id sinin listesi
    acik = Profiller.objects.values_list('id', flat=True).filter(Görünüm=1, Bit_Tarihi__gte=zmn)
    # Profil__in komutu ile liste olarak gelen id leri Postlar tablosunda filitrele
    posts = Postlar.objects.filter(Profil__in=acik)
    prof = Profiller.objects.all()
    return render(request, 'uygpostblog/hepsi.html', {'posts': posts, 'prof':prof})

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

def mecralar(request, PK, MECRA):
    mecraadi = MECRA

    numara = Mecralar.objects.filter(Mecra=mecraadi).get()
    posts = Postlar.objects.filter(Mecra=numara)
    prof = Profiller.objects.all()
    return render(request, 'uygpostblog/mecra.html', {'posts': posts, 'mecraadi':mecraadi, 'prof':prof})

# profil sayfası için views tanımlama

def profiller(request, PK, PROFIL):
    profiladi = PROFIL

    numara = Profiller.objects.filter(Url=profiladi).get()
    posts = Postlar.objects.filter(Profil=numara)

    return render(request, 'uygpostblog/profil.html', {'posts': posts, 'numara':numara})

# Post paylaşım sayfası için views tanımlama

def postlar(request, PK):
    postno = PK
    posts = Postlar.objects.filter(pk=PK)
    prof = Profiller.objects.all()   
    return render(request, 'uygpostblog/paylas.html', {'posts': posts, 'postno': postno, 'prof': prof})

# Takip Listesi için görünüm kodları

def takiptekiler(request):
    mec = Mecralar.objects.values('Mecra').order_by('Mecra').distinct()
    sonkayit = Profiller.objects.values('Bas_Tarihi').order_by('Bas_Tarihi').last()['Bas_Tarihi']
    sonuncu = (sonkayit.strftime("%d.%m.%Y"))

    # Şimdi ki tarihi yazdırmak için kullanılan kodlar. Sayfa da {{ tarih }} etiketi ile kullanılabilinir.
    # x = datetime.datetime.now()
    # tarih = (x.strftime("%d.%m.%Y"))

    args = {'mec': mec, 'sonuncu': sonuncu}
    return render(request, 'uygpostblog/takip.html', args)

# Takip sayfasında ki mecra ismine basınca, o mecraya ait listenin gösterileceği sayfa fonksiyonu

def listeler(request, MECRA):
    baslik = MECRA

    numara = Mecralar.objects.filter(Mecra=baslik).get()
    lis = Profiller.objects.filter(Mecra=numara).order_by('Profil').distinct()

    # mec, sonkayit ve sonuncu formülleri takip sayfasının altında çıkmasından ötürü bulunmak zorunda
    mec = Mecralar.objects.values('Mecra').order_by('Mecra').distinct() 
    sonkayit = Profiller.objects.values('Bas_Tarihi').order_by('Bas_Tarihi').last()['Bas_Tarihi']
    sonuncu = (sonkayit.strftime("%d.%m.%Y"))

    args = {'baslik':baslik, 'lis': lis, 'mec':mec, 'sonuncu': sonuncu}
    return render(request, 'uygpostblog/listeler.html', args)

# Talep edilenler ve yeni profil talepleri için Talep Listesi sayfasının görünümü

def taleptekiler(request):
    # if ile else arasında ki komutlar talep formunun çalışması içindir.
    if request.method == "POST":
        form = TalepFormu(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('taleplistesi')
    else:
        form = TalepFormu()
        kast = Talepler.objects.order_by('Talep')
    return render(request, 'uygpostblog/talep.html', {'form': form, 'kast': kast})

# Teşekkürler sayfası için görünüm kodları

def tesekkurler(request):
    return render(request, 'uygpostblog/tesekkur.html', {})

# 404 sayfası için ekleme, diğer eklemeler uygulamanın değil proje urls.py dosyasında

def kiriklink(request, exception):
    return render(request,'uygpostblog/404.html', {})

# 500 sayfası için ekleme, diğer eklemeler uygulamanın değil proje urls.py dosyasında

def hatalikomut(request, exception=None):
    return render(request,'uygpostblog/500.html', {})


# deneme sayfasının görünüm kodları

def denemeler1(request):
    # şimdiki zamanı tanımlamak için zmn
    zmn = datetime.datetime.now()
    # Profiller tablosunda Görünümü 1 (Açık) olanlar ile Bitiş Tarihleri geçmemiş olanların id sinin listesi
    acik = Profiller.objects.values_list('id', flat=True).filter(Görünüm=1, Bit_Tarihi__gte=zmn)
    # Profil__in komutu ile liste olarak gelen id leri Postlar tablosunda filitrele
    posts = Postlar.objects.filter(Profil__in=acik)
    aydi = Profiller.objects.all()
    return render(request, 'uygpostblog/deneme1.html', {'posts': posts, 'aydi': aydi})

def denemeler2(request, PK, PROFIL):
    return render(request,'uygpostblog/deneme2.html', {})

# Arama formu için arama sayfasının görünüm kodları

def aramalar(request):
    metin = request.GET.get('kelime')
    if metin:
        queryset = (Q(Profil__icontains=metin))
        sonuc = Profiller.objects.filter(queryset).distinct()
    else:

        sonuc = []
    return render(request, 'uygpostblog/arama.html', {'sonuc':sonuc, 'metin':metin})

