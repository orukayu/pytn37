from django.db import models
from django.utils import timezone

# Create your models here.

class Postlar(models.Model):
    mecra = models.TextField()
    profil = models.TextField()
    embed = models.TextField()
    tarih = models.DateTimeField(
        default=timezone.now)

    class Meta:
        ordering = ['-tarih',]  # Kaydedilen Postlar'ın hangi başlığa göre sıralanacağını belirliyor

    def __str__(self):
        return self.mecra    # Kaydedilen Postlar'ın hangi başlığa göre sıralanacağını belirliyor

# Talep formu için model oluşturulur

class Talepler(models.Model):
    kullanici = models.TextField()
    tarih = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.kullanici

# Takip listesi için model oluşturulur

class Takipler(models.Model):
    mecra = models.TextField()
    profil = models.TextField()
    link = models.TextField()
    tarih = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.profil