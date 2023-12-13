from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("signin",views.signin,name="signin"),
    path("create-user",views.create_new_user,name="create-user"),
    path("logout",views.logout,name="logout"), #edit_profile
    path("edit/profile/<int:id>",views.edit_student_profile,name="edit-student-profile"),
    path("change-password",views.change_password,name="change_password")
]
