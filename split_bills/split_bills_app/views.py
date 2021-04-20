from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from .models import House, Residents

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

class HouseListView(ListView):
  model = House
  template_name = 'house-list.html'

class HouseCreateView(CreateView):
    model = House
    template_name = "create.html"
    fields = ('nick_name','adress')
    success_url = reverse_lazy('house-list')

class HouseUpdateView(UpdateView):
    model = House
    template_name = "update.html"
    fields = ('nick_name', 'adress',)
    context_object_name = 'house'
    def get_success_url(self):
        return reverse_lazy('house-list')

class HouseDeleteView(DeleteView):
    model = House
    template_name = "delete.html"
    success_url = reverse_lazy('house-list')

class ResidentsListView(ListView):
  model = Residents
  template_name = 'residents-list.html'

class ResidentsCreateView(CreateView):
    model = Residents
    template_name = "create.html"
    fields = ('name','email','mobile','cod_house')
    success_url = reverse_lazy('residents-list')

class ResidentsUpdateView(UpdateView):
    model = Residents
    template_name = "update.html"
    fields = ('name','email','mobile','cod_house')
    context_object_name = 'residents'
    def get_success_url(self):
        return reverse_lazy('residents-list')

class ResidentsDeleteView(DeleteView):
    model = Residents
    template_name = "delete.html"
    success_url = reverse_lazy('residents-list')


