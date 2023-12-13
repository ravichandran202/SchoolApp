from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StudentDetails(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    stu_class = models.IntegerField()
    
    def __str__(self):
        return str(self.full_name)
    