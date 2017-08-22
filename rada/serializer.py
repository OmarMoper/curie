from rest_framework import serializers

from rada.models import Dispositivo


class DispositivoSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        absolute_url = self.context['request'].build_absolute_uri('/')[:-1].strip("/")
        return absolute_url + "/api/dispositivo/" + obj.nombre

    class Meta:
        model = Dispositivo
        fields = '__all__'
