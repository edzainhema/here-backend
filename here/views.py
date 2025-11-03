from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

@api_view(['GET'])
@permission_classes([AllowAny]) 
def hello_world(request):
	if request.user.is_authenticated:
		message = f"Hello {request.user.username}, how are you doing?"
	else:
		message = "Hello stranger, how are you doing?"
	
	return Response({"message": message})
# Create your views here.
