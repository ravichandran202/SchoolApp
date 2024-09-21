from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("signin",views.signin,name="signin"),
    path("create-user",views.create_new_user,name="create-user"),
    path("create-teacher",views.create_new_teacher,name="create-teacher"),
    path("logout",views.logout,name="logout"), #edit_profile
    path("edit/profile/<int:id>",views.edit_student_profile,name="edit-student-profile"),
    path("profile/<int:id>",views.profile_page,name="profile_page"),
    path("change-password",views.change_password,name="change_password"),
    path("create-announcement",views.create_announchment,name="create_announchment"),
    path("edit/announcement/<int:id>",views.edit_announchment,name="edit_announchment"),
    path("announcements",views.announcements,name="announchments"),
    path("announcement/<int:id>",views.announcement,name="announchment"),
    path("delete/comment/<int:id>",views.delete_comment,name="delete_comment"),
    path("chat/<int:id>",views.chat_page,name="chat"),
    path("chat/",views.chat,name="chat_list"),
    path("users-list",views.users_list,name="users_list"),
    path("create-test",views.create_test,name="create_test"),
    path("display-tests",views.display_tests,name="display_tests"),
    path("delete-test/<int:id>",views.delete_test,name="delete_test"),
    path("upload-marks/<int:id>",views.upload_marks,name="upload_marks"),
    path("update-marks/<int:id>",views.update_marks,name="update_marks"),
    path("student-display-tests",views.student_display_tests,name="student_display_tests"),
    path("marks-card/<int:id>",views.marks_card,name="marks_card"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
