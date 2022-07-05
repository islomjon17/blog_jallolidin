from pdb import post_mortem
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return (self.name)

    def get_absolute_url(self):
        return reverse('home')


STATUS = (
    (0, "Draft"),
    (1, "Published")
)

REGION = (
    ("Andijon", "Andijon"), ("Samarqand", "Samarqand"), ("Sirdaryo", "Sirdaryo"),
    ("Buxoro", "Buxoro"), ("Qashqadaryo",
                           "Qashqadaryo"), ("Surxondaryo", "Surxondaryo"),
    ("Farg'ona", "Farg'ona"), ("Navoiy", "Navoiy"), ("Toshkent", "Toshkent"),
    ("Jizzax", "Jizzax"), ("Namangan",
                           "Namangan"), ("Qoraqalpag'iston", "Qoraqalpag'iston"),
    ("Xorazm", "Xorazm"),
)


class BlogPost(models.Model):
    # Title of the Article
    title = models.CharField(max_length=200, unique=True)
    # Unique identifier for the article
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)  # Author of the Article
    # Short Description of the articlentent of the article, you need to install CKEditor
    description = RichTextField(blank=True, null=True)
    category = models.ForeignKey(
        'Category', related_name='category', on_delete=models.CASCADE)
    keywords = models.CharField(max_length=250)  # Keywords to be used in SEO
    # Cover Image of the article
    cover = models.ImageField(null=True, blank=True, upload_to='images/')
    created_on = models.DateTimeField(auto_now_add=True)  # Date of creation
    updated_on = models.DateTimeField(auto_now=True)  # Date of updation
    # Status of the Article either Draft or Published
    status = models.IntegerField(choices=STATUS, default=0)
    # Status of the Article regions
    region = models.CharField(
        max_length=250, choices=REGION, default="Toshkent")
    # Article likes
    likes = models.ManyToManyField(User, related_name="blog_posts")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"({self.title}) ({self.author})"

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))
