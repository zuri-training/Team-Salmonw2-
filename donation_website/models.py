from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AbstractBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


GENDER_CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
)

class Alumni(AbstractBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    course = models.CharField(max_length=255)
    graduation_year = models.DateField(null=True)
    student_id = models.CharField(max_length=255)

    def __init__(self):
        return self.name

class Student(AbstractBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name  = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name


class Payment(AbstractBaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

class Donation(AbstractBaseModel):
    alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date_donated = models.DateTimeField(null=True)

    def __str__(self):
        return self.alumni.name

class Donate(AbstractBaseModel):
    name = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_donated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
