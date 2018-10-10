from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.generic import ListView
from .models import Athlete, Session

class AthleteListView(ListView):
    model = Athlete
    context_object_name = 'athletes'

class SessionListView(ListView):
    model = Session
    context_object_name = 'sessions'

# Create your views here.
def index(request):
    athletes = Athlete.objects.order_by('name')
    sessions = Session.objects.order_by('date')
    return render(request, 'pvapp/index.html', locals(), {'athletes': athletes, 'sessions': sessions})

def athlete(request, pk):
    athlete = get_object_or_404(Athlete, pk=pk)
    return render(request, 'pvapp/athlete.html', {'athlete': athlete})

def session(request, pk):
    session = get_object_or_404(Session, pk=pk)
    return render(request, 'pvapp/session.html', {'session': session})

def athletes(request):
    athletes = Athlete.objects.order_by('name')
    sessions = Session.objects.order_by('date')
    return render(request, 'pvapp/athletes.html', locals(), {'athletes': athletes})

def sessions(request):
    sessions = Session.objects.order_by('date')
    athletes = Athlete.objects.order_by('name')
    return render(request, 'pvapp/sessions.html', locals(), {'sessions': sessions, 'athletes': athletes})

def calibrate(request):
    return render(request, 'pvapp/calibrate.html', locals())