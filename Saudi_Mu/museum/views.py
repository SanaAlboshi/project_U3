from django.shortcuts import render

def add_museum(request):
    return render(request, 'museum/add_museum.html')

def all_del_museum(request):
    return render(request, 'museum/all_del_museum.html')

def booking(request):
    return render(request, 'museum/booking.html')

def details(request):
    return render(request, 'museum/details.html')

def search(request):
    return render(request, 'museum/search.html')
