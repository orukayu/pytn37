from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.anasayfa, name='Post Takip Anasayfası'),

    # APİ için yüklemeler

    path('api/', views.PostlarListesi.as_view())
]