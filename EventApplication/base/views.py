from django.shortcuts import render, redirect
from .models import User, Event, Submission
from .forms import SubmissionForm

# Create your views here.
def home_page(request):
    users = User.objects.filter(party=True)
    events = Event.objects.all()
    context = {'users': users, 'events': events}
    return render(request, "home.html", context)


def event_page(request, pk):
    event = Event.objects.get(id=pk)
    
    registered = request.user.events.filter(id=event.id).exists()
    
    print('registered', registered)
    context = {'event' : event, 'registered': registered}
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

def submission_page(request, pk):
    events =  Event.objects.get(id=pk)
    forms = SubmissionForm()
    context = {'events' : events, 'forms': forms }
    
    if request.method == "POST":
        forms = SubmissionForm(request.POST)
        submission = forms.save(commit=False)
        submission.participant = request.user
        if forms.is_valid():
            submission = forms.save(commit=False)
            submission.participant = request.user
            submission.event = events
            submission.save()
            return redirect('account')
        
    return render(request, 'submit.html', context)
    