from django.shortcuts import render, redirect
from .models import User, Event, Submission

# Create your views here.
def home_page(request):
    users = User.objects.filter(party=True)
    events = Event.objects.all()
    context = {'users': users, 'events': events}
    return render(request, "home.html", context)


def event_page(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event' : event}
    return render(request, 'event.html', context)

def registration_confirmation(request, pk):
    event= Event.objects.get(id=pk)
    context = {'event' : event}
    
    if request.method == 'POST':
        event.participants.add(request.user)
        return redirect('event', pk=event.id)
    return render(request, 'event_confirmation.html', context)

def user_page(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'profile.html', context)

def account_page(request):
    user = request.user
    context = {'user' : user} 
    return render(request, 'account.html', context)