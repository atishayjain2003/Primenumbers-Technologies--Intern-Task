from django.shortcuts import render
from .models import Restaurant
from django.db.models import Q

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Restaurant.objects.filter(Q(name__icontains=query) | Q(dish__icontains=query))
    return render(request, 'search.html', {'query': query, 'results': results})
