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
        ordering = ['-tarih',]

    def __str__(self):
        return self.mecra    # Kaydedilen Postlar'ın hangi başlığa göre sıralanacağını belirliyor

# Talep formu için model oluşturulur

class Talepler(models.Model):
    kullanici = models.TextField()

    def __str__(self):
        return self.kullanici
