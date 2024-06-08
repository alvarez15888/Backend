from django.shortcuts import render
from .models import Calculo

from .serializer import CalculoSerializer
from rest_framework import generics

class CalculoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Calculo.objects.all()
    serializer_class = CalculoSerializer

class CalculoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Calculo.objects.all()
    serializer_class = CalculoSerializer

class CalculoUpdateAPIView(generics.UpdateAPIView):
    queryset = Calculo.objects.all()
    serializer_class = CalculoSerializer
    def perform_update(self, serializer):
        instance = serializer.save()

class CalculoDestroyAPIView(generics.DestroyAPIView):
    queryset = Calculo.objects.all()
    serializer_class = CalculoSerializer
    def perform_destroy(self, instance):
        super().perform_destroy(instance)