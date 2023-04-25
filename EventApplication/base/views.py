from django.shortcuts import render
from .models import User, Event, Submission

# Create your views here.
def home_page(request):
    users = User.objects.filter(party=True)
    events = Event.objects.all()
    context = {'users': users, 'events': events}
    return render(request, "home.html", context)
