from django.shortcuts import HttpResponse, render


# Create your views here.
def home(request):
    return HttpResponse("Home")


def menu(request):
    return HttpResponse("Menu")


def locations(request):
    return render(request, "locations.html")
