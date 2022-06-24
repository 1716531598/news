from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class News(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    url = models.CharField(max_length=300)
    image = models.CharField(max_length=100)
    published_at=models.DateTimeField(default=timezone.now)
    content= models.TextField(max_length=10000)
    news_source = models.ForeignKey(to="Source", on_delete=models.CASCADE)

class Source(models.Model):
    id = models.AutoField(primary_key=True)
    source_id = models.CharField(max_length=30)
    source_name = models.CharField(max_length=30)