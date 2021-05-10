from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from api.models import Company, CsvFile

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def calculator(request):
    return render(request, "calculator.html")

def about(request):
    return render(request, "calculator.html")

def companies(request):
    companies = Company.objects.all()

    context= {'companies': companies}
    return render(request, "about.html", context)

def company(request, pk):

    company = Company.objects.get(pk=pk)

    context = {

        'company': company

    }

    return render(request, 'company.html', context)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
