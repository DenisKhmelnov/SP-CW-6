from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager
from django.db import models
from users.managers import UserManager, UserRoles
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = PhoneNumberField( )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=UserRoles.choices)
    image = models.ImageField(null=True, blank=True, default=None, upload_to="avatars")
    is_active = models.BooleanField(default=True)

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    # Необходимые параметры для корректной работе Django

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    # также для работы модели пользователя должен быть переопределен
    # менеджер объектов
    objects = UserManager()
