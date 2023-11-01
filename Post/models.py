from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Use 'models.CASCADE' for on_delete
    title = models.CharField(max_length=50)
    content = models.TextField(default=',')  # Correct default value
    img = models.ImageField(upload_to='post_img/' , default='post_img/default.png')
    created = models.DateTimeField(default=timezone.now)  # Use auto_now_add for created timestamp



    def __str__(self):
        return self.title