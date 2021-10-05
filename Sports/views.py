from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import about,slider,clients,portfolio
def sports(request):
    # aboutdata=about.objects.all()[0]
    # sliderdata=slider.objects.all()
    # clientsdata=clients.objects.all()
    # portfoliodata=portfolio.objects.all()
    #
    # diction={'about':aboutdata, 'slider':sliderdata,'clients':clientsdata, 'portfolio':portfoliodata}
    return render(request,'sports.html')
