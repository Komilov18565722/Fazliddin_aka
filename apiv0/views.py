from django.shortcuts import render
from apiv0.serializer import MySerializer
from myapp.models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework import generics
from myapp.models import MyBase

# Create your views here.


class CreateList(generics.ListCreateAPIView):
    queryset = MyBase.objects.all()
    serializer_class = MySerializer


class UpdateList(generics.UpdateAPIView):
    serializer_class = MySerializer

    def get_object(self):
        return MyBase.objects.get(id = self.request.data.get('id'))


class DeleteList(generics.DestroyAPIView):
    serializer_class = MySerializer
    
    def get_object(self):
        return MyBase.objects.get(pk = self.request.data.get('id'))