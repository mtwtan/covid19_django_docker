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
    county = models.TextField(blank=True, null=True)
    numconfirmed = models.BigIntegerField(db_column='numConfirmed', blank=True, null=True)  # Field name made lowercase.
    numdeaths = models.BigIntegerField(db_column='numDeaths', blank=True, null=True)  # Field name made lowercase.
    daybefore = models.BigIntegerField(db_column='dayBefore', blank=True, null=True)  # Field name made lowercase.
    change = models.BigIntegerField(blank=True, null=True)
    daybeforedeaths = models.BigIntegerField(db_column='dayBeforeDeaths', blank=True, null=True)  # Field name made lowercase.
    changedeaths = models.BigIntegerField(db_column='changeDeaths', blank=True, null=True)  # Field name made lowercase.
    movingaverage = models.FloatField(db_column='movingAverage', blank=True, null=True)  # Field name made lowercase.
    movingaveragedeaths = models.FloatField(db_column='movingAverageDeaths')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dmv_moving_average'


class Testcovid(models.Model):
    county = models.CharField(max_length=100)
    confirmed = models.IntegerField()
    death = models.IntegerField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'testcovid'
