from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to = 'images', null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.author.username} - {self.text}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE,
                             related_name = 'comments')
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.author.username} - {self.text}'

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE,
                             related_name = 'likes')
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.author.username} - {self.post}'
