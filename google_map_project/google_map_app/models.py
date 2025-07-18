from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()

    def __str__(self):
        return self.name
class user_table(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True, max_length=50)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    user_type = models.IntegerField()
    partner_id = models.CharField(max_length=50, null= True)
    def __str__(self):
        return self.name
