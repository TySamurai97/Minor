from django.shortcuts import render

# Create your views here.from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status
from cp.models import UserData
from cp.models import CodeChef
from cp.models import UserHandler
from cp.models import Questions
from cp.models import Spoj
from cp.models import CodeForces
from cp.serializers import CodeChefSerializer
from cp.serializers import UserSerializer
from cp.serializers import SpojSerializer
from cp.serializers import CodeForcesSerializer
from cp.serializers import UserHandlerSerializer
from cp.serializers import QuestionsSerializer



