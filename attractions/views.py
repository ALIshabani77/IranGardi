from django.shortcuts import render
from attractions.models import Attraction

def attraction_list(request):
    attractions = Attraction.objects.all()
    return render(request, 'attractions/list.html', {'attractions': attractions})