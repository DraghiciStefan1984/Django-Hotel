from django.shortcuts import render
from .models import Property, Category
from .forms import ReserveForm


# Create your views here.
def property_list(request):
    property_list=Property.objects.all()
    return render(request, 'list.html', {'property_list':property_list})


def property_detail(request, id):
    property=Property.objects.get(pk=id)
    if request.method=='POST':
        reserve_form=ReserveForm(request.POST)
        if reserve_form.is_valid():
            pass
    else:
        reserve_form=ReserveForm()
    context={'property':property, 'reserve_form':reserve_form}
    return render(request, 'detail.html', context)