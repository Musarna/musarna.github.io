from django.shortcuts import render
from pruebaApp.models import Juguete
from django.http import JsonResponse
from pruebaAPI.serializers import JugueteSerializar
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def juguete_listado(request):
    if request.method == "GET":
        juguetes = Juguete.objects.all()
        serializer = JugueteSerializar(juguetes,many = True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = JugueteSerializar(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def juguete_detalle(request,pk):
    try:
        juguete = Juguete.objects.get(id=pk)
    except Juguete.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = JugueteSerializar(juguete)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = JugueteSerializar(juguete,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        juguete.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)




# Create your views here.
def juguetesApi(request):
    juguetes =  Juguete.objects.filter()
    data = {
        'juguetes':list(
            juguetes.values('id','nombre','descripcion','precio','codigoProducto')
        )
    }
    return JsonResponse(data)

