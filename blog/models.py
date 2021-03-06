from django.db import models
from django.urls import reverse

# Class of posts in the blog
class Post(models.Model):
    #very much self-explanatory variable names
    author = models.CharField(max_length=16)
    title = models.CharField(max_length=32)
    text = models.TextField()

    #string representation of class object
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:read_post',kwargs={'pk':self.pk})

# Comments, anyone can add. No veification
class Comment(models.Model):
    #very much self-explanatory variable names
    author = models.CharField(max_length=16)
    text = models.TextField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') #to which post is the comment

    #string representation of class object
    def __str__(self):
        return self.author
