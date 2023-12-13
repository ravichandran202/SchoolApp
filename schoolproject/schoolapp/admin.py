from django.contrib import admin
from .models import StudentDetails
# Register your models here.

@admin.register(StudentDetails)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student','full_name', 'roll_no','stu_class')