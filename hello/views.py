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
            temp = route.quantity * route.distance * route.frequency
            emissions[route.delivery]['train'] += temp
            emissions_train += temp
        elif route.transportation == 'truck':
            temp = route.quantity * route.distance * route.frequency
            emissions[route.delivery]['truck'] += temp
            emissions_truck += temp
        elif route.transportation == 'ship':
            temp = route.quantity * route.distance * route.frequency
            emissions[route.delivery]['ship'] += temp
            emissions_ship += temp
        elif route.transportation == 'plane':
            temp = route.quantity * route.distance * route.frequency
            emissions[route.delivery]['plane'] += temp
            emissions_plane += temp
        elif route.transportation == 'others':
            temp = route.quantity * route.distance * route.frequency
            emissions[route.delivery]['others'] += temp
            emissions_others += temp

    # compute tkm
    internal_tkm = 0
    for transportation in emissions['internal']:
        internal_tkm += emissions['internal'][transportation]
    in_tkm = 0
    for transportation in emissions['in']:
        in_tkm += emissions['in'][transportation]
    out_tkm = 0
    for transportation in emissions['out']:
        out_tkm += emissions['out'][transportation]
    total_tkm = internal_tkm + in_tkm + out_tkm

    print(total_tkm)

    # convert tkm to CO2 emissions
    emissions['internal']['train'] *= 17
    emissions['internal']['truck'] *= 111
    emissions['internal']['ship'] *= 30
    emissions['internal']['plane'] *= 713
    emissions['internal']['others'] *= 0
    emissions['in']['train'] *= 17
    emissions['in']['truck'] *= 111
    emissions['in']['ship'] *= 30
    emissions['in']['plane'] *= 713
    emissions['in']['others'] *= 0
    emissions['out']['train'] *= 17
    emissions['out']['truck'] *= 111
    emissions['out']['ship'] *= 30
    emissions['out']['plane'] *= 713
    emissions['out']['others'] *= 0

    # compute CO2 emissions
    internal_emissions = 0
    for transportation in emissions['internal']:
        internal_emissions += emissions['internal'][transportation]
    in_emissions = 0
    for transportation in emissions['in']:
        in_emissions += emissions['in'][transportation]
    out_emissions = 0
    for transportation in emissions['out']:
        out_emissions += emissions['out'][transportation]
    total_emissions = internal_emissions + in_emissions + out_emissions

    if(total_tkm == 0):
        total_tkm = 1
        in_tkm = 1
        out_tkm = 1
        internal_tkm = 1
        total_emissions = 1
    total = total_emissions / total_tkm
    

    eff_in = in_emissions / in_tkm
    eff_internal = internal_emissions / internal_tkm
    eff_out = out_emissions / out_tkm
    if (eff_in>260):
        zulieferung = 1
    elif (eff_in>200):
        zulieferung = 2
    else :
        zulieferung = 3
    

    if (eff_internal>300) :
        intern = 1
    elif (eff_internal>200):
        intern = 2
    else :
        intern = 3
    

    if (eff_out>300) :
        zustellung = 1
    elif (eff_out>200):
        zustellung = 2
    else :
        zustellung = 3
    

    # zulieferung = 3
    # intern = 2
    # zustellung = 1

        

    context = {
        'name': company.name,
        'id': company.id,
        'rating': 'silver',
        'zulieferung_yellow': range(zulieferung),
        'zulieferung_gray': range(3-zulieferung),
        'intern_yellow': range(intern),
        'intern_gray': range(3-intern),
        'zustellung_yellow': range(zustellung),
        'zustellung_gray': range(3-zustellung),
        'emissions': {
            'bahn': emissions_train * 17 * 100 / total_emissions,
            'lkw': emissions_truck * 111 * 100 / total_emissions,
            'schiff': emissions_ship * 30 * 100 / total_emissions,
            'flug': emissions_plane * 713 * 100 / total_emissions,
            'sonstige': emissions_others * 0 * 100 / total_emissions,
        }
    }
    if ((zulieferung+intern+zustellung)/3 < 1.5 ):
        context['rating'] = 'bronze'
    elif ((zulieferung+intern+zustellung)/3 < 2.5 ):
        context['rating'] = 'silver'
    else:
        context['rating'] = 'gold'
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
