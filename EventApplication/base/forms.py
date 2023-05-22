from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Submission, User, Event

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ["details"]
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]
        

class RegisterForm(UserCreationForm):
    class Meta:
        model =  User
        fields = ["username", "email", "name", "password1", "password2"]    


