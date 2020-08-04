from django.urls import path
  
from . import views

urlpatterns = [
    path('plt_nova_total_cases', views.plt_nova_total_cases_view, name='plt_nova_total_cases_view'),
    path('plt_nova_casechange', views.plt_nova_casechange_view, name='plt_nova_casechange_view'),
    path('plt_nova_mavg', views.plt_nova_movingavg_view, name='plt_nova_movingavg'),
    path('plt_nova_changedeath_view', views.plt_nova_changedeath_view, name='plt_nova_changedeath_view'),
    path('plt_nova_movingavg_deaths_view', views.plt_nova_movingavg_deaths_view, name='plt_nova_movingavg_deaths_view'),
]