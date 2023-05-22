from django.shortcuts import render, redirect
from .models import User, Event, Submission
from .forms import SubmissionForm, UserForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    users = User.objects.filter(party=True)
    events = Event.objects.all()
    context = {'users': users, 'events': events}
    return render(request, "home.html", context)


def event_page(request, pk):
    event = Event.objects.get(id=pk)
    
    registered = request.user.events.filter(id=event.id).exists()
    submitted = Submission.objects.filter(participant=request.user, event=event).exists()
    print('registered', registered)
    print('submitted', submitted)
    context = {'event' : event, 'registered': registered, 'submitted': submitted}
    return render(request, 'event.html', context)

@login_required()
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

@login_required(login_url='login')
def account_page(request):
    user = request.user
    context = {'user' : user} 
    return render(request, 'account.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def update_submission(request, pk):
    submission = Submission.objects.get(id=pk)
    events = submission.event
    forms = SubmissionForm(instance=submission)
    
    if request.user != submission.participant:
        return HttpResponse("Nice Try")
    elif request.user is None:
        return redirect('account')
    
    if request.method == 'POST':
        forms = SubmissionForm(request.POST, instance=submission)
        if forms.is_valid():
            forms.save()
            return redirect('account')
        
    context= {'forms': forms, 'events': events}
    return render(request, 'submit.html', context)

def login_page(request):
    page = 'login'
    
    if request.method == 'POST':
        user = authenticate(
            email=request.POST['email'],
            password=request.POST['password']
            )
        if user is not None:
            login(request, user)
            return redirect('home')
        
    context = {'page': page}
    return render(request, 'login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')

def register_page(request):
    forms = RegisterForm
    page = 'register'
    
    if request.method == "POST":
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            user = forms.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
    context = {'page': page, 'forms': forms}
    return render(request, 'login.html', context)