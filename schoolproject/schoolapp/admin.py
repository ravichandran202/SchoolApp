from django.contrib import admin
from .models import StudentDetails,Announcement,Comment
# Register your models here.

@admin.register(StudentDetails)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student','full_name', 'roll_no','stu_class')
    
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title','created_by')
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('created_by','content','announcement_post')