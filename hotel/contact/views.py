from django.shortcuts import render
from .models import Contact


# Create your views here.
def contact(request):
    contact=Contact.objects.last()
    return render(request, 'contact.html', {'contact':contact})