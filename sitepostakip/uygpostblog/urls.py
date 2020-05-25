from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='Post Takip Anasayfası'),

    # APİ için yüklemeler

    path('api/', views.PostlarListesi.as_view())
]