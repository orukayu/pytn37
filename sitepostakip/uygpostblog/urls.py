from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSiteMap, MecralarSiteMap, ProfillerSiteMap

sitemaps = {
    'static':StaticSiteMap,
    'mecramaps':MecralarSiteMap,
    'profilmaps':ProfillerSiteMap
}

urlpatterns = [
    path('', views.hepsi, name='anasayfamiz'),

    # APİ için yüklemeler

    path('api/', views.PostlarListesi.as_view(), name='apisayfasi'),

    # mecra ve profil başlıklarına tıklayınca gidilecek sayfalar için

    path('mecra/<str:Mecra>/', views.mecralar, name='mecrasayfasi'),
    path('profil/<str:Profil>/', views.profiller, name='profilsayfasi'),
    path('post/<int:pk>/', views.postlar, name='postsayfasi'),

    # üstmenüde ki linklerin urlleri

    path('takiplistesi/', views.takiptekiler, name='takiplistesi'),
    path('taleplistesi/', views.taleptekiler, name='taleplistesi'),
    path('tesekkurlistesi/', views.tesekkurler, name='tesekkurlistesi'),

    # Takip sayfasında ki mecralara tıklayınca gidilecek sayfanın URL si

    path('takiplistesi/<str:Mecra>/', views.listeler, name='listesayfasi'),

    # URL ye yazıpta gitmeye çalışırsa

    path('mecra/', views.takiptekiler, name='mecra404'),
    path('profil/', views.takiptekiler, name='profil404'),
    path('post/', views.takiptekiler, name='paylas404'),

    # Deneme sayfası için url tayini

    path('d/', views.denemeler, name='denemesayfasi'),

    # Arama sayfası için url tayini

    path('aranan/', views.aramalar, name='aramasayfasi'),

    # Robots.txt dosyası için url tayini

    path("robots.txt", TemplateView.as_view(template_name="uygpostblog/robots.txt", content_type="text/plain")),

    # Sitemaps için url tayini

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]