from django.shortcuts import render
from .models import User, Event, Submission

# Create your views here.
def home_page(request):
    users = User.objects.filter(party=True)
    context = {'users': users, 'events': events}
    events = Event.objects.all()
    return render(request, "home.html")
