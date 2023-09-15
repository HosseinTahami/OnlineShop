# Django Imports
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not email:
            raise ValueError("User should have Email")

        user = self.model(email=email, username=username)
        user.set_password(password)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
