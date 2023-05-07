from django.db import models
from db.base_model import BaseModel
# Create your models here.

class AirData(BaseModel):
    '''空气参数'''
    Air_wendu = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='空气温度')
    Air_shidu = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='空气湿度')

    class Meta:
        db_table = 'df_airdata'
        verbose_name = '空气数据'
        verbose_name_plural = verbose_name

class GroundData(BaseModel):
    '''土壤数据'''
    tu_place = models.CharField(max_length=20,verbose_name='土地位置')
    tu_depth = models.IntegerField(default=20,verbose_name='土壤深度')
    tu_shidu = models.DecimalField(max_digits=10,decimal_places=1,verbose_name='土壤湿度')
    tu_wendu = models.DecimalField(max_digits=10,decimal_places=1,verbose_name='土壤温度')

    class Meta:
        db_table = 'df_grounddata'
        verbose_name = '土壤数据'
        verbose_name_plural = verbose_name
