from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, Company, CsvFile

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def calculator(request):
    return render(request, "calculator.html")
def about(request):
    return render(request, "about.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
