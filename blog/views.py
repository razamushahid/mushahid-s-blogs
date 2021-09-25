from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from datetime import date

from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.
from blog.forms import CommentForm
from blog.models import Post, Comment

"""
======================
Class based View
======================
"""

# class IndexView(TemplateView):
#     template_name = "blog/index.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         latest_posts = Post.objects.all().order_by("-published_on")[:3]
#         context["posts"] = latest_posts
#         return context


class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-last_updated", "-published_on"]
    context_object_name = "posts"

    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data


class PostListView(ListView):
    template_name = "blog/posts.html"
    model = Post
    context_object_name = "all_posts"
    ordering = ["-last_updated", "-published_on"]

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["all_posts"] = Post.objects.all().order_by("-last_updated")
    #     return context


class PostDetailView(View):

    def is_saved_posts(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts:
            is_saved = post_id in stored_posts
        else:
            is_saved = False
        return is_saved

    def _get_context(self, post, comment_form, is_saved):
        return {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by('-pk'),
            "display_read_later": not is_saved
        }

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = self._get_context(post, CommentForm(), self.is_saved_posts(request, post.id))
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail", args=[slug]))
        context = self._get_context(post, comment_form, self.is_saved_posts(request, post.id))
        return render(request, "blog/post-detail.html", context)


class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if not stored_posts:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")
        post_id = int(request.POST["post_id"])
        if stored_posts is None:
            stored_posts = []
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")



    # model = Post
    # template_name = "blog/post-detail.html"
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tags'] = self.object.tags.all()
    #     context["comment_form"] = CommentForm()
    #     return context






"""
=======================
Function based Views
=======================

"""
# def index(request):
#     latest_posts = Post.objects.all().order_by("-published_on")[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })
#
#
# def posts(request):
#     all_posts = Post.objects.all().order_by("-last_updated")
#     return render(request, "blog/posts.html", {
#         "all_posts": all_posts
#     })
#
#
# def post_detail(request, post_slug):
#     identified_post = get_object_or_404(Post, slug=post_slug)
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post,
#         "tags": identified_post.tags.all()
#     })
