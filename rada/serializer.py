from rest_framework import serializers

from rada.models import Dispositivo


class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'