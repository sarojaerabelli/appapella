from django.shortcuts import render

# Create your views here.
from backend.models import Recorder
from backend.serializers import RecorderSerializer
from rest_framework import generics

class RecorderListCreate(generics.ListCreateAPIView):
    queryset = Recorder.objects.all()
    serializer_class = RecorderSerializer