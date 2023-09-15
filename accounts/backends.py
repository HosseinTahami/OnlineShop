# Django Imports
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

# RestFrameWork Imports
from rest_framework.authentication import BaseAuthentication
from rest_framework.response import Response
from rest_framework import exceptions

# Inside Project Imports
from .models import CustomUser

# Other Imports
import jwt
import os


secret_key = os.getenv("SECRET_KEY", "not-a-very-secret-key")


class CustomAuthentication(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = CustomUser.objects.get(email=username)
        except CustomUser.DoesNotExist:
            try:
                user = CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
                raise exceptions.NotFound("User Not Found")

        if user.check_password(password):
            return user
        return None
        """
        try:
            payload = jwt.decode(token, secret_key, algorithms=["HS256"])
            user_id = payload["id"]
            user = CustomUser.objects.get(pk=user_id)
            return user

        except (jwt.DecodeError, CustomUser.DoesNotExist):
            return None
        """

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
