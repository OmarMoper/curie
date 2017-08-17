from django.conf.urls import url
from rest_framework.compat import include
from rest_framework.routers import DefaultRouter

from rada.api import DispositivoViewSet, DispositivoEstado, EncenderLed, ApagarLed

router = DefaultRouter()
router.register(r'dispositivo', DispositivoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/dispositivo/(?P<nombre>[0-9a-zA-Z]+)/estado', DispositivoEstado.as_view()),
    url(r'^api/dispositivo/(?P<nombre>[0-9a-zA-Z]+)/on', EncenderLed.as_view()),
    url(r'^api/dispositivo/(?P<nombre>[0-9a-zA-Z]+)/off', ApagarLed.as_view())
]
