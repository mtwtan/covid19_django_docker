from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.template import Context, Template
from django.template.response import TemplateResponse
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import FilterByCountyForm
import json

# Create your views here.
from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

#from nova.models import DmvMovingAverage, Counties, VwNovaDailyCases, VwNovaSevenMvgAvg, VwNovaTotalCases, VwCountyPopulation
from nova.models import *
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

# Create your views here.
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
days = mdates.DayLocator(interval=5) # every day
days_one_interval = mdates.DayLocator(interval=1) # every day
month_fmt = mdates.DateFormatter('%m-%y')
day_fmt = mdates.DateFormatter('%d')

nova = DmvMovingAverage.objects.using('data').all().order_by('admin2', 'date').values()

df_nova = pd.DataFrame(list(nova))
df_nova['date'] = pd.to_datetime(df_nova['date'])
#df_nova['movingaveragedeaths'] = pd.to_numeric(df_nova['movingaveragedeaths'])
df_index = df_nova.index
num_rows = len(df_index)
max_index = num_rows - 1

rows_per_page = 30


def plt_nova_total_cases_view(request):

  fig, ax = plt.subplots()
  ax.set_title('Confirmed Cases Per Million Population')
  ax.plot('date', 'numconfirmedperm', data=df_nova.loc[df_nova['admin2'] == 'Fairfax'], label="Fairfax")
  ax.plot('date', 'numconfirmedperm', data=df_nova.loc[df_nova['admin2'] == 'Arlington'], label="Arlington")
  ax.plot('date', 'numconfirmedperm', data=df_nova.loc[df_nova['admin2'] == 'District of Columbia'], label="District of Columbia")
  ax.plot('date', 'numconfirmedperm', data=df_nova.loc[df_nova['admin2'] == 'Montgomery'], label="Montgomery")
  ax.plot('date', 'numconfirmedperm', data=df_nova.loc[df_nova['admin2'] == 'Loudoun'], label="Loudoun")
  ax.plot('date', 'numconfirmedperm', data=df_nova.loc[df_nova['admin2'] == 'Alexandria'], label="Alexandria")

  ax.xaxis.set_major_locator(months)
  ax.xaxis.set_major_formatter(month_fmt)
  ax.xaxis.set_minor_locator(days)

#  # round to nearest months
  datemin = np.datetime64(df_nova['date'][0], 'D')
#  datemax = np.datetime64(df_fairfax['date'][-1], 'D') + np.timedelta64(15, 'D')
  datemax = np.datetime64(df_nova['date'][max_index], 'D')  
  ax.set_xlim(datemin, datemax)

  plt.tight_layout()
  plt.text
  plt.legend()
  fig_buffer = BytesIO()
  plt.savefig(fig_buffer, format='png', dpi=300)

  # Save the figure as a HttpPesponse
  response = HttpResponse(content_type='image/png')
  response.write(fig_buffer.getvalue())

#  image_base64 = base64.b64encode(fig_buffer.getvalue()).decode('utf-8').replace('\n','')

  fig_buffer.close()

  return response

def plt_nova_total_deaths_view(request):

  fig, ax = plt.subplots()
  ax.set_title('Deaths Per Million Population')
  ax.plot('date', 'numdeathsperm', data=df_nova.loc[df_nova['admin2'] == 'Fairfax'], label="Fairfax")
  ax.plot('date', 'numdeathsperm', data=df_nova.loc[df_nova['admin2'] == 'Arlington'], label="Arlington")
  ax.plot('date', 'numdeathsperm', data=df_nova.loc[df_nova['admin2'] == 'District of Columbia'], label="District of Columbia")
  ax.plot('date', 'numdeathsperm', data=df_nova.loc[df_nova['admin2'] == 'Montgomery'], label="Montgomery")
  ax.plot('date', 'numdeathsperm', data=df_nova.loc[df_nova['admin2'] == 'Loudoun'], label="Loudoun")
  ax.plot('date', 'numdeathsperm', data=df_nova.loc[df_nova['admin2'] == 'Alexandria'], label="Alexandria")

  ax.xaxis.set_major_locator(months)
  ax.xaxis.set_major_formatter(month_fmt)
  ax.xaxis.set_minor_locator(days)

