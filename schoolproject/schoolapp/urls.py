from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("signin",views.signin,name="signin"),
    path("create-user",views.create_new_user,name="createuser")
]
