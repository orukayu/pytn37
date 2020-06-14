from django.contrib import admin
from .models import Postlar

# Register your models here.

class PostlarAdmin(admin.ModelAdmin):
    list_display = ('id', 'mecra', 'profil', 'tarih')

admin.site.register(Postlar,PostlarAdmin)