# -*-coding:utf-8-*-
__author__ = 'BING'
import requests,json,re

class apiUse(object):
    def __init__(self):
        self.getLatestApi = 'http://news-at.zhihu.com/api/4/news/latest'
        self.getNewApi = 'http://news-at.zhihu.com/api/4/news/'

        #headers信息
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT'
        self.headrs = {'User-Agent':self.user_agent}

    def access(self,url):
        self.mystr = requests.get(url,headers = self.headrs)
        return json.loads(self.mystr.text)

    def getLateset(self):
        return self.access(self.getLatestApi)

    def getNews(self,_id):
        return self.access(self.getNewApi+str(_id))

class singelNews(object):
    def __init__(self,api,_id):
        self.data = api.getNews(_id)

    def getbody(self):
        return self.data['body']

    def gettitle(self):
        return self.data['title']

    def getimage(self):
        return self.data['image']

    def getid(self):
        return self.data['id']

    def getcss(self):
        return self.data['css']

class latestNews():
    def __init__(self,api):
        self.data = api.getLateset()

    def getdate(self):
        return self.data['date']

    def getimage(self,index):
        return self.data['stories'][index].get('image')

    def gettitle(self,index):
        return self.data['stories'][index].get('title')

    def getid(self,index):
        return self.data['stories'][index].get('id')

    def getnum(self):
        return len(self.data['stories'])

if __name__=='__main__':
    api = apiUse()
    latest = latestNews(api)
    print u'当前的知乎日报消息有:',int(latest.getnum()),u'条'
    for index in range(int(latest.getnum())):
        print u'标题:',latest.gettitle(index),u'id号:',latest.getid(index)

    while True:
        id = raw_input(u'输入消息id号:')
        news = singelNews(api,int(id))
        print u'标题:',news.gettitle()
        print u'body:',news.getbody()
        raw_input()



