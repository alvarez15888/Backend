from django.shortcuts import render
from .models import Lost, Found
from .serializer import LostSerializer, FoundSerializer
from rest_framework import generics, permissions, authentication

class LostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lost.objects.all()
    serializer_class = LostSerializer

# Ver y crear
class LostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lost.objects.all()
    serializer_class = LostSerializer

class LostUpdateAPIView(generics.UpdateAPIView):
    queryset = Lost.objects.all()
    serializer_class = LostSerializer
    def perform_update(self, serializer):
        instance = serializer.save()
    # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    # permission_classes = [permissions.DjangoModelPermissions]

class LostDestroyAPIView(generics.DestroyAPIView):
    queryset = Lost.objects.all()
    serializer_class = LostSerializer
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
    # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    # permission_classes = [permissions.DjangoModelPermissions]

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
    # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    # permission_classes = [permissions.DjangoModelPermissions]

class FoundDestroyAPIView(generics.DestroyAPIView):
    queryset = Found.objects.all()
    serializer_class = FoundSerializer
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
    # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    # permission_classes = [permissions.DjangoModelPermissions]
