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
        return self.mecra

# Takip listesi için model oluşturulur

class Takipler(models.Model):
    mecra = models.ForeignKey('uygpostblog.Mecralar', on_delete=models.CASCADE)
    #Tabloya mecra_id adında bağlantılı sütun ekler bu yüzden adının mecra olması şart.
    #İlk sırada olmasıda form doldururken ilk seçeneğin bu olması için.
    #Mecralar modeli aşağıda kaldığı için yolu '' işaretleri arasında gösterdim.
    profil = models.TextField()
    link = models.TextField()
    bas_tarihi = models.DateTimeField(
        default=timezone.now)

    class Meta:
        ordering = ['id',]  # Tablonun hangi başlığa göre sıralanacağını belirliyor

    def __str__(self):
        return self.profil

# Talep formu için model oluşturulur

class Talepler(models.Model):
    talep = models.TextField()
    tal_tarihi = models.DateTimeField(
        default=timezone.now)

    class Meta:
        ordering = ['talep',]  # Tablonun hangi başlığa göre sıralanacağını belirliyor

    def __str__(self):
        return self.talep

# Mecralar formu için model oluşturulur, yukarıda olmasının nedeni Takipler modelinde Foreignkey kullandığım için

class Mecralar(models.Model):
    mecra = models.TextField()

    class Meta:
        ordering = ['id',]  # Tablonun hangi başlığa göre sıralanacağını belirliyor

    def __str__(self):
        return self.mecra

