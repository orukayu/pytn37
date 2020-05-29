from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='Post Takip Anasayfası'),

    # APİ için yüklemeler

    path('api/', views.PostlarListesi.as_view(), name='Api Sayfası'),

    # Talep Formunu anasayda dışında açıp kaydetmek için

    # path('form/', views.Talep, name='Form Sayfası'),

]