#  # round to nearest months
  datemin = np.datetime64(df_nova['date'][0], 'D')
#  datemax = np.datetime64(df_fairfax['date'][-1], 'D') + np.timedelta64(15, 'D')
  datemax = np.datetime64(df_nova['date'][max_index], 'D')  
  ax.set_xlim(datemin, datemax)

  plt.tight_layout()
  plt.text
  plt.legend()
  fig_buffer = BytesIO()
  plt.savefig(fig_buffer, format='png', dpi=300)

  # Save the figure as a HttpPesponse
  response = HttpResponse(content_type='image/png')
  response.write(fig_buffer.getvalue())

#  image_base64 = base64.b64encode(fig_buffer.getvalue()).decode('utf-8').replace('\n','')

  fig_buffer.close()

  return response

def plt_nova_movingavg_view(request):
#  df_nova = pd.DataFrame(list(DmvMovingAverage.objects.using('data').all().values()))
#  df_nova['date'] = pd.to_datetime(df_nova['date'])
#  df_index = df_nova.index
#  num_rows = len(df_index)
#  max_index = num_rows - 1

  fig, ax = plt.subplots()
  ax.set_title('7 days Moving Average - Confirmed Cases Per Million Population')
  ax.plot('date', 'movingaverageperm', data=df_nova.loc[df_nova['admin2'] == 'Fairfax'], label="Fairfax")
  ax.plot('date', 'movingaverageperm', data=df_nova.loc[df_nova['admin2'] == 'Arlington'], label="Arlington")
  ax.plot('date', 'movingaverageperm', data=df_nova.loc[df_nova['admin2'] == 'District of Columbia'], label="District of Columbia")
  ax.plot('date', 'movingaverageperm', data=df_nova.loc[df_nova['admin2'] == 'Montgomery'], label="Montgomery")
  ax.plot('date', 'movingaverageperm', data=df_nova.loc[df_nova['admin2'] == 'Loudoun'], label="Loudoun")
  ax.plot('date', 'movingaverageperm', data=df_nova.loc[df_nova['admin2'] == 'Alexandria'], label="Alexandria")

  ax.xaxis.set_major_locator(months)
  ax.xaxis.set_major_formatter(month_fmt)
  ax.xaxis.set_minor_locator(days)

#  # round to nearest months
  datemin = np.datetime64(df_nova['date'][0], 'D')
#  datemax = np.datetime64(df_fairfax['date'][-1], 'D') + np.timedelta64(15, 'D')
  datemax = np.datetime64(df_nova['date'][max_index], 'D')
  ax.set_xlim(datemin, datemax)

  plt.tight_layout()
  plt.text
  plt.legend()
  fig_buffer = BytesIO()
  plt.savefig(fig_buffer, format='png', dpi=300)

  # Save the figure as a HttpPesponse
  response = HttpResponse(content_type='image/png')
  response.write(fig_buffer.getvalue())

  fig_buffer.close()

  return response

def plt_nova_casechange_view(request):

  fig, ax = plt.subplots()
  ax.set_title('Confirmed Cases - Daily Per Million Population')
  ax.plot('date', 'changeperm', data=df_nova.loc[df_nova['admin2'] == 'Fairfax'], label="Fairfax")
  ax.plot('date', 'changeperm', data=df_nova.loc[df_nova['admin2'] == 'Arlington'], label="Arlington")
  ax.plot('date', 'changeperm', data=df_nova.loc[df_nova['admin2'] == 'District of Columbia'], label="District of Columbia")
  ax.plot('date', 'changeperm', data=df_nova.loc[df_nova['admin2'] == 'Montgomery'], label="Montgomery")
  ax.plot('date', 'changeperm', data=df_nova.loc[df_nova['admin2'] == 'Loudoun'], label="Loudoun")
  ax.plot('date', 'changeperm', data=df_nova.loc[df_nova['admin2'] == 'Alexandria'], label="Alexandria")

  ax.xaxis.set_major_locator(months)
  ax.xaxis.set_major_formatter(month_fmt)
  ax.xaxis.set_minor_locator(days)

