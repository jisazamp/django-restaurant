from django.shortcuts import HttpResponse 


# Create your views here.
def home(request):
    return HttpResponse("Home")


def menu(request):
    return HttpResponse("Menu")


def locations(request):
    return HttpResponse("Locations")