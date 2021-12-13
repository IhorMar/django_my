from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'start_window/index.html')
    # return HttpResponse("<h4>Hello, world. You're at the polls index.<h4/>")


def asia(request):
    return render(request, 'start_window/asia.html')


def europe(request):
    return render(request, 'start_window/europe.html')


def ukraine(request):
    return render(request, 'start_window/ukraine.html')
