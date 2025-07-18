from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()

    def __str__(self):
        return self.name
class UserManager(BaseUserManager):
    def create_user(self, user_id, email_id, password=None, **extra_fields):
        if not email_id:
            raise ValueError("Email is required")
        email_id = self.normalize_email(email_id)
        user = self.model(user_id=user_id, email_id=email_id, **extra_fields)
        user.set_password(password)  # hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, email_id, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(user_id, email_id, password, **extra_fields)

class user_table(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(primary_key=True, max_length=50, unique=True)
    name = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True, max_length=50)
    phone_number = models.CharField(max_length=15)
    partner_id = models.CharField(max_length=50, null=True, blank=True)
    user_type = models.IntegerField()  # Add user_type field

    # Inherited password field from AbstractBaseUser
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email_id']

    def __str__(self):
        return self.name
