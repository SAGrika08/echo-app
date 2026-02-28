from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sound


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class SoundList(ListView):
    model = Sound


