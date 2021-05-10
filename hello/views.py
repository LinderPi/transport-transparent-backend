from django.shortcuts import render
from django.http import HttpResponse

from api.models import Company, CsvFile
from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def calculator(request):
    if request.method == 'GET':
        return render(request, "calculator.html")

    csv_file = request.FILES['file']
    print(csv_file.read().decode('UTF-8'))

    return render(request, "calculator.html") # TODO: go to results

def about(request):
    return render(request, "about.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
