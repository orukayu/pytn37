from django.db import models
from django.utils import timezone

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
        ordering = ['-Post_Tarihi',]  # Kaydedilen Postlar'ın hangi başlığa göre sıralanacağını belirliyor

    def __str__(self):
        return self.Post

# Takip listesi için model oluşturulur

class Profiller(models.Model):
    Mecra = models.ForeignKey('uygpostblog.Mecralar', on_delete=models.CASCADE)
    #İlk sırada olması form doldururken ilk seçeneğin bu olması için.
    Profil = models.TextField()
    Link = models.TextField()
    Bas_Tarihi = models.DateTimeField(default=timezone.now)
    Bit_Tarihi = models.DateTimeField(default=0)
    Müşteri = models.ForeignKey('uygpostblog.Müşteriler', on_delete=models.CASCADE, default=2)
    Görünüm = models.ForeignKey('uygpostblog.Görünümler', on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['Profil',]  # Tablonun hangi başlığa göre sıralanacağını belirliyor

    def __str__(self):
        return self.Profil

# Talep formu için model oluşturulur

class Talepler(models.Model):
    Tal_Tarihi = models.DateTimeField(
        default=timezone.now)
    Talep = models.TextField()

    class Meta:
        ordering = ['-Tal_Tarihi',]  # Tablonun hangi başlığa göre sıralanacağını belirliyor

    def __str__(self):
        return self.Talep

# Mecralar formu için model oluşturulur, yukarıda olmasının nedeni Takipler modelinde Foreignkey kullandığım için

class Mecralar(models.Model):
    Mecra = models.TextField()

    def __str__(self):
        return self.Mecra


# Müşteriler tablosu oluşturma

class Müşteriler(models.Model):
    Müşteri = models.TextField()

    def __str__(self):
        return self.Müşteri


# Görünümler tablosu oluşturma

class Görünümler(models.Model):
    Görünüm = models.TextField()

    def __str__(self):
        return self.Görünüm