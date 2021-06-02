from django.db import models

class Post(models.Model):
  text = models.TextField(default='')

  def __str__(self):
    return f"Post {self.text[:50]}"
