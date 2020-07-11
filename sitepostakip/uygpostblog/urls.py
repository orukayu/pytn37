from django.urls import path
from . import views

# postakiplogo.svg dosyası gibi sabit medyaların bütün sayfalarda çıkmasını sağlıyor.

from django.conf.urls.static import static


urlpatterns = [
    path('', views.hepsi, name='anasayfamiz'),

    # APİ için yüklemeler

    path('api/', views.PostlarListesi.as_view(), name='apisayfasi'),

    # mecra ve profil başlıklarına tıklayınca gidilecek sayfalar için

    path('Mecra/<str:mecra>/', views.mecralar, name='mecrasayfasi'),
    path('Profil/<str:profil>/', views.profiller, name='profilsayfasi'),

    # üstmenüde ki linklerin urlleri

    path('TakipListesi/', views.takiptekiler, name='takiplistesi'),
    path('TalepListesi/', views.taleptekiler, name='taleplistesi'),
    path('TesekkurListesi/', views.tesekkurler, name='tesekkurlistesi'),

]