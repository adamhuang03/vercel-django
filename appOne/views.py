from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def say_hi(request):
    return Response({'Error': 'Cannot execute function.'}, status=status.HTTP_200_OK)