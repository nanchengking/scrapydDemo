echo 开始运行第一个爬虫
curl http://localhost:6800/schedule.json -d project=scrapydDemo -d spider=Spider_One
echo 开始云顶第二个爬虫
curl http://localhost:6800/schedule.json -d project=scrapydDemo -d spider=Spider_Two


