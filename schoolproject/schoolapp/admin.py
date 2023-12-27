from django.contrib import admin
from .models import StudentDetails,Announcement,Comment,Message,Test,TestMarks,UserQuery
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

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender','receiver','content')

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title','test_for')

@admin.register(TestMarks)
class TestMarksAdmin(admin.ModelAdmin):
    list_display = ('test_id','test_obj','student')

@admin.register(UserQuery)
class TestMarksAdmin(admin.ModelAdmin):
    list_display = ('username','email','phone')
