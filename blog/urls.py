from django.urls.conf import path
from blog import views
from django.shortcuts import render

urlpatterns = [
    # API to post a comment
    path('postComment', views.postComment, name='postComment'),
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogpost, name='blogpost'),
]