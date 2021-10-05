from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import about,slider,clients,portfolio
def home(request):
    # aboutdata=about.objects.all()[0]
    # sliderdata=slider.objects.all()
    # clientsdata=clients.objects.all()
    # portfoliodata=portfolio.objects.all()
    #
    # diction={'about':aboutdata, 'slider':sliderdata,'clients':clientsdata, 'portfolio':portfoliodata}
    return render(request,'index.html')

def aboutus(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')

def education(request):
    return render(request,'education.html')

def sports(request):
    return render(request,'sports.html')

def tennis(request):
    return render(request,'tennis.html')
