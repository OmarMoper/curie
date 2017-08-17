from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from rada.models import Dispositivo
from rada.serializer import DispositivoSerializer
from django.core import serializers

import RPi.GPIO as GPIO


import json

class DispositivoViewSet(ModelViewSet):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer

class DispositivoEstado(APIView):
    def get(self, request, nombre):
        dispositivo = Dispositivo.objects.get(nombre=nombre)
        serializer = DispositivoSerializer(dispositivo)
        return Response(serializer.data)

class EncenderLed(APIView):
    def get(self, request, nombre):
        dispositivo = Dispositivo.objects.get(nombre=nombre)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(dispositivo.puerto, GPIO.OUT)
        GPIO.output(dispositivo.puerto, True)
        return Response(dispositivo.puerto)


class ApagarLed(APIView):
    def get(self, request, nombre):
        dispositivo = Dispositivo.objects.get(nombre=nombre)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(dispositivo.puerto, GPIO.OUT)
        GPIO.output(dispositivo.puerto, False)
        return Response(dispositivo.puerto)
