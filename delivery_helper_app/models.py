from django.db import models
from django.contrib.auth.models import User, BaseUserManager


class user_types(models.Model):
    type_name = models.CharField(max_length=50, unique=True)
    partner_id_required = models.BooleanField(default=False)


class Profile(models.Model):
    auth_user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    user_type_id = models.ForeignKey(user_types, on_delete=models.CASCADE)
    partner_id = models.CharField(max_length=50, null=True, blank=True)


class location(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    location_name = models.CharField(unique=True, max_length=50)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=False, blank=False
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=False, blank=False
    )
    location_type = models.CharField(max_length=20, null=False, blank=False)
    city_level_address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.location_name} ({self.latitude}, {self.longitude})"


class customer_order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order_name = models.TextField(null=False, blank=False)
    order_location = models.ForeignKey(location, on_delete=models.CASCADE)
    is_delivered = models.BooleanField(default=False)
    price = models.IntegerField(null=False, blank=False)
    date_of_delivery = models.DateField(null=False, blank=False)
    date_of_order = models.DateField(null=False, blank=False)
    assigned_delivery_agent = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="delivery_orders"
    )

    def __str__(self):
        return f"{self.order_name} ({self.price}, {self.customer_id},{self.assigned_delivery_agent_id},{self.is_delivered})"


class UserManager(BaseUserManager):
    def create_user(self, user_id, email_id, password=None, **extra_fields):
        if not user_id:
            raise ValueError("The user_id must be set")
        if not email_id:
            raise ValueError("The Email must be set")
        email_id = self.normalize_email(email_id)

        user = self.model(user_id=user_id, email_id=email_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, email_id, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        extra_fields.setdefault("user_type", 1)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(user_id, email_id, password, **extra_fields)
