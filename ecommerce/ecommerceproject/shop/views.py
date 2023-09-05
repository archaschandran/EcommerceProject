from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def allProdCat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        products_list=Product.objects.all().filter(available=True)

    paginator=Paginator(products_list,6)
    try:
        pages=int(request.GET.get('page','1'))
    except:
        pages=1 #to return page 1 otherwise write like this: pages = paginator.page(1)
    try:
        products=paginator.page(pages) #to get that given page from page in paginator.
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages) #paginator.num_pages is to get last page.

    return render(request,'category.html',{'category':c_page,'products': products})

def proDetail(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})