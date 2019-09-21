from django.db import models
 
# Create your models here.

class Gallery(models.Model):
    description = models.CharField(default='这里输入简介',max_length=100)
    image = models.ImageField(default='图片',upload_to='images/')
    title = models.CharField(default='这里是标题',max_length=50)

    def __str__(self):
        return self.title