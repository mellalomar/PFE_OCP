from urllib import request
from django.db import models
import django_tables2 as tables
from django_mysql.models import ListCharField 


# Create your models here.
info = 5# request.Request.session.get('num column')
#request.session['Columns_name'] = ['name'].append([f"car {i}" for i in range(info)])

class Info(models.Model):
    name = models.CharField(max_length=100, verbose_name="full name")
    Columns = ListCharField(
        base_field = models.CharField(max_length=10),
        size = info,
        max_length=(6 * 11),
        )
    Columns_name = ['name'].append([f"car {i}" for i in range(info)])
#    for i in range(info):
#        Columns.append( models.CharField(max_length=100, verbose_name="CAR" )) 



class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="full name")
    car1 = models.CharField(max_length=100, verbose_name="CAR 1")
    car2 = models.CharField(max_length=100, verbose_name="CAR 2")
    car3 = models.CharField(max_length=100, verbose_name="CAR 3")


#######################################

class Details(models.Model):
    id=models.AutoField(primary_key=True)
    First_Name=models.CharField(max_length=30)
    Last_Name=models.CharField(max_length=30)
    City=models.CharField(max_length=30)


class Detail(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="layer name")
    car1 = models.CharField(max_length=100, verbose_name="car 1")
    car1 = models.CharField(max_length=100, verbose_name="car 2")
    #Columns = ListCharField(
    #    base_field = models.CharField(max_length=10),
    #    size = info,
    #    max_length=(6 * 11),
    #    )