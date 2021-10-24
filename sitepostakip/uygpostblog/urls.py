from django.urls import path
from . import views
from .views import SearchResultsView

# postakiplogo.svg dosyası gibi sabit medyaların bütün sayfalarda çıkmasını sağlıyor.

from django.conf.urls.static import static


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
    path('aranan/', SearchResultsView.as_view(), name='aramasayfasi'),

]