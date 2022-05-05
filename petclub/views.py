# modulos de DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import ListAPIView

class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello, World !", status=200) # respuesta del serviciofrom django.shortcuts import render
  