#  # round to nearest months
  datemin = np.datetime64(df_nova['date'][0], 'D')
#  datemax = np.datetime64(df_fairfax['date'][-1], 'D') + np.timedelta64(15, 'D')
  datemax = np.datetime64(df_nova['date'][max_index], 'D')
  ax.set_xlim(datemin, datemax)

  plt.tight_layout()
  plt.text
  plt.legend()
  fig_buffer = BytesIO()
  plt.savefig(fig_buffer, format='png', dpi=300)

  # Save the figure as a HttpPesponse
  response = HttpResponse(content_type='image/png')
  response.write(fig_buffer.getvalue())

  fig_buffer.close()

  return response

def plt_nova_changedeath_view(request):

  fig, ax = plt.subplots()
  ax.set_title('Deaths - Daily Per Million Population')
  ax.plot('date', 'changedeathsperm', data=df_nova.loc[df_nova['admin2'] == 'Fairfax'], label="Fairfax")
  ax.plot('date', 'changedeathsperm', data=df_nova.loc[df_nova['admin2'] == 'Arlington'], label="Arlington")
  ax.plot('date', 'changedeathsperm', data=df_nova.loc[df_nova['admin2'] == 'District of Columbia'], label="District of Columbia")
  ax.plot('date', 'changedeathsperm', data=df_nova.loc[df_nova['admin2'] == 'Montgomery'], label="Montgomery")
  ax.plot('date', 'changedeathsperm', data=df_nova.loc[df_nova['admin2'] == 'Loudoun'], label="Loudoun")
  ax.plot('date', 'changedeathsperm', data=df_nova.loc[df_nova['admin2'] == 'Alexandria'], label="Alexandria")

  ax.xaxis.set_major_locator(months)
  ax.xaxis.set_major_formatter(month_fmt)
  ax.xaxis.set_minor_locator(days)

#  # round to nearest months
  datemin = np.datetime64(df_nova['date'][0], 'D')
#  datemax = np.datetime64(df_fairfax['date'][-1], 'D') + np.timedelta64(15, 'D')
  datemax = np.datetime64(df_nova['date'][max_index], 'D')
  ax.set_xlim(datemin, datemax)

  plt.tight_layout()
  plt.text
  plt.legend()
  fig_buffer = BytesIO()
  plt.savefig(fig_buffer, format='png', dpi=300)

  # Save the figure as a HttpPesponse
  response = HttpResponse(content_type='image/png')
  response.write(fig_buffer.getvalue())

  fig_buffer.close()

  return response

def plt_nova_movingavg_deaths_view(request):

  fig, ax = plt.subplots()
  ax.set_title('7 days Moving Average - Deaths Per Million Population')
  ax.plot('date', 'movingaveragedeathsperm', data=df_nova.loc[df_nova['admin2'] == 'Fairfax'], label="Fairfax")
  ax.plot('date', 'movingaveragedeathsperm', data=df_nova.loc[df_nova['admin2'] == 'Arlington'], label="Arlington")
  ax.plot('date', 'movingaveragedeathsperm', data=df_nova.loc[df_nova['admin2'] == 'District of Columbia'], label="District of Columbia")
  ax.plot('date', 'movingaveragedeathsperm', data=df_nova.loc[df_nova['admin2'] == 'Montgomery'], label="Montgomery")
  ax.plot('date', 'movingaveragedeathsperm', data=df_nova.loc[df_nova['admin2'] == 'Loudoun'], label="Loudoun")
  ax.plot('date', 'movingaveragedeathsperm', data=df_nova.loc[df_nova['admin2'] == 'Alexandria'], label="Alexandria")

  ax.xaxis.set_major_locator(months)
  ax.xaxis.set_major_formatter(month_fmt)
  ax.xaxis.set_minor_locator(days)

