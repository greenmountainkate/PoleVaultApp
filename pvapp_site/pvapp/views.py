from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.generic import ListView
from .models import Athlete

class AthleteListView(ListView):
    model = Athlete
    context_object_name = 'athletes'

# Create your views here.
def index(request):
    athletes = Athlete.objects.order_by('name');
    return render(request, 'pvapp/index.html', locals(), {'athletes': athletes})

def athlete(request, pk):
    athlete = get_object_or_404(Athlete, pk=pk)
    return render(request, 'pvapp/athlete.html', {'athlete': athlete})