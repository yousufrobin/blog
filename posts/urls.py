import imp
from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path("", views.index, name="home"),
    path("post/<str:post_id>", views.postviewer, name="postviewer"),
]
