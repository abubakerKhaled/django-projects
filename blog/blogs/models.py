from django.db import models

class BlogPost(models.Model):
    """Blog Post model."""
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title