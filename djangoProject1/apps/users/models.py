from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('An Email Address is required.')
        if not username:
            raise ValueError('A Username is required.')
        # if not first_name:
        #     raise ValueError('Firstname is required')
        # if not last_name:
        #     raise ValueError('Lastname is required')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            # first_name=first_name,
            # last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        if password is None:
            raise TypeError('Password is required for SuperUser.')

        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_verified = True
        user.save()

        return user


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='email address', unique=True, max_length=255, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.username

    class Meta:
        db_table = 'auth_user'


