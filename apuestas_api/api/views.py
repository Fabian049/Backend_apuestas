from django.shortcuts import render
from .models import Cuota, Ayer
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import json

from django.template import loader
from django.http import HttpResponse

#Rest Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CuotaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
          if (id > 0):
            cuotas = list(Cuota.objects.filter(id=id).values())
            if len(cuotas) > 0:
                cuota =  cuotas[0]
                datos = {'message': "Success", 'company': cuota}
            else:
                datos = {'message': "Company not found..."}
            return JsonResponse(datos)
          else:
            cuotas = list(Cuota.objects.values())
            if len(cuotas) > 0:
                datos = {'message': "Success", 'companies': cuotas}
            else:
                datos = {'message': "Companies not found..."}
            return JsonResponse(datos)


class AyerView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, id=0):
          if (id > 0):
            ayer = list(Ayer.objects.filter(id=id).values())
            if len(ayer) > 0:
                ayer1 =  ayer[0]
                datos = {'message': "Success", 'company': ayer1}
            else:
                datos = {'message': "Company not found..."}
            return JsonResponse(datos)
          else:
            ayer = list(Ayer.objects.values())
            if len(ayer) > 0:
                datos = {'message': "Success", 'companies': ayer}
            else:
                datos = {'message': "Companies not found..."}
            return JsonResponse(datos)