from urllib import request
from django.db import models
import django_tables2 as tables
from django_mysql.models import ListCharField 


#######################################

class Detail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="layer name")
    BPL = models.FloatField( default=0, verbose_name="BPL value")
    MgO = models.FloatField( default=0, verbose_name="MgO value")
    MO = models.FloatField( default=0, verbose_name="MO value")
    SiO2 = models.FloatField( default=0, verbose_name="SiO2 value")
    CO2 = models.FloatField( default=0, verbose_name="CO2 value")
    Mix = models.FloatField( default=0, verbose_name="mix value")
    #Columns = ListCharField(
    #    base_field = models.CharField(max_length=10),
    #    size = info,
    #    max_length=(6 * 11),
    #    )
    def __id__(self):
        return self.id
    class Meta:
        ordering = ('-id',)


class layers(models.Model):
    id = models.OneToOneField(
        Detail,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    SM_BO = models.FloatField( default=0, verbose_name="SM_BO") 
    SM_MZ = models.FloatField( default=0, verbose_name="SM_MZ")                    
    MAT_NIF = models.FloatField( default=0, verbose_name="MAT_NIF")
    SFA = models.FloatField( default=0, verbose_name="SFA")
    DSP = models.FloatField( default=0, verbose_name="C2_Sup")
    C2_Sup = models.FloatField( default=0, verbose_name="C2_Sup")
    C4_inf = models.FloatField( default=0, verbose_name="C4_inf")
    C5_supA = models.FloatField( default=0, verbose_name="C5_supA")
    C5_inf = models.FloatField( default=0, verbose_name="C5_inf")
    C6_sm = models.FloatField( default=0, verbose_name="C6_sm")
    C6_inf = models.FloatField( default=0, verbose_name="C6_inf")
    