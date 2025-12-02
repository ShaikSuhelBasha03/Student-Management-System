from django.db import models
from django.utils import timezone
 

# Create your models here
class Student(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    join_date = models.DateField(default=timezone.now)
    address = models.CharField(max_length=255)
    about = models.TextField(max_length=200)

    def __str__(self):
        return self.name