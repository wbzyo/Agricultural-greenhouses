import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render,reverse,redirect
from django.views.generic import View

from apps.news.models import News,NewsInfo,NewsSwiper,Comment
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from bigpeng import settings

#http://127.0.0.1:8000/news/luntan
class LuntanView(View):
    '''论坛'''
    def get(self,request):
        # 组织上下文
        news_info = NewsInfo.objects.all()
        for new_info in news_info:
            new = News.objects.get(id=new_info.news_id)
            new_info.editor = new.editor #  动态的添加属性
            new_info.title = new.title  # 动态的添加属性
        news_swiper = NewsSwiper.objects.all()
        for new_swiper in news_swiper:
            new = News.objects.get(id=new_swiper.news_id)
            new_swiper.title = new.title  # 动态的添加属性
        # for new_info in news_info:
        #     print(new_info.editor)
        #     print(new_info.title)
        contexts = {
            'news_info':news_info,
            'news_swiper':news_swiper,
        }
        return render(request,'luntan.html',contexts)


    def post(self,request):
        username = request.POST.get('username')
        return JsonResponse({'username':username})



#http://127.0.0.1:8000/news/write
class WriteView(LoginRequiredMixin,View):
    '''发布帖子'''
    def get(self,request):
        return render(request,'write_message.html')

    def post(self,request):
        '''接受内容'''
        user = request.user
        content = request.POST.get('content')
        title = request.POST.get('title')
        info = request.POST.get('info')
        image = request.FILES.get('img')
        path = default_storage.save('news/'+image.name,ContentFile(image.read()))
        print(path)
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        print(path)
        try:
            news = News.objects.create(title=title,news_content=content,editor=user)# 插入一条数据
            NewsInfo.objects.create(news_info=info,news_image=tmp_file,news_id=news.id)# 插入到news_info表
        except Exception :
            return render(request,'write_message.html')

        return redirect(reverse('news:luntan'))



# /news/detail/7

class DetailView(LoginRequiredMixin,View):
    '''详情'''
    # 使用方法同时返回帖子和评论，在评论模板中，comments.user可以获取当前登陆的用户名
    def get(self,request,id):
        news = News.objects.get(id=id)
        comments = Comment.objects.filter(news_id=id)
        comments=comments[::-1]
        print(comments)
        params = {
            'news':news,
            'comments':comments
        }
        return render(request,'news_detail.html',params)

    def post(self,request,id):
        user = request.user
        content = request.POST.get('content')
        Comment.objects.create(is_delete=0,user_id=user.id,news_id=id,comment_content=content)
        return redirect(reverse('news:detail',kwargs={'id':id})) # 重定向并且传递参数










