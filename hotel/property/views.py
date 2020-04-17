from django.shortcuts import render
from .models import Property, Category


# Create your views here.
def property_list(request):
    property_list=Property.objects.all()
    return render(request, 'list.html', {'property_list':property_list})


def property_detail(request, id):
    property=Property.objects.get(pk=id)
    return render(request, 'detail.html', {'property':property})