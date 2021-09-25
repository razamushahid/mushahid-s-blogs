from django.urls import path

from . import views


# urlpatterns = [
#     path('', views.index, name="home"),
#     path('posts', views.posts, name="posts"),
#     path('posts/<slug:post_slug>', views.post_detail, name="post-detail")  # posts/my-first-post
# ]


urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('posts', views.PostListView.as_view(), name="posts"),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name="post-detail"),
    path('read-later-posts', views.ReadLaterView.as_view(), name="read-later-posts")
]
