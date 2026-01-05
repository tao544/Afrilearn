from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    



class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    start_time = models.TimeField()
    location = models.CharField(max_length=150)
    end_time = models.TimeField()
    slug =models.SlugField(unique=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["event_date"]


    def __str__(self):
        return self.title    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="teachers/")
    slug = models.SlugField(unique=True)
    is_featured =models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
