from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from api.serializers import RegistrationSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def __get_token(user):
    token, created = Token.objects.get_or_create(user=user)
    return token.key


@api_view(["POST"])
@permission_classes([AllowAny])
def register_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            context = serializer.data
            context["token"] = __get_token(account)
            return Response(context, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([AllowAny])
def example_view(request):
    return Response({"Token":"token"})

@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data["username"]
    password = request.data["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        token = __get_token(user)
        return Response({"Token":token})
    else:
        return Response({"error": "unable to login"}, status=status.HTTP_400_BAD_REQUEST)
