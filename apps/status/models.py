from django.db import models
from db.base_model import BaseModel
# Create your models here.
class Status(BaseModel):
    '''设备状态表'''
    status_name = models.CharField(max_length=20, verbose_name='设备名称')
    temprature = models.IntegerField(verbose_name='温度')
    vol = models.DecimalField(default=0,max_digits=10,decimal_places=2,verbose_name='电压')
    power = models.IntegerField(default=0,verbose_name='电量')
    place = models.CharField(max_length=20,verbose_name='放置位置')
    class Meta:
        db_table = 'df_status'
        verbose_name = '设备状态'
        verbose_name_plural = verbose_name


