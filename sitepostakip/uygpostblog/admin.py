from django.contrib import admin
from .models import Postlar
from .models import Profiller
from .models import Talepler
from .models import Mecralar
from .models import Musteriler
from .models import Görünümler

# Register your models here.

class PostlarAdmin(admin.ModelAdmin):
    list_display = ('id', 'Mecra', 'Profil', 'Post_Tarihi')

class ProfillerAdmin(admin.ModelAdmin):
    list_display = ('id', 'Mecra', 'Profil', 'Url', 'Link', 'Bas_Tarihi', 'Bit_Tarihi', 'Müşteri', 'Görünüm')
    # prepopulated ile Profil'e yazdığımız herşey aynı anda Slug'a da yazıyor.
    prepopulated_fields = {'Url': ('Profil',)}

class TaleplerAdmin(admin.ModelAdmin):
    list_display = ('id', 'Talep', 'Tal_Tarihi')

class MecralarAdmin(admin.ModelAdmin):
    list_display = ('id', 'Mecra')

class MusterilerAdmin(admin.ModelAdmin):
    list_display = ('id', 'Müşteri')

class GörünümlerAdmin(admin.ModelAdmin):
    list_display = ('id', 'Görünüm')


admin.site.register(Postlar,PostlarAdmin)
admin.site.register(Profiller,ProfillerAdmin)
admin.site.register(Talepler,TaleplerAdmin)
admin.site.register(Mecralar,MecralarAdmin)
admin.site.register(Musteriler,MusterilerAdmin)
admin.site.register(Görünümler,GörünümlerAdmin)