#  # round to nearest months
  datemin = np.datetime64(df_nova['date'][0], 'D')
#  datemax = np.datetime64(df_fairfax['date'][-1], 'D') + np.timedelta64(15, 'D')
  datemax = np.datetime64(df_nova['date'][max_index], 'D')
  ax.set_xlim(datemin, datemax)

  plt.tight_layout()
  plt.text
  plt.legend()
  fig_buffer = BytesIO()
  plt.savefig(fig_buffer, format='png', dpi=300)

  # Save the figure as a HttpPesponse
  response = HttpResponse(content_type='image/png')
  response.write(fig_buffer.getvalue())

  fig_buffer.close()

  return response

def plt_nova_last_seven_days_mvg_cases(request):

  last_seven_days_obj = VwNovaSevenMvgAvg.objects.using('data').order_by('date', 'admin2').values()
  df_seven_days = pd.DataFrame(list(last_seven_days_obj))
  df_seven_days['date'] = pd.to_datetime(df_seven_days['date'])

  num_rows = len(df_seven_days)
  max_index = num_rows - 1

  fig, ax = plt.subplots()
  ax.set_title('Last 7 days Moving Average - New Cases Per Million Population')
  ax.plot('date', 'mvg_cases', data=df_seven_days.loc[df_seven_days['admin2'] == 'Fairfax'], label="Fairfax")
  ax.plot('date', 'mvg_cases', data=df_seven_days.loc[df_seven_days['admin2'] == 'Arlington'], label="Arlington")
  ax.plot('date', 'mvg_cases', data=df_seven_days.loc[df_seven_days['admin2'] == 'District of Columbia'], label="District of Columbia")
  ax.plot('date', 'mvg_cases', data=df_seven_days.loc[df_seven_days['admin2'] == 'Montgomery'], label="Montgomery")
  ax.plot('date', 'mvg_cases', data=df_seven_days.loc[df_seven_days['admin2'] == 'Loudoun'], label="Loudoun")
  ax.plot('date', 'mvg_cases', data=df_seven_days.loc[df_seven_days['admin2'] == 'Alexandria'], label="Alexandria")

  ax.xaxis.set_major_locator(days_one_interval)
  ax.xaxis.set_major_formatter(day_fmt)
  #ax.xaxis.set_minor_locator(days_one_interval)

#  # round to nearest months
  datemin = np.datetime64(df_seven_days['date'][0], 'D')
  datemax = np.datetime64(df_seven_days['date'][max_index], 'D')
  ax.set_xlim(datemin, datemax)

  plt.tight_layout()
  plt.text
  plt.legend()
  fig_buffer = BytesIO()
  plt.savefig(fig_buffer, format='png', dpi=300)

  # Save the figure as a HttpPesponse
  response = HttpResponse(content_type='image/png')
  response.write(fig_buffer.getvalue())

  fig_buffer.close()

  return response

def plt_nova_last_seven_days_mvg_deaths(request):
  last_seven_days_obj = VwNovaSevenMvgAvg.objects.using('data').order_by('date', 'admin2').values()
  df_seven_days = pd.DataFrame(list(last_seven_days_obj))
  df_seven_days['date'] = pd.to_datetime(df_seven_days['date'])

  num_rows = len(df_seven_days)
  max_index = num_rows - 1

  fig, ax = plt.subplots()
  ax.set_title('Last 7 days Moving Average - New Deaths Per Million Population')
  ax.plot('date', 'mvg_deaths', data=df_seven_days.loc[df_seven_days['admin2'] == 'Fairfax'], label="Fairfax")
  ax.plot('date', 'mvg_deaths', data=df_seven_days.loc[df_seven_days['admin2'] == 'Arlington'], label="Arlington")
  ax.plot('date', 'mvg_deaths', data=df_seven_days.loc[df_seven_days['admin2'] == 'District of Columbia'], label="District of Columbia")
  ax.plot('date', 'mvg_deaths', data=df_seven_days.loc[df_seven_days['admin2'] == 'Montgomery'], label="Montgomery")
  ax.plot('date', 'mvg_deaths', data=df_seven_days.loc[df_seven_days['admin2'] == 'Loudoun'], label="Loudoun")
  ax.plot('date', 'mvg_deaths', data=df_seven_days.loc[df_seven_days['admin2'] == 'Alexandria'], label="Alexandria")

  ax.xaxis.set_major_locator(days_one_interval)
  ax.xaxis.set_major_formatter(day_fmt)
  #ax.xaxis.set_minor_locator(days_one_interval)

