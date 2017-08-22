from rest_framework import serializers

from rada.models import Dispositivo


class DispositivoSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return "api/dispositivo/" + obj.nombre + "/%i" % obj.puerto

    class Meta:
        model = Dispositivo
        fields = '__all__'
