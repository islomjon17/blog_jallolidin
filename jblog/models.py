from pdb import post_mortem
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse    

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return (self.name)

   


STATUS = (
    (0, "Draft"),
    (1, "Published")
)



class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True) #Title of the Article
    slug = models.SlugField(max_length=200, unique=True) #Unique identifier for the article
    author = models.ForeignKey(User, on_delete=models.CASCADE) #Author of the Article
    description = models.CharField(max_length=500) #Short Description of the articlentent of the article, you need to install CKEditor
    category = models.CharField(max_length=255, default="uncategorized")#Category of the article
    keywords = models.CharField(max_length=250) #Keywords to be used in SEO
    cover = models.ImageField(null=True, blank=True, upload_to='images/') #Cover Image of the article
    created_on = models.DateTimeField(auto_now_add=True) #Date of creation
    updated_on = models.DateTimeField(auto_now=True) #Date of updation
    status = models.IntegerField(choices=STATUS, default=0) #Status of the Article either Draft or Published

    def __str__(self):
        return f"({self.title}) ({self.author})"
        
    

    