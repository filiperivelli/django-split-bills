from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .models import House, Residents, BillType, Bills, Split

from .forms import CreateUserForm

#Accounts Views
def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' +user)
            return redirect('login')

    context = {'form':form}
    return render(request,'accounts/register.html', context)
  
class LoginView(LoginView):
    template_name = 'accounts/login.html'    

#House Views
class HouseListView(ListView):
    model = House
    template_name = 'house-list.html'

class HouseCreateView(CreateView):
    model = House
    template_name = "create.html"
    fields = ['nick_name','adress']
    success_url = reverse_lazy('house-list')

class HouseUpdateView(UpdateView):
    model = House
    template_name = "update.html"
    fields = ['nick_name', 'adress']
    context_object_name = 'house'
    def get_success_url(self):
        return reverse_lazy('house-list')

class HouseDeleteView(DeleteView):
    model = House
    template_name = "delete.html"
    success_url = reverse_lazy('house-list')

#Residents Views
class ResidentsListView(ListView):
    model = Residents
    template_name = 'residents-list.html'

class ResidentsCreateView(CreateView):
    model = Residents
    template_name = "create.html"
    fields = ('name','email','mobile','cod_house','dt_in','dt_out')
    success_url = reverse_lazy('residents-list')

class ResidentsUpdateView(UpdateView):
    model = Residents
    template_name = "update.html"
    fields = ('name','email','mobile','cod_house','dt_in','dt_out')
    context_object_name = 'residents'
    def get_success_url(self):
        return reverse_lazy('residents-list')

class ResidentsDeleteView(DeleteView):
    model = Residents
    template_name = "delete.html"
    success_url = reverse_lazy('residents-list')

#Bill Type Views
class BillTypeListView(ListView):
    model = BillType
    template_name = "bill-type-list.html"

class BillTypeCreateView(CreateView):
    model = BillType
    template_name = "create.html"
    fields = ('name',)
    success_url = reverse_lazy('bill-type-list')

class BillTypeUpdateView(UpdateView):
    model = BillType
    template_name = "update.html"
    fields = ('name',)
    
    def get_success_url(self):
        return reverse_lazy('bill-type-list')

class BillTypeDeleteView(DeleteView):
    model = BillType
    template_name = "delete.html"
    success_url =reverse_lazy('bill-type-list')

#Bills Views
class BillsListView(ListView):
    model = Bills
    template_name = "bills-list.html"

class BillsCreateView(CreateView):
    model = Bills
    fields = '__all__'
    template_name = "create.html"
    success_url = reverse_lazy('bills-list')

class BillsUpdateView(UpdateView):
    model = Bills
    template_name = "update.html"
    fields = '__all__'
    def get_success_url(self):
        return reverse_lazy('bills-list')

class BillsDeleteView(DeleteView):
    model = Bills
    template_name = "delete.html"
    success_url = reverse_lazy('bills-list')