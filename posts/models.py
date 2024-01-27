# posts/models.py
from django.db import models
from accounts.models import UserAccount as User
from django.utils.timesince import timesince

class PostAttachment(models.Model):
    image = models.ImageField(upload_to='post_attachments/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    attachments = models.ManyToManyField(PostAttachment, blank=True)

    class Meta:
        ordering = ['-created_at']

    def get_time_since_created(self):
        return timesince(self.created_at)
    
    def __str__(self):
        return self.content[:50]

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name + " " + self.user.last_name} liked {self.post}'
