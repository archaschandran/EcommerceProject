# to save all the links related to model category
from . models import Category

def menu_links(request):
    links=Category.objects.all()
    return dict(links=links) # to get as dictionary links in red is the key


