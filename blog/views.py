from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import date

# Create your views here.
from blog.models import Post


def index(request):
    latest_posts = Post.objects.all().order_by("-published_on")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-last_updated")
    return render(request, "blog/posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, post_slug):
    identified_post = get_object_or_404(Post, slug=post_slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "tags": identified_post.tags.all()
    })
