from django.shortcuts import render

from api.models import Company, Route
from .models import Greeting

import logging
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
                start=df_route['start'],
                end=df_route['end'],
                distance=df_route['distance'],
                quantity=df_route['quantity'],
                transportation=df_route['transportation'],
                delivery=df_route['delivery'],
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
    emissions = {
        'internal': {
            'train': 0,
            'truck': 0,
            'ship': 0,
            'plane': 0,
            'others': 0,
        },
        'in': {
            'train': 0,
            'truck': 0,
            'ship': 0,
            'plane': 0,
            'others': 0,
        },
        'out': {
            'train': 0,
            'truck': 0,
            'ship': 0,
            'plane': 0,
            'others': 0,
        }
    }

    emissions_train = emissions_truck = emissions_ship = emissions_plane = emissions_others = 0

    # evaluate routes
    for route in company.routes.all():
        if route.transportation == 'train':
            temp = route.quantity * route.distance * route.frequency * 17
            emissions[route.delivery]['train'] += temp
            emissions_train += temp
        elif route.transportation == 'truck':
            temp = route.quantity * route.distance * route.frequency * 111
            emissions[route.delivery]['truck'] += temp
            emissions_truck += temp
        elif route.transportation == 'ship':
            temp = route.quantity * route.distance * route.frequency * 30
            emissions[route.delivery]['ship'] += temp
            emissions_ship += temp
        elif route.transportation == 'plane':
            temp = route.quantity * route.distance * route.frequency * 713
            emissions[route.delivery]['plane'] += temp
            emissions_plane += temp
        elif route.transportation == 'others':
            temp = route.quantity * route.distance * route.frequency * 0
            emissions[route.delivery]['others'] += temp
            emissions_others += temp

    total_emissions = emissions_train + emissions_truck + emissions_ship + emissions_plane + emissions_others

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
            'bahn': emissions_train * 100 / total_emissions,
            'lkw': emissions_truck * 100 / total_emissions,
            'schiff': emissions_ship * 100 / total_emissions,
            'flug': emissions_plane * 100 / total_emissions,
            'sonstige': emissions_others * 100 / total_emissions,
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
