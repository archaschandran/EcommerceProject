from django.shortcuts import render
from shop.models import Product
from django.db.models import Q # to do query related things
# Create your views here.

def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q') # to place the submitted 'q' from url in GET method
        products=Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request,'search.html',{'query':query,'products':products})