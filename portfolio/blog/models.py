from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    creat_tiem = models.DateTimeField()
    image = models.ImageField(default='default.png', upload_to='images/')
    text = models.TextField()
    def __str__(self):
        return self.title
      