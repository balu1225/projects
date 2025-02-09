from django.db import models

# Create your models here.
class BlogPostModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class CommentModel(models.Model):  # Ensure the correct class name is used
    post = models.ForeignKey(BlogPostModel, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name}"