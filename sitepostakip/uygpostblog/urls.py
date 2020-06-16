from django.urls import path
from . import views

urlpatterns = [
    path('', views.hepsi, name='anasayfamiz'),

    # APİ için yüklemeler

    path('api/', views.PostlarListesi.as_view(), name='apisayfasi'),

    # Talep Formunu anasayda dışında açıp kaydetmek için

    # path('form/', views.Talep, name='Form Sayfası'),

    # mecra başlıklarına tıklayınca gidilecek sayfa

    path('Mecra/<str:mecra>/', views.mecralar, name='mecrasayfasi'),

]