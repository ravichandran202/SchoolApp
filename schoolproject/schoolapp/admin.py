from django.contrib import admin
from .models import StudentDetails,Announcement
# Register your models here.

@admin.register(StudentDetails)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student','full_name', 'roll_no','stu_class')
    
@admin.register(Announcement)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('title','created_by')