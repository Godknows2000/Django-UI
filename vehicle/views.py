from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from main.models import Vehicle

from main.section import Section
section = Section()
section.actionbar = True
section.breadcrumb = True

def index_view(request):
    
    section.page_title = "Vehicles"
    section.sidebar=False
    section.actionbar = True

    my_list = Vehicle.objects.all().order_by('year')
    context = {
        'section': section,
        'query_string': "",
        'my_list': my_list,
        'user': request.user,
        
    }
    
    return render(request, 'vehicles/index.html', context)

def details_view(request, number_plate):
    vehicle = Vehicle.objects.get(number_plate = number_plate)
    section.page_title = vehicle.number_plate
    section.sidebar = True
    section.actionbar = True

    context = {
        'section': section,
        'query_string': "",
        'vehicle': vehicle,       
        'user': request.user,
        
    }
    return render(request, 'vehicles/details.html', context)