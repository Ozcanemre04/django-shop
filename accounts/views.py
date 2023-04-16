
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index_view(request):
    # Just a test right here for homepage
    data = {"test": "hello world", "success": True}
    return Response(data)