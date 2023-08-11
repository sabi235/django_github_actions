from django.db import models

class Article(models.Model):
   author_name = models.CharField(max_length=30)
   title = models.CharField(max_length=20)
   content = models.CharField(max_length=200)
   def __str__(self):
       return self.title