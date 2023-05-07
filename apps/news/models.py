from django.db import models
from db.base_model import BaseModel

from tinymce.models import HTMLField
# Create your models here.

class Comment(BaseModel):
    '''评论表'''
    user = models.ForeignKey('user.User',verbose_name='用户',on_delete=models.CASCADE)
    news = models.ForeignKey('News',verbose_name='新闻',on_delete=models.CASCADE)
    comment_content = models.TextField(verbose_name='评论内容')
    class Meta:
        db_table = 'df_comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name

        ordering = ('create_time',)

    # 控制台显示信息
    # def __str__(self):
    #     return 'Comment by {} on {}'.format(self.user.username, self.news.title)


class News(BaseModel):
    '''新闻表'''
    title = models.CharField(max_length=256,verbose_name='标题')
    news_content = HTMLField(blank=True,verbose_name='新闻内容')
    editor = models.CharField(max_length=20,verbose_name='编辑人')
    class Meta:
        db_table = 'df_news'
        verbose_name = '新闻'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title


class NewsInfo(BaseModel):
    '''新闻简介'''
    news = models.ForeignKey('News',verbose_name='新闻',on_delete=models.CASCADE)
    news_info = models.TextField(max_length=256,verbose_name='新闻简介')
    news_image = models.ImageField(upload_to='news',verbose_name='新闻图片')
    class Meta:
        db_table = 'df_newsinfo'
        verbose_name = '新闻简介'
        verbose_name_plural = verbose_name



class NewsSwiper(BaseModel):
    '''滚动新闻'''
    news = models.ForeignKey('News', verbose_name='新闻', on_delete=models.CASCADE)
    news_info = models.TextField(max_length=256, verbose_name='新闻简介')
    news_image = models.ImageField(upload_to='news', verbose_name='新闻图片')
    class Meta:
        db_table = 'df_newsswiper'
        verbose_name = '滚动新闻'
        verbose_name_plural = verbose_name
