# modulos de DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import ListAPIView

class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello, World !", status=200) # respuesta del serviciofrom django.shortcuts import render
class PetAPIView(APIView):
    def get(self, request):
        return Response(data="esto es un get", status=200) 
    def post(self, request):
        return Response(data="esto es un post", status=200) 
    def patch(self, request):
        return Response(data="esto es un patch", status=200) 
    def delete(self, request):
        return Response(data="esto es un delete", status=200)  
class PersonAPIView(APIView):
    def get(self, request):
        return Response(data="esto es un get", status=200) 
    def post(self, request):
        return Response(data="esto es un post", status=200)       
    def patch(self, request):
        return Response(data="esto es un patch", status=200) 
    def delete(self, request):
        return Response(data="esto es un delete", status=200)  
