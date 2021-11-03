from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError(_("Users must have an email address"))

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.staff = True
        user.admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    """
    Represents user model.

    Args:
        email (str): User's email address.
        user_id (str): Unique user's identifier.
        is_active (bool): Defines if user is active.
        staff (bool): Defines if user belongs to staff.
        admin (bool): Defines if user is an administrator.
    """

    objects = UserManager()

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    username = None
    email = models.EmailField(
        verbose_name=_("email address"),
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=32, verbose_name=_("first name"))
    last_name = models.CharField(max_length=64, verbose_name=_("last name"))
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name=_("is active"))
    staff = models.BooleanField(default=False, verbose_name=_("staff"))
    admin = models.BooleanField(default=False, verbose_name=_("administrator"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
