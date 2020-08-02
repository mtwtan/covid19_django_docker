from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from django.template.response import TemplateResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import FilterByCountyForm

# Create your views here.
from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

from nova.models import DmvMovingAverage
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

# Create your views here.
years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
days = mdates.DayLocator(interval=5) # every day
month_fmt = mdates.DateFormatter('%m-%y')
day_fmt = mdates.DateFormatter('%d')

nova = DmvMovingAverage.objects.using('data').all().order_by('county', 'date').values()

df_nova = pd.DataFrame(list(nova))
df_nova['date'] = pd.to_datetime(df_nova['date'])
#df_nova['movingaveragedeaths'] = pd.to_numeric(df_nova['movingaveragedeaths'])
df_index = df_nova.index
num_rows = len(df_index)
max_index = num_rows - 1

rows_per_page = 30


def plt_nova_total_cases_view(request):

  fig, ax = plt.subplots()
  ax.set_title('Confirmed Cases')
  ax.plot('date', 'numconfirmed', data=df_nova.loc[df_nova['county'] == 'Fairfax'], label="Fairfax")
  ax.plot('date', 'numconfirmed', data=df_nova.loc[df_nova['county'] == 'Arlington'], label="Arlington")
  ax.plot('date', 'numconfirmed', data=df_nova.loc[df_nova['county'] == 'District of Columbia'], label="District of Columbia")
  ax.plot('date', 'numconfirmed', data=df_nova.loc[df_nova['county'] == 'Montgomery'], label="Montgomery")
  ax.plot('date', 'numconfirmed', data=df_nova.loc[df_nova['county'] == 'Loudoun'], label="Loudoun")
  ax.plot('date', 'numconfirmed', data=df_nova.loc[df_nova['county'] == 'Alexandria'], label="Alexandria")

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
  plt.savefig(fig_buffer, format='png', dpi=150)

  # Save the figure as a HttpPesponse
  response = HttpResponse(content_type='image/png')
  response.write(fig_buffer.getvalue())

#  image_base64 = base64.b64encode(fig_buffer.getvalue()).decode('utf-8').replace('\n','')

  fig_buffer.close()

  return response