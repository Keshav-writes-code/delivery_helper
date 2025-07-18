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

class order_assign(models.Model):
    order_book_id = models.ForeignKey(customer_order,on_delete=models.CASCADE)
    assign_person_id = models.IntegerField(null=False,blank=False)


    def __str__(self):
        return f"{self.order_name} ({self.price}, {self.user_id},{self.delivery_person_id})"