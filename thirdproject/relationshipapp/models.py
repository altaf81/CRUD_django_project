from django.db import models

# one to one


class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.cust_id}-{self.cust_name}'


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cart_items = models.CharField(max_length=50)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cart_id}-{self.cart_items} {self.customer}'


# Many to one
class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dpt_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.dept_id}-{self.dpt_name}'


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.emp_id}-{self.emp_name} {self.department}'

# many to many


class Courses(models.Model):
    crs_id = models.AutoField(primary_key=True)
    crs_name = models.CharField(max_length=20)
    crs_fee = models.FloatField(max_length=60)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.crs_id}-{self.crs_name}'


class Students(models.Model):
    std_id = models.AutoField(primary_key=True)
    std_name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Courses)

    def __str__(self):
        return f'{self.std_id}-{self.std_name} {self.courses.all()}'
