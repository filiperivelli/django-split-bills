from django.views.generic import ListView, UpdateView, CreateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .models import House, Residents, BillType, Bills, Split

#Accounts Views
class RegisterPage(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('house-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
  
      
class LoginView(LoginView):
    template_name = 'accounts/login.html'    

#House Views
class HouseListView(LoginRequiredMixin, ListView):
    model = House
    template_name = 'house-list.html'
    context_object_name = 'houses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["houses"] = context["houses"].filter(user=self.request.user)
        return context
    
    def get_queryset(self):
        return HouseListView.objects.filter(user=self.request.user)
    

class HouseCreateView(LoginRequiredMixin, CreateView):
    model = House
    template_name = "create.html"
    fields = ['nick_name','adress']
    success_url = reverse_lazy('house-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(HouseCreateView, self).form_valid(form)


class HouseUpdateView(LoginRequiredMixin, UpdateView):
    model = House
    template_name = "update.html"
    fields = ['nick_name', 'adress']
    context_object_name = 'house'
    def get_success_url(self):
        return reverse_lazy('house-list')

class HouseDeleteView(LoginRequiredMixin, DeleteView):
    model = House
    template_name = "delete.html"
    success_url = reverse_lazy('house-list')

#Residents Views
class ResidentsListView(LoginRequiredMixin, ListView):
    model = Residents
    template_name = 'residents-list.html'

class ResidentsCreateView(LoginRequiredMixin, CreateView):
    model = Residents
    template_name = "create.html"
    fields = ('name','email','mobile','cod_house','dt_in','dt_out')
    success_url = reverse_lazy('residents-list')

class ResidentsUpdateView(LoginRequiredMixin, UpdateView):
    model = Residents
    template_name = "update.html"
    fields = ('name','email','mobile','cod_house','dt_in','dt_out')
    context_object_name = 'residents'
    def get_success_url(self):
        return reverse_lazy('residents-list')

class ResidentsDeleteView(LoginRequiredMixin, DeleteView):
    model = Residents
    template_name = "delete.html"
    success_url = reverse_lazy('residents-list')

#Bill Type Views
class BillTypeListView(LoginRequiredMixin, ListView):
    model = BillType
    template_name = "bill-type-list.html"

class BillTypeCreateView(LoginRequiredMixin, CreateView):
    model = BillType
    template_name = "create.html"
    fields = ('name',)
    success_url = reverse_lazy('bill-type-list')

class BillTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = BillType
    template_name = "update.html"
    fields = ('name',)
    
    def get_success_url(self):
        return reverse_lazy('bill-type-list')

class BillTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = BillType
    template_name = "delete.html"
    success_url =reverse_lazy('bill-type-list')

#Bills Views
class BillsListView(LoginRequiredMixin, ListView):
    model = Bills
    template_name = "bills-list.html"

class BillsCreateView(LoginRequiredMixin, CreateView):
    model = Bills
    fields = '__all__'
    template_name = "create.html"
    success_url = reverse_lazy('bills-list')

class BillsUpdateView(LoginRequiredMixin, UpdateView):
    model = Bills
    template_name = "update.html"
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('bills-list')

class BillsDeleteView(LoginRequiredMixin, DeleteView):
    model = Bills
    template_name = "delete.html"
    success_url = reverse_lazy('bills-list')