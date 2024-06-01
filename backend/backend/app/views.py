from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *

# Create your views here.

class Reactview(APIView):
    def get(self, request):
        output = ''
