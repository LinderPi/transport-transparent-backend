from django.shortcuts import render

from api.models import Company, Route
from .models import Greeting

import logging
import math
import pandas as pd

logger = logging.getLogger(__name__)

def index(request):
    return render(request, "index.html")

def calculator(request):
    if request.method == 'GET':
        return render(request, "calculator.html")

    try:
        # read posted CSV file
        csv_file = request.FILES['file']
        df_csv = pd.read_csv(csv_file, sep=";")

        # iterate through CSV and create routes
        route_ids = []
        for _, df_route in df_csv.iterrows():
            route = Route(
                delivery=df_route['delivery'],
                start=df_route['start'],
                end=df_route['end'],
                product=df_route['product'],
                quantity=df_route['quantity'],
                duration_max=df_route['duration_max'],
                distance_train=df_route['distance_train'],
                duration_train=df_route['duration_train'],
                energy_train=df_route['energy_train'],
                distance_truck=df_route['distance_truck'],
                duration_truck=df_route['duration_truck'],
                energy_truck=df_route['energy_truck'],
                distance_ship=df_route['distance_ship'],
                duration_ship=df_route['duration_ship'],
                energy_ship=df_route['energy_ship'],
                distance_plane=df_route['distance_plane'],
                duration_plane=df_route['duration_plane'],
                energy_plane=df_route['energy_plane'],
                distance_bike=df_route['distance_bike'],
                duration_bike=df_route['duration_bike'],
                energy_bike=df_route['energy_bike'],
                name_others=(None if math.isnan(df_route['name_others']) else df_route['name_others)']),
                distance_others=df_route['distance_others'],
                duration_others=df_route['duration_others'],
                energy_others=df_route['energy_others'],
                energy_goods=df_route['energy_goods'],
                frequency=df_route['frequency'],
            )
            route.save()
            route_ids.append(route.id)

        # create new company if not yet existing
        company_name = request.POST['company']
        try:
            company = Company.objects.get(name=company_name)
        except Company.DoesNotExist:
            company = Company(name=company_name)
            company.save()

        # add routes to company
        for route_id in route_ids:
            company.routes.add(route_id)

    except Exception as e:
        print(e)

    return companies(request)

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
