from django.shortcuts import render

# Create your views here.
def affiliate(request):
    return render (request, 'base_affiliate.html')

def seats(request):
    return render (request, 'affiliate/seats.html')