from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime

# Create your models here.

class Postlar(models.Model):
    # Django tablo için ilk anahtarı otomatik oluşturur fakat illa biz tanımlamak istersek aşağıda ki gibi yapabiliriz.
    # PostID = models.AutoField(primary_key = True)
    Post = models.TextField()
    # ForeignKey oluştururken komut adı sadece tabloda ne şekilde yazacağını belirtir.
    Profil = models.ForeignKey('uygpostblog.Profiller', on_delete=models.CASCADE)
    Mecra = models.ForeignKey('uygpostblog.Mecralar', on_delete=models.CASCADE)
    Post_Tarihi = models.DateTimeField(
        default=timezone.now)

    class Meta:
        verbose_name_plural = "Postlar" # Admin sayfasında ki adını istediğimiz gibi koyabiliyoruz
        ordering = ['-Post_Tarihi',]  # Kaydedilen Postlar'ın hangi başlığa göre sıralanacağını belirliyor

    def __str__(self):
        return self.Post

# Takip listesi için model oluşturulur

class Profiller(models.Model):
    Mecra = models.ForeignKey('uygpostblog.Mecralar', on_delete=models.CASCADE)
    #İlk sırada olması form doldururken ilk seçeneğin bu olması için.
    Profil = models.TextField()
    Url = models.SlugField(null=False, unique=True)
    Link = models.TextField()
    Bas_Tarihi = models.DateTimeField(default=timezone.now)
    Bit_Tarihi = models.DateTimeField(default=datetime.datetime(2050, 1, 1))
    Müşteri = models.ForeignKey('uygpostblog.Musteriler', on_delete=models.CASCADE, default=2)
    Görünüm = models.ForeignKey('uygpostblog.Görünümler', on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['Profil',]  # Tablonun hangi başlığa göre sıralanacağını belirliyor
        verbose_name_plural = "Profiller" # Admin sayfasında ki adını istediğimiz gibi koyabiliyoruz

    def __str__(self):
        return self.Profil

# Talep formu için model oluşturulur

class Talepler(models.Model):
    Tal_Tarihi = models.DateTimeField(
        default=timezone.now)
    Talep = models.TextField()

    class Meta:
        verbose_name_plural = "Talepler" # Admin sayfasında ki adını istediğimiz gibi koyabiliyoruz
        ordering = ['-Tal_Tarihi',]  # Tablonun hangi başlığa göre sıralanacağını belirliyor

    def __str__(self):
        return self.Talep

# Mecralar formu için model oluşturulur, yukarıda olmasının nedeni Takipler modelinde Foreignkey kullandığım için

class Mecralar(models.Model):
    Mecra = models.TextField()

    class Meta:
        verbose_name_plural = "Mecralar" # Admin sayfasında ki adını istediğimiz gibi koyabiliyoruz

    def __str__(self):
        return self.Mecra


# Müşteriler tablosu oluşturma

class Musteriler(models.Model):
    Müşteri = models.TextField()

    class Meta:
        verbose_name_plural = "Müşteriler" # Admin sayfasında ki adını istediğimiz gibi koyabiliyoruz

    def __str__(self):
        return self.Müşteri


# Görünümler tablosu oluşturma

class Görünümler(models.Model):
    Görünüm = models.TextField()

    class Meta:
        verbose_name_plural = "Görünümler" # Admin sayfasında ki adını istediğimiz gibi koyabiliyoruz

    def __str__(self):
        return self.Görünüm