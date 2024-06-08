from django.http import JsonResponse
from calculadora.models import Calculo
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from calculadora.serializer import CalculoSerializer


@api_view(['GET'])
def api_home(request, *arg, **kwargs):
    instance = Calculo.objects.all().order_by('?').first()
    data = {}

    if instance:
        data = CalculoSerializer(instance).data

    return JsonResponse(data)