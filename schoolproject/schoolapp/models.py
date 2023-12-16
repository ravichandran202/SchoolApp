from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BasicInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class StudentDetails(models.Model):
    user_id = models.IntegerField(blank = True, null=True)
    
    profile_image = models.ImageField(upload_to='media/profile',blank=True,null=True,default='default.jpg')
    
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    stu_class = models.IntegerField()
    date_of_birth = models.DateField( blank=True, null=True)
    gender = models.CharField(max_length=10,blank=True, null=True)
    
    # Address
    street = models.CharField(max_length=100, blank=True, null=True )
    city = models.CharField(max_length=50, blank=True, null=True )
    state = models.CharField(max_length=50, blank=True, null=True )
    zip_code = models.CharField(max_length=10, blank=True, null=True )
    
    # Contact Information
    phone_number = models.CharField(max_length=15, blank=True, null=True )
    email = models.EmailField(blank=True, null=True )

    # Parent/Guardian Information
    father_name = models.CharField(max_length=50, blank=True, null=True )
    father_contact = models.CharField(max_length=15, blank=True, null=True )
    mother_name = models.CharField(max_length=50, blank=True, null=True )
    mother_contact = models.CharField(max_length=15, blank=True, null=True )# Contact Information
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # Parent/Guardian Information
    father_name = models.CharField(max_length=50, blank=True, null=True)
    father_contact = models.CharField(max_length=15, blank=True, null=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    mother_contact = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return str(self.full_name)
    
class Announcement(BasicInfo):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/announcement',blank=True,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    announce_to = models.IntegerField(default=0)  # 0 - indicates For Everyone

    
    def __str__(self):
        return self.title
    
class Comment(BasicInfo):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    announcement_post = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.content[:15])
    