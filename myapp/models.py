from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    




class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title



