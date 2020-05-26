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
        return self.profil    # Kaydedilen Postlar'ın hangi başlığa göre sıralanacağını belirliyor