from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator

class CustomUser(User):
    username_validator = ASCIIUsernameValidator()
    first_name = User.first_name
    last_name = User.last_name
    def __str__(self):
        print('this',self.get_full_name)
        return self.get_full_name
