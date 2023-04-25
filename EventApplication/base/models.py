from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # AbstractUser class implements a fully featured User model with admin-compliant permissions
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    party = models.BooleanField(default=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
class Event(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, blank=True)
    date = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Submission(models.Model):
    participant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    # models.CASCADE deletes the model tree ie parent, child
    # models.SET_NULL saves an instance of a submission
    details = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.event) + '---' + str(self.participant)
    
    
    