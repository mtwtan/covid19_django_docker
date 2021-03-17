# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Counties(models.Model):
    county = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'counties'


class DmvMovingAverage(models.Model):
    date = models.TextField(blank=True, null=True)
    numconfirmed = models.BigIntegerField(db_column='numConfirmed', blank=True, null=True)  # Field name made lowercase.
    numdeaths = models.BigIntegerField(db_column='numDeaths', blank=True, null=True)  # Field name made lowercase.
    numrecovered = models.BigIntegerField(db_column='numRecovered', blank=True, null=True)  # Field name made lowercase.
    admin2 = models.TextField(blank=True, null=True)
    province_state = models.TextField(blank=True, null=True)
    county = models.TextField(blank=True, null=True)
    numconfirmedperm = models.DecimalField(db_column='numConfirmedPerM', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    numdeathsperm = models.DecimalField(db_column='numDeathsPerM', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    numrecoveredperm = models.DecimalField(db_column='numRecoveredPerM', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    daybefore = models.BigIntegerField(db_column='dayBefore', blank=True, null=True)  # Field name made lowercase.
    change = models.BigIntegerField(blank=True, null=True)
    daybeforedeaths = models.BigIntegerField(db_column='dayBeforeDeaths', blank=True, null=True)  # Field name made lowercase.
    changedeaths = models.BigIntegerField(db_column='changeDeaths', blank=True, null=True)  # Field name made lowercase.
    daybeforerecovered = models.BigIntegerField(db_column='dayBeforeRecovered', blank=True, null=True)  # Field name made lowercase.
    changerecovered = models.BigIntegerField(db_column='changeRecovered', blank=True, null=True)  # Field name made lowercase.
    daybeforeperm = models.DecimalField(db_column='dayBeforePerM', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    changeperm = models.DecimalField(db_column='changePerM', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    daybeforedeathsperm = models.DecimalField(db_column='dayBeforeDeathsPerM', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    changedeathsperm = models.DecimalField(db_column='changeDeathsPerM', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    daybeforerecoveredperm = models.DecimalField(db_column='dayBeforeRecoveredPerM', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    changerecoveredperm = models.DecimalField(db_column='changeRecoveredPerM', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    movingaverageperm = models.DecimalField(db_column='movingAveragePerM', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    movingaveragedeathsperm = models.DecimalField(db_column='movingAverageDeathsPerM', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    movingrecoveredperm = models.DecimalField(db_column='movingRecoveredPerM', max_digits=15, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dmv_moving_average'

class MvwCountyPopulation(models.Model):
    uid = models.AutoField(primary_key=True)
    id = models.IntegerField()
    population = models.BigIntegerField(blank=True, null=True)
    ctyname = models.TextField(blank=True, null=True)
    stname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mvw_county_population'


class MvwNovaDailyCases(models.Model):
    uid = models.AutoField(primary_key=True)
    id = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    admin2 = models.TextField(blank=True, null=True)
    dailycases = models.BigIntegerField(db_column='dailyCases', blank=True, null=True)  # Field name made lowercase.
    dailydeaths = models.BigIntegerField(db_column='dailyDeaths', blank=True, null=True)  # Field name made lowercase.
    dailycasesperm = models.DecimalField(db_column='dailyCasesPerM', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dailydeathsperm = models.DecimalField(db_column='dailyDeathsPerM', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mvw_nova_daily_cases'

class MvwNovaSevenMvgAvg(models.Model):
    uid = models.AutoField(primary_key=True)
    id = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    datediff = models.IntegerField(blank=True, null=True)
    admin2 = models.TextField(blank=True, null=True)
    mvg_cases = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    mvg_deaths = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mvw_nova_seven_mvg_avg'


class MvwNovaTotalCases(models.Model):
    uid = models.AutoField(primary_key=True)
    id = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    admin2 = models.TextField(blank=True, null=True)
    totalcases = models.BigIntegerField(db_column='totalCases', blank=True, null=True)  # Field name made lowercase.
    totaldeaths = models.BigIntegerField(db_column='totalDeaths', blank=True, null=True)  # Field name made lowercase.
    totalcasesperm = models.DecimalField(db_column='totalCasesPerM', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totaldeathsperm = models.DecimalField(db_column='totalDeathsPerM', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mvw_nova_total_cases'


class VwCountyPopulation(models.Model):
    id = models.IntegerField()
    population = models.BigIntegerField(blank=True, null=True)
    ctyname = models.TextField(blank=True, null=True)
    stname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vw_county_population'
        
class VwNovaDailyCases(models.Model):
    date = models.DateField(blank=True, null=True)
    admin2 = models.TextField(blank=True, null=True)
    dailycases = models.BigIntegerField(db_column='dailyCases', blank=True, null=True)  # Field name made lowercase.
    dailydeaths = models.DecimalField(db_column='dailyDeaths', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dailycasesperm = models.DecimalField(db_column='dailyCasesPerM', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dailydeathsperm = models.DecimalField(db_column='dailyDeathsPerM', max_digits=11, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vw_nova_daily_cases'


class VwNovaSevenMvgAvg(models.Model):
    date = models.DateField(blank=True, null=True)
    datediff = models.IntegerField(blank=True, null=True)
    admin2 = models.TextField(blank=True, null=True)
    mvg_cases = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    mvg_deaths = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vw_nova_seven_mvg_avg'


class VwNovaTotalCases(models.Model):
    date = models.DateField(blank=True, null=True)
    admin2 = models.TextField(blank=True, null=True)
    totalcases = models.BigIntegerField(db_column='totalCases', blank=True, null=True)  # Field name made lowercase.
    totaldeaths = models.BigIntegerField(db_column='totalDeaths', blank=True, null=True)  # Field name made lowercase.
    totalcasesperm = models.DecimalField(db_column='totalCasesPerM', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totaldeathsperm = models.DecimalField(db_column='totalDeathsPerM', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vw_nova_total_cases'

class Testcovid(models.Model):
    county = models.CharField(max_length=100)
    confirmed = models.IntegerField()
    death = models.IntegerField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'testcovid'
