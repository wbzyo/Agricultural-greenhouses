from django.db import models
from db.base_model import BaseModel
# Create your models here.
class ControlEexel(BaseModel):
    '''控制表'''

    AUTO = {
        '0': "手动",
        '1': "自动",
    }

    AUTO.keys()

    AUTO_CHOICES ={
        (0,'手动'),
        (1,'自动')
    }
    auto_flag = models.SmallIntegerField(choices=AUTO_CHOICES,default=0)
    place = models.CharField(max_length=20,verbose_name='阀门位置')
    tu_depth = models.IntegerField(default=0,verbose_name='土壤深度')
    grow_circle = models.CharField(max_length=20,verbose_name='作物生长周期')
    start_time = models.DateTimeField(auto_now_add=False,verbose_name='计划开始时间')
    stop_time = models.DateTimeField(auto_now_add=False,verbose_name='计划结束时间')
    class Meta:
        db_table = 'df_controlexcel'
        verbose_name = '控制表'
        verbose_name_plural = verbose_name


class XiData(BaseModel):
    '''比例系数表'''
    grow_circle = models.ForeignKey('ControlEexel',verbose_name='生长周期外键',on_delete=models.CASCADE)
    Ke = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='系数Ke')
    Kec = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='系数Kec')
    Ku = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='系数Ku')

    class Meta:
        db_table = 'df_xidata'
        verbose_name = '比例系数表'
        verbose_name_plural = verbose_name

class FuzzySearch(BaseModel):
    '''Fuzzy查询表'''
    grow_circle = models.ForeignKey('ControlEexel', verbose_name='生长周期外键',on_delete=models.CASCADE)
    xi_data = models.ForeignKey('XiData',verbose_name='比例系数外键',on_delete=models.CASCADE)
    cha_value = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='差值')
    zhengteng_value = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='误差变化率')
    water_length = models.IntegerField(default=0,verbose_name='灌溉时间')
    class Meta:
        db_table = 'df_fuzzytable'
        verbose_name = 'fuzzy查询表'
        verbose_name_plural = verbose_name
