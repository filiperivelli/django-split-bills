from django.views.generic import ListView

from .models import House, Residents

class HousesView(ListView):
  model = House
  template_name = 'my-houses.html'

class ResidentsView(ListView):
  model = Residents
  template_name = 'residents.html'