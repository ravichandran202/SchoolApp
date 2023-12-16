from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("signin",views.signin,name="signin"),
    path("create-user",views.create_new_user,name="create-user"),
    path("logout",views.logout,name="logout"), #edit_profile
    path("edit/profile/<int:id>",views.edit_student_profile,name="edit-student-profile"),
    path("profile/<int:id>",views.profile_page,name="profile_page"),
    path("change-password",views.change_password,name="change_password"),
    path("create-announcement",views.create_announchment,name="create_announchment"),
    path("edit/announcement/<int:id>",views.edit_announchment,name="edit_announchment"),
    path("announcements",views.announcements,name="announchments"),
    path("announcement/<int:id>",views.announcement,name="announchment"),
    path("delete/comment/<int:id>",views.delete_comment,name="delete_comment")
]
