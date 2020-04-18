
from django.urls import path
from . import views

app_name='agent'

urlpatterns = [
    path('', views.agents_list, name='agents_list'),
]
