from django.shortcuts import render
from .models import Lost, Found
from .serializer import LostSerializer, FoundSerializer
from rest_framework import generics

class LostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lost.objects.all()
    serializer_class = LostSerializer

class LostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lost.objects.all()
    serializer_class = LostSerializer

class LostUpdateAPIView(generics.UpdateAPIView):
    queryset = Lost.objects.all()
    serializer_class = LostSerializer
    def perform_update(self, serializer):
        instance = serializer.save()

class LostDestroyAPIView(generics.DestroyAPIView):
    queryset = Lost.objects.all()
    serializer_class = LostSerializer
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

class FoundRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Found.objects.all()
    serializer_class = FoundSerializer

class FoundListCreateAPIView(generics.ListCreateAPIView):
    queryset = Found.objects.all()
    serializer_class = FoundSerializer

class FoundUpdateAPIView(generics.UpdateAPIView):
    queryset = Found.objects.all()
    serializer_class = FoundSerializer
    def perform_update(self, serializer):
        instance = serializer.save()

class FoundDestroyAPIView(generics.DestroyAPIView):
    queryset = Found.objects.all()
    serializer_class = FoundSerializer
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
