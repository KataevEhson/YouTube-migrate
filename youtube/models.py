from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Ganr(models.Model):
    text = models.TextField()
    created_at = models.DateField(default=datetime.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Video(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='video/')
    image = models.ImageField(upload_to='video_images/')
    title = models.CharField()
    author = models.CharField()
    caption = models.TextField()
    created_at = models.DateField(default=datetime.now)
    status = models.BooleanField(default=False)
    category_id = models.ForeignKey(Ganr, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title







class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField()
    text = models.TextField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateField(default=datetime.now)

    def __str__(self):
        return self.author
