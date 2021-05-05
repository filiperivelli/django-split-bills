from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views, models


urlpatterns = [
    path('', views.HouseListView.as_view(), name='house-list'),
    path('house/create', views.HouseCreateView.as_view(), name='house-create'),
    path('house/<int:pk>/update', views.HouseUpdateView.as_view(), name='house-update'),
    path('house/<int:pk>/delete', views.HouseDeleteView.as_view(), name='house-delete'),
   
    path('residents/', views.ResidentsListView.as_view(), name='residents-list'),
    path('residents/create', views.ResidentsCreateView.as_view(), name='residents-create'),
    path('residents/<int:pk>/update', views.ResidentsUpdateView.as_view(), name='residents-update'),
    path('residents/<int:pk>/delete', views.ResidentsDeleteView.as_view(), name='residents-delete'),

    path('billtype/', views.BillTypeListView.as_view(), name='bill-type-list'),
    path('billtype/create', views.BillTypeCreateView.as_view(), name='bill-type-create'),
    path('billtype/<int:pk>/update', views.BillTypeUpdateView.as_view(), name='bill-type-update'),
    path('billtype/<int:pk>/delete', views.BillTypeDeleteView.as_view(), name='bill-type-delete'),

    path('bills/', views.BillsListView.as_view(), name='bills-list'),
    path('bills/create', views.BillsCreateView.as_view(), name='bills-create'),
    path('bills/<int:pk>/update', views.BillsUpdateView.as_view(), name='bills-update'),
    path('bills/<int:pk>/delete', views.BillsDeleteView.as_view(), name='bills-delete'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
]