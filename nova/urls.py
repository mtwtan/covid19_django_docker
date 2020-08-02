from django.urls import path
  
from . import views

urlpatterns = [
    path('plt_nova_total_cases', views.plt_nova_total_cases_view, name='plt_nova_total_cases_view'),
]