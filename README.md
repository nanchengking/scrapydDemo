# scrapydDemo
A demo for scrapyd and scrapy which realise a simple distributed spider system.基于scrapy和scrapyd的分布式爬虫 <br><br>
环境搭建:  <br>
1.python2.7 安装pip <br>
2.pip install scrapy <br>
3.pip install scrapyd <br>
<br>
官方文档: <br> 
1.scrapy  http://doc.scrapy.org/en/latest/ <br> 
2.scrapyd http://scrapyd.readthedocs.org/en/latest/ <br>
<br>
<br>
云端部署问题
Run on server
<br>
1.首先:新打开一个终端运行 scrapyd,把scrapy 的server端口打开<br>
1.first of all :open a terminal to run : 'scrapyd' ,which start the scrapy's service<br>
2.运行命令进行部署: scrapyd-deploy default -p scrapydDemo<br>
2.then, open another terminal to run: 'scrapyd-deploy default -p scrapydDemo' , whitch deploy the project on service  <br><br>
例如下面<br>
For example as follows <br>
$ scrapyd-deploy default -p scrapydDemo(其实后面不用加,直接 scrapyd-deploy 就可以了)<br>
部署成功 返回如下信息/once the deploy is success,we get some infos as follows<br>
$ Packing version 1443188926(这个版本号是默认的当前时间戳)<br>
$ Deploying to project "scrapydDemo" in http://localhost:6800/addversion.json<br>
$ Server response (200):<br>
$ {"status": "ok", "project": "scrapydDemo", "version": "1443188926", "spiders": 1, "node_name": "nancheng-Lenovo-G480"}<br>
3.运行spider:  <br>
3.run spider on server<br>
 在根目录下面编写了一个url请求,这个请求就是下面这样,实际上,还是相当于发出了一个curl请求<br>
create a py file anywhere(of course,better in the project's root direction ),we code some thing to mock a nimal get request  like this (my named dmoz-start.py),then run it as py<br>
coding=utf-8   <br>      
 dmoz_data={'project':'scrapydDemo','spider':'dmoz'}<br>
 dmoz_data_urlencode=urllib.urlencode(dmoz_data)<br>
 requesurl="http://localhost:6800/schedule.json"<br>
 req=urllib2.Request(url=requesurl,data=dmoz_data_urlencode)<br>
 res_data=urllib2.urlopen(req)<br>
