from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class student(models.Model):
    student_change = models.IntegerField(null=True)
    student_id = models.BooleanField(blank=True)
    // add some test cases
class UserManager(BaseUserManager):
    def create_user(self, user_id, email_id, password=None, **extra_fields):
        if not user_id:
            raise ValueError('The user_id must be set')
        if not email_id:
            raise ValueError('The Email must be set')
        email_id = self.normalize_email(email_id)

        user = self.model(user_id=user_id, email_id=email_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, email_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        extra_fields.setdefault('user_type', 1)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(user_id, email_id, password, **extra_fields)

class user_table(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(primary_key=True, max_length=50, unique=True)
    name = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True, max_length=50)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    user_type = models.IntegerField()
    partner_id = models.CharField(max_length=50, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email_id']

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'user_table'  # 👈 this overrides the default table name


    
class location_table(models.Model):
    owner_id = models.ForeignKey(user_table, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=100,null=False,blank=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,null=False,blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,null=False,blank=False)

    def __str__(self):
        return f"{self.location_name} ({self.latitude}, {self.longitude})"

class customer_order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(user_table,on_delete=models.CASCADE)
    order_name = models.TextField(null=False,blank=False)
    status = models.IntegerField(default=0)
    price = models.IntegerField(null=False,blank=False)
    date_of_delivery = models.DateField(null=False,blank=False)
    date_of_order = models.DateField(null=False,blank=False)
    def __str__(self):
        return f"{self.order_name} ({self.price}, {self.user_id},{self.delivery_person_id})"

class order_assign(models.Model):
    order_book_id = models.ForeignKey(customer_order,on_delete=models.CASCADE)
    assign_person_id = models.IntegerField(null=False,blank=False)

