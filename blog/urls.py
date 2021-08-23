from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('posts', views.posts, name="posts"),
    path('posts/<slug:post_slug>', views.post_detail, name="post-detail")  # posts/my-first-post
]
