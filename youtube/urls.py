from django.urls import path, include
from .views import *

urlpatterns = [
    path("", registration, name="registration"),
    path("login/", login_user, name="login"),
    path('create_video', create_video, name="create_video"),
]