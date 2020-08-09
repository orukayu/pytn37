from django.contrib import admin
from .models import Postlar
from .models import Takipler
from .models import Talepler
from .models import Mecralar

# Register your models here.

class PostlarAdmin(admin.ModelAdmin):
    list_display = ('id', 'mecra', 'profil', 'tarih')

class TakiplerAdmin(admin.ModelAdmin):
    list_display = ('id', 'mecra_id', 'profil', 'link', 'bas_tarihi')

class TaleplerAdmin(admin.ModelAdmin):
    list_display = ('id', 'talep', 'tal_tarihi')

class MecralarAdmin(admin.ModelAdmin):
    list_display = ('id', 'mecra')

admin.site.register(Postlar,PostlarAdmin)
admin.site.register(Takipler,TakiplerAdmin)
admin.site.register(Talepler,TaleplerAdmin)
admin.site.register(Mecralar,MecralarAdmin)