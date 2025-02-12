from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Puedes agregar campos adicionales si es necesario
    pass

