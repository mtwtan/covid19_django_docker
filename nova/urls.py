from django.urls import path
  
from . import views

urlpatterns = [
    path('plt_nova_total_cases', views.plt_nova_total_cases_view, name='plt_nova_total_cases_view'),
    path('plt_nova_total_deaths', views.plt_nova_total_deaths_view, name='plt_nova_total_deaths_view'),
    path('plt_nova_casechange', views.plt_nova_casechange_view, name='plt_nova_casechange_view'),
    path('plt_nova_mavg', views.plt_nova_movingavg_view, name='plt_nova_movingavg'),
    path('plt_nova_changedeath_view', views.plt_nova_changedeath_view, name='plt_nova_changedeath_view'),
    path('plt_nova_movingavg_deaths_view', views.plt_nova_movingavg_deaths_view, name='plt_nova_movingavg_deaths_view'),
    path('plt_nova_last_seven_days_mvg_cases', views.plt_nova_last_seven_days_mvg_cases, name='plt_nova_last_seven_days_mvg_cases'),
    path('plt_nova_last_seven_days_mvg_deaths', views.plt_nova_last_seven_days_mvg_deaths, name='plt_nova_last_seven_days_mvg_deaths'),
    path('tbl_nova', views.datatable, name='tbl_nova'),
    path('tbl_nova_count', views.datatable_count, name='tbl_nova_count'),
    path('list_counties', views.counties_json, name='list_counties'),
    path('counties_total_cases_json', views.counties_total_cases_json, name='counties_total_cases_json'),
    path('counties_daily_cases_json', views.counties_daily_cases_json, name='counties_daily_cases_json'),
    path('counties_seven_mvg_json', views.counties_seven_mvg_json, name='counties_seven_mvg_json'),
]