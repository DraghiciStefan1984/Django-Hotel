from django.shortcuts import render
from .models import Agent


# Create your views here.
def agents_list(request):
    agents_list=Agent.objects.all()
    return render(request, 'agents.html', {'agents_list':agents_list})