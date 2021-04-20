from django.urls import path

from . import views


urlpatterns = [
    path('', views.HouseListView.as_view(), name='house-list'),
    path('house/create', views.HouseCreateView.as_view(), name='house-create'),
    path('house/<int:pk>/update', views.HouseUpdateView.as_view(), name='house-update'),
    path('house/<int:pk>/delete', views.HouseDeleteView.as_view(), name='house-delete'),
   
    path('residents/', views.ResidentsListView.as_view(), name='residents-list'),
    path('residents/create', views.ResidentsCreateView.as_view(), name='residents-create'),
    path('residents/<int:pk>/update', views.ResidentsUpdateView.as_view(), name='residents-update'),
    path('residents/<int:pk>/delete', views.ResidentsDeleteView.as_view(), name='residents-delete'),
]