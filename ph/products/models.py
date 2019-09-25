from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    title = models.CharField(default='产品标题',max_length=50)
    intro = models.TextField(default='产品简介')
    product_url = models.URLField()
    product_icon = models.ImageField(upload_to='images/')
    product_image = models.ImageField(upload_to='images/')
    votes = models.IntegerField(default=1)
    publish_date = models.DateTimeField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title