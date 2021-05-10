from django.shortcuts import render
from django.http import HttpResponse

from api.models import Company
from .models import Greeting

import pandas as pd

import logging
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def calculator(request):
    if request.method == 'GET':
        return render(request, "calculator.html")

    csv_file = request.FILES['file']
    df_csv = pd.read_csv(csv_file)
    print(df_csv)

    return render(request, "calculator.html") # TODO: go to results

def about(request):
    return render(request, "calculator.html")

def companies(request):
    companies = Company.objects.all()

    results = []
    for company in companies:
        results.append(evaluateCompany(company))

    logger.warning(companies)
    context= {'results': results}
    return render(request, "companies.html", context)

def evaluateCompany(company):
#
# Hier könnten die Auswertung der Daten gemacht werden. Vielleicht ist es aber besser diese direkt beim hochladen zu machen und ins company objekt zu speichern, damit nicht jedes Mal alle Routen analysiert werden müssen.
#
    totalemissions = {         
        'flug': 0,
        'bahn': 0,
        'lkw' : 0,
        'sonstige' : 0
    }
# Auswertung der Routen
    for route in company.routes.all():
        totalemissions['flug'] += route.distance_plane * route.quantity * 20

    
    zulieferung = 4
    intern = 3
    zustellung = 1


    context = {
        'name': company.name,
        'id': company.id,
        'rating': 'silver',
        'zulieferung_yellow': range(zulieferung),
        'zulieferung_gray': range(5-zulieferung),
        'intern_yellow': range(intern),
        'intern_gray': range(5-intern),
        'zustellung_yellow': range(zustellung),
        'zustellung_gray': range(5-zustellung),
        'emissions': {
            'flug': 20,
            'bahn': 40,
            'lkw' : 30,
            'sonstige' : 10
        }
    }
    return context

def company(request, pk):

    company = Company.objects.get(pk=pk)


    context = evaluateCompany(company)
    

    return render(request, 'company.html', context)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
