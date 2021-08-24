from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)
    # post = models.ManyToManyField(Post)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=255)
    image_name = models.CharField(max_length=100)
    published_on = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    slug = models.SlugField(unique=True, max_length=60, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default="N/A", related_name="posts")
    tags = models.ManyToManyField(Tag)

