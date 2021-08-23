from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [{
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "Mushahid Raza",
    "published_on": date(2021, 8, 23),
    "title": "Mountain Hiking",
    "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't \
                    even prepared for what happened whilst I was enjoying the view!",
    "content": """
        Nature is both evolution and extinction, life and death, growth and decay. She is a mosaic of heat and cold,
        light and darkness, fragility and awesome power. Nature offers sunshine and hurricanes, swans and maggots,
        rain forests and pond scum, whales and bacteria, distant galaxies and the molecules of life.
        
        Nature is both evolution and extinction, life and death, growth and decay. She is a mosaic of heat and cold,
        light and darkness, fragility and awesome power. Nature offers sunshine and hurricanes, swans and maggots,
        rain forests and pond scum, whales and bacteria, distant galaxies and the molecules of life.
        
        Nature is both evolution and extinction, life and death, growth and decay. She is a mosaic of heat and cold,
        light and darkness, fragility and awesome power. Nature offers sunshine and hurricanes, swans and maggots,
        rain forests and pond scum, whales and bacteria, distant galaxies and the molecules of life.
        
        Nature is both evolution and extinction, life and death, growth and decay. She is a mosaic of heat and cold,
        light and darkness, fragility and awesome power. Nature offers sunshine and hurricanes, swans and maggots,
        rain forests and pond scum, whales and bacteria, distant galaxies and the molecules of life.
    """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "published_on": date(2021, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "published_on": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    """
    }
]


def get_date(post):
    return post['published_on']


def index(request):
    # all_posts.sort(key=get_date)
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, post_slug):
    identified_post = next(post for post in all_posts if post['slug'] == post_slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
