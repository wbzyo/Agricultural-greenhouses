from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel

# Create your models here.
class User(AbstractUser,BaseModel):
    '''用户类'''
    address = models.CharField(max_length=20,verbose_name='地址')
    phone = models.CharField(max_length=11,verbose_name='联系电话')


    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户'



