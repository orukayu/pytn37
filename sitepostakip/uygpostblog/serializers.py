from rest_framework import serializers
from .models import Postlar

class PostlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postlar
        # fields = ('alis','satis') // belirtilen kisimlari ceker.
        # fields = '__all__' // tum kisimlari ceker.
        fields = ('mecra','profil','embed')