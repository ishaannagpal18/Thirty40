from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=264, verbose_name="Put a Title")
    slug = models.CharField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name="What is on your mind?")
    blog_image = models.ImageField(upload_to='blog_image', verbose_name="Blog Image")
    publish_date = models.DateField(auto_now_add=True)
    upload_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='blog_comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateField(auto_now_add=True)

class Like(models.Model):
    blog = models.ForeignKey(Blog, related_name='liked_blog', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='liked_user', on_delete=models.CASCADE)
