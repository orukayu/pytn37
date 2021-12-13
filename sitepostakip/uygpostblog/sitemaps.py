from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Mecralar
from .models import Profiller

class ProfillerSiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Profiller.objects.all()

    def location(self, obj):
        return reverse('profilsayfasi', args=[obj.pk, obj.Url])



class MecralarSiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Mecralar.objects.all()

    def location(self, obj: Mecralar) -> str:
        return reverse('mecrasayfasi', args=[obj.pk, obj.Mecra])
 


class StaticSiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return ['anasayfamiz', 'takiplistesi', 'taleplistesi', 'tesekkurlistesi']

    def location(self, item):
        return reverse(item)