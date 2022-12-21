from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.startingPage, name="startingPage"),
    path("posts/", views.posts, name="postPage"),
    path("posts/<slug:slug>", views.postDetail, name="postDetailPage"),
]