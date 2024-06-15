from rest_framework import viewsets, mixins

from .models import Lost, Found
from .serializer import LostSerializer, FoundSerializer

class LostViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Lost.objects.all()
    serializer_class = LostSerializer
    lookup_field = 'pk'

class FoundViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Found.objects.all()
    serializer_class = FoundSerializer
    lookup_field = 'pk'