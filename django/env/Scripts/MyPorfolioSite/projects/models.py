from django.db import models
from django.urls import reverse
# Create your models here.

class Project(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pretext= models.TextField(max_length=150)
    text = models.TextField()
    link = models.URLField(max_length=200)
    priority = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title
