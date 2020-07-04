from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from django.http import Http404
from django.shortcuts import get_object_or_404


#Importanciones de modelos
from Example1.models import Example1

#Importancion de serializer
from Example1.serializer import Example1Serializers


class ExampleList(APIView):
    def get(self, request, format=None):
        print("GET")
        queryset = Example1.objects.all()
        serializer = Example1Serializers(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Example1Serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        else:
            return Response("Hay datos que superan el limite o hay datos que son faltantes")

class ExampleDetail(APIView):
    def get_object(self, id):
        try:
            return Example1.objects.get(pk = id)
        except Example1.DoesNotExist:
            return 404


    def get(self, request, id, format=None):
        print("GET Detail")
        example = self.get_object(id)
        if example == 404:
            return Response("No existen datos")
        else:
            serializer = Example1Serializers(example)
            return Response(serializer.data)


    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        serializer = Example1Serializers(example, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        else:
            return Response(serializers.errors)