#  # round to nearest months
  datemin = np.datetime64(df_seven_days['date'][0], 'D')
  datemax = np.datetime64(df_seven_days['date'][max_index], 'D')
  ax.set_xlim(datemin, datemax)

  plt.tight_layout()
  plt.text
  plt.legend()
  fig_buffer = BytesIO()
  plt.savefig(fig_buffer, format='png', dpi=300)

  # Save the figure as a HttpPesponse
  response = HttpResponse(content_type='image/png')
  response.write(fig_buffer.getvalue())

  fig_buffer.close()

  return response

def datatable(request):

  page = request.GET.get('page', 1)
  filterby = request.GET.get('filterby', "")
  filterbycode = ""
  rows_per_page = 15
  start_row = (int(page) - 1) * rows_per_page
  end_row = start_row + rows_per_page

  if filterby != "":
    if start_row == 0:
      novaf = DmvMovingAverage.objects.using('data').filter(admin2=filterby).order_by('admin2', 'date')[:end_row]
    else:
      novaf = DmvMovingAverage.objects.using('data').filter(admin2=filterby).order_by('admin2', 'date')[start_row:end_row]
      filterbycode = "&filterby=" + filterby

      if novaf.count() == 0:
        novaf = DmvMovingAverage.objects.using('data').filter(admin2=filterby).order_by('admin2', 'date')[:rows_per_page]
  else:
    if start_row == 0:
      novaf = DmvMovingAverage.objects.using('data').order_by('admin2', 'date')[:end_row]
    else:
      novaf = DmvMovingAverage.objects.using('data').order_by('admin2', 'date')[start_row:end_row]

  datajson = serializers.serialize('json',novaf)

  data_count = datatable_count(filterby)

  jsonadd = { "count": data_count }

  data_object = json.loads(datajson)
  data_object.insert(0,jsonadd)

  data_return = json.dumps(data_object)

  return HttpResponse(data_return,content_type="text/json-comment-filterered")

def datatable_count(filterby):

  filterbycode = ""

  if filterby != "":
    count = DmvMovingAverage.objects.using('data').filter(admin2=filterby).count()

  else:
    count = DmvMovingAverage.objects.using('data').all().count()

  return count

def counties_json(request):
  # field name is county -- admin2 in the main table
  counties_obj = Counties.objects.using('data').order_by('county')
  counties = serializers.serialize('json',counties_obj)
  return HttpResponse(counties, content_type="text/json-comment-filterered")

def counties_total_cases_json(request):
  total_cases_obj = MvwNovaTotalCases.objects.using('data').order_by('admin2')
  total_cases = serializers.serialize('json',total_cases_obj)
  return HttpResponse(total_cases, content_type="text/json-comment-filterered")

def counties_daily_cases_json(request):
  daily_cases_obj = MvwNovaDailyCases.objects.using('data').order_by('admin2')
  daily_cases = serializers.serialize('json',daily_cases_obj)
  return HttpResponse(daily_cases, content_type="text/json-comment-filterered")

def counties_seven_mvg_json(request):
  seven_mvg_obj = MvwNovaSevenMvgAvg.objects.using('data').order_by('admin2', 'date')
  seven_mvg = serializers.serialize('json', seven_mvg_obj)
  return HttpResponse(seven_mvg, content_type="text/json-comment-filterered")

def population_table(request):
  population_obj = MvwCountyPopulation.objects.using('data').order_by('ctyname')
  population = serializers.serialize('json', population_obj)
  return HttpResponse(population, content_type="text/json-comment-filterered")
