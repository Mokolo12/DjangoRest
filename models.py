from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
	@@ -21,6 +21,8 @@ class PersoneModel(AbstractBaseUser, PermissionsMixin):
    django model for validators
    """
    username_validator = ASCIIUsernameValidator()

    objects = UserManager()

    username = CharFieldCaseIgnore(
        _("username"),
	@@ -68,6 +70,13 @@ class PersoneModel(AbstractBaseUser, PermissionsMixin):
        editable=False
    )

    is_staff = models.BooleanField(
            default=False
            )
    is_active = models.BooleanField(
            default=False
            )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]