from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Profile(models.Model):
    created_by = models.OneToOneField(User, related_name='profiles', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    about_me = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class Todo(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    )


    user = models.ForeignKey(Profile, related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default='Pending', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title