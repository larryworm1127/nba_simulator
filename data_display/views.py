from django.shortcuts import render
from .models import Simulator


def index(request):
    title = Simulator.simulator_title
    return render(request, 'data_display/index.html', {'title': title})

