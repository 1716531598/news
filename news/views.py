from django.shortcuts import render
from django.http import JsonResponse
import json
from news.models import News
# Create your views here.
def newslistd(request):
   res = {"sucess":True, "result":None,"total_count":0}
   news = News.objects.all().order_by('-published_at')[:100]
   result = []
   for new in news:
      item = {}
      source={}
      item['author']=new.author
      item['title']=new.title
      item["description"]=new.description
      item['url']=new.url
      item['image']=new.image
      item['published_at']=new.published_at
      item['content']=new.content
      source['id'] = new.news_source.source_id
      source['name'] = new.news_source.source_name
      item['source'] = source
      result.append(item)
   res['total_count'] = news.count()
   res['result'] = result
   return JsonResponse(res)
def index(request):
   res={}
   res = News.objects.order_by('-published_at').all()[:20] # 获取最进的20条数据
   return render(request,"index.html",{'res':res})