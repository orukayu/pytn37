from django.contrib import admin
from .models import Postlar
from .models import Talepler

# Register your models here.

class PostlarAdmin(admin.ModelAdmin):
    list_display = ('id', 'mecra', 'profil', 'tarih')

class TaleplerAdmin(admin.ModelAdmin):
    list_display = ('tarih', 'kullanici')

admin.site.register(Postlar,PostlarAdmin)
admin.site.register(Talepler,TaleplerAdmin)