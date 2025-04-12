from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=255)
    Email = models.EmailField(null=True)
    Password = models.CharField(null=True)
    def __str__(self):
        return f"{self.Username} - {self.Email}"

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=255)
    Date_Published = models.DateTimeField(auto_now_add=True)
    
    

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Content = models.TextField()
    Date_Posted = models.DateTimeField(auto_now_add=True) 
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py createsuperuser
