from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

#MODEL FOR INVITATION FORM
class Invitation(models.Model):
    guest1 = '1 Guest'
    guest2 = '2 Guest'
    guest3 = '3 Guest'
    guest4 = '4 Guest'
    guest_number = [
        (guest1, '1 Guest'),
        (guest2, '2 Guest'),
        (guest3, '3 Guest'),
        (guest4, '4 Guest'),
    ]
    full_name = models.CharField(verbose_name='Full Name', max_length = 100)
    email = models.EmailField(verbose_name = 'Email')
    guest = models.CharField(verbose_name='Number of guest', max_length=10, choices=guest_number, default=guest1)
    message = models.TextField(verbose_name='Message')
    time = models.DateTimeField(default=timezone.now)

# MODEL FOR BLOG CATEGORY
class Category(models.Model):
    cat_name = models.CharField(verbose_name='Category Name', max_length=50)
    cat_desc = models.CharField(verbose_name='Category Description', max_length=250)

    def __str__(self):
        return self.cat_name

# MODEL FOR BLOG POST
class Post(models.Model):
    title = models.CharField(verbose_name='Post Title', max_length=300)
    post = models.TextField(verbose_name='Post Content')
    cat = models.ManyToManyField(Category, verbose_name='Select Post Category')
    img = models.ImageField(verbose_name='Picture', upload_to= 'images', blank=True, null=True)
    poster = models.ForeignKey(User, verbose_name='Post By', on_delete=models.CASCADE, default=User)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

# MODEL FOR COMMENTS
class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name ='comments')
    comment = models.TextField(verbose_name='Comment')
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.comment

# MODEL FOR PICTUER GALLERY
class Pictures(models.Model):
    couple = models.CharField(verbose_name= "couple's Name", max_length= 250)
    image = models.ImageField(verbose_name="couples's name", upload_to='wedding_pictures', null= True, blank=True)
    def __str__(self):
        return self.couple

# MODEL FOR VIDEO GALLERY
class Video(models.Model):
    couple_name = models.CharField(verbose_name= "couple's Name", max_length= 250)
    video = models.FileField(verbose_name="Upload video here", upload_to='wedding_videos', null=True, blank=True)
    poster = models.ImageField(verbose_name='Video Poster', upload_to='Video_Poster', null=True, blank=True)
    def __str__(self):
        return self.couple_name
