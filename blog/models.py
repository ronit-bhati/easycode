from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=350)
    content = models.TextField()
    author = models.CharField(max_length=30)
    slug = models.CharField(max_length=130)
    views = models.IntegerField(default=0)
    timeStamp = models.DateField(blank=True)
    thumbnail = models.ImageField(upload_to="blog/images", default="")

    def __str__(self):
        return '"' + self.title + '"' + ' by ' + self.author

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        if len(self.comment) >= 80:
            return self.comment[:80] + '...' + ' | comment from - ' + self.user.username
        else:
            return self.comment + ' | comment from - ' + self.user.username

class allIps(models.Model):
    ips = models.TextField(default=None)
    postname = models.TextField(default=None)
    def __str__(self):
        return f"View for: {self.postname}, ip: {self.ips}"