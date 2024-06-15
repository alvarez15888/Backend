from django.http import JsonResponse
from lost_found.models import Lost, Found
from rest_framework.decorators import api_view
from rest_framework.response import Response
from lost_found.serializer import LostSerializer

@api_view(['GET'])
def api_home(request, *arg, **kwargs):
    instance = Lost.objects.all().order_by('?').first()

    ldata = {}

    if instance:
        ldata = LostSerializer(instance).data

    return JsonResponse(ldata)

# Create your views here.
