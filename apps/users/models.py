

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from utils.uploads import upload_instance

# manager for our custom model
class UserManager(BaseUserManager):
    """
        This is a manager for Account class
    """

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an Emaill address")
        if not username:
            raise ValueError("Users must have an Username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
      Custom user class inheriting AbstractBaseUser class
    """

    first_name = models.CharField(verbose_name='Имя', max_length=250)
    last_name = models.CharField(verbose_name= 'Фамилия', max_length=250)
    phone_number = models.CharField(verbose_name='Phone #', max_length=20)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    avatar = models.ImageField (verbose_name='Picture', upload_to='upload_instance')

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

