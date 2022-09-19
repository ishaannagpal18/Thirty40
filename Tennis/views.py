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
    return render(request,'tennis.html')

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

def packages(request):
    return render(request,'packages.html')

def private(request):
    return render(request,'private.html')

def T_C(request):
    return render(request,'T_C.html')

def gurugram(request):
    return render(request,'gurugram.html')

def delhi(request):
    return render(request,'delhi.html')

def muza(request):
    return render(request,'muza.html')

def spain(request):
    return render(request,'spain.html')

def news(request):
    return render(request,'news.html')      
