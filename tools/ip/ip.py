#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：ip.py
# 作者：zhangxiaofei
# 日期：2018-04-20
# 功能：用于初始化数据
# -------------------------------------------------------------------------

import requests
import threading
from bs4 import BeautifulSoup

from ..file.file import File
from ..check.check import Check
from ..datetime.datetime import Datetime

class Ip(object):

  # -----------------------------------------------------------------------
  # 初始化可用 IP 代理地址

  def init_ip_address():

    self.redis.file_push(self.path, self.field, self.message)




  # -----------------------------------------------------------------------
  # 得到代理 IP 网站访问地址

  def get_proxy_ip_url(self):

    # 读取代理 IP 网站的地址
    return self.file.read(self.proxy_ip_url, 'r')




  # -----------------------------------------------------------------------
  # 从代理 IP 网站上，获得可用IP地址

  # ip类型,页码,目标url,存放ip的路径
  def get_ip_address(self, category, page):

    try:

      ip_urls = self.get_proxy_ip_url()

      "%s%d" % (ip_urls[0].strip(), 1)

      url = "%s%d" % (ip_urls[category].strip(), page) # 配置url

      # 随机获取一个 User Agent 信息
      ua = self.user_agent.get_user_agent().strip()

      headers = {'User-Agent': ua}

      html=requests.get(url=url,headers=headers,timeout = 5).text

      soup=BeautifulSoup(html,'lxml')

      all=soup.find_all('tr',class_='odd')

      for i in all:

          t=i.find_all('td')

          ip=t[1].text+':'+t[2].text
          self.logger.info(ip)
          is_avail = self.check.check_ip(self.validation_url, headers, ip)
          self.logger.info(ip)
          if is_avail == True:

              self.redis.lpush(self.field, ip)

              self.logger.info(ip)

    except Exception as e:

      self.logger.error(e)




  # -----------------------------------------------------------------------
  # 多线程抓取ip入口

  def get_ip(self):

    try:

      # 如果redis中存在代理ip数据，清空
      self.redis.exists(self.field)

      # 开始时间
      start = Datetime.get_now_time()

      threads = []

      # 四种类型ip,每种类型取前三页,共12条线程
      for category in range(1):

        for page in range(1, 2):

          t = threading.Thread(target = self.get_ip_address,
                               args=(category, page))

          threads.append(t)

      self.logger.info('开始爬取代理ip')

      for s in threads: # 开启多线程爬取
         s.start()

      for e in threads: # 等待所有线程结束
         e.join()

      self.logger.info('爬取完成')

      end = Datetime.get_now_time() # 结束时间

      diff = Datetime.get_time_diff(start, end)  # 计算耗时

      # 读取爬到的ip数量
      ips = self.redis.llen(self.field)

      self.logger.info('一共爬取代理ip: %s 个,共耗时: %s \n' % (len(ips), diff))

    except Exception as e:

      self.logger.error(e)



  # -----------------------------------------------------------------------
  # 从代理 IP 网站上，获得可用IP地址

  def __init__(self, redis, user_agent, conf, logger):

    self.redis = redis

    self.user_agent = user_agent

    self.logger = logger

    self.file = File(self.logger)

    self.path,\
    self.field,\
    self.message,\
    self.proxy_ip_url,\
    self.validation_url = conf.get_ip_conf_info()

    self.check = Check(self.logger)

    # 开始多线程抓取IP地址信息
    self.get_ip()

    # ua = self.user_agent.get_user_agent()
    # self.logger.info(ua)

    # ip_urls = self.get_proxy_ip_url()

    # url = "%s%d" % (ip_urls[0].strip(), 1) # 配置url

    # print(url)


  # #-------------------------------------------------------获取代理方法----------------------------------------------------
  # # 免费代理 XiciDaili
  # def findip(type,pagenum,targeturl,path): # ip类型,页码,目标url,存放ip的路径
  #     list={'1': 'http://www.xicidaili.com/nt/', # xicidaili国内普通代理
  #           '2': 'http://www.xicidaili.com/nn/', # xicidaili国内高匿代理
  #           '3': 'http://www.xicidaili.com/wn/', # xicidaili国内https代理
  #           '4': 'http://www.xicidaili.com/wt/'} # xicidaili国外http代理
  #     url=list[str(type)]+str(pagenum) # 配置url
  #     headers = getheaders() # 定制请求头
  #     html=requests.get(url=url,headers=headers,timeout = 5).text
  #     soup=BeautifulSoup(html,'lxml')
  #     all=soup.find_all('tr',class_='odd')
  #     for i in all:
  #         t=i.find_all('td')
  #         ip=t[1].text+':'+t[2].text
  #         is_avail = checkip(targeturl,ip)
  #         if is_avail == True:
  #             write(path=path,text=ip)
  #             print(ip)
  # #-----------------------------------------------------多线程抓取ip入口---------------------------------------------------
  # def getip(targeturl,path):
  #      truncatefile(path) # 爬取前清空文档
  #      start = datetime.datetime.now() # 开始时间
  #      threads=[]
  #      for type in range(4):   # 四种类型ip,每种类型取前三页,共12条线程
  #          for pagenum in range(3):
  #              t=threading.Thread(target=findip,args=(type+1,pagenum+1,targeturl,path))
  #              threads.append(t)
  #      print('开始爬取代理ip')
  #      for s in threads: # 开启多线程爬取
  #          s.start()
  #      for e in threads: # 等待所有线程结束
  #          e.join()
  #      print('爬取完成')
  #      end = datetime.datetime.now() # 结束时间
  #      diff = gettimediff(start, end)  # 计算耗时
  #      ips = read(path)  # 读取爬到的ip数量
  #      print('一共爬取代理ip: %s 个,共耗时: %s \n' % (len(ips), diff))

  # #-------------------------------------------------------启动-----------------------------------------------------------
  # if __name__ == '__main__':
  #     path = 'ip.txt' # 存放爬取ip的文档path
  #     targeturl = 'http://www.cnblogs.com/TurboWay/' # 验证ip有效性的指定url
  # getip(targeturl,path)


  # def validateip(useragents):
  #     url = "http://ip.chinaz.com/getip.aspx"
  #     with open("proxy", "r") as f:
  #         lines = f.readlines()
  #     with open("proxy", "w") as f_w:
  #         for line in lines:
  #             ip =line.strip("\n")
  #             if ip.strip():
  #                 try:
  #                     # 下面是模拟浏览器进行访问
  #                     req = urllib2.Request(url)
  #                     req.add_header("User-Agent", random.choice(useragents))
  #                     req.add_header("Host", "ip.chinaz.com")
  #                     req.add_header("Connection", "close")
  #                     # 下面是使用ip代理进行访问
  #                     proxy_handler = urllib2.ProxyHandler({"http": ip})
  #                     opener = urllib2.build_opener(proxy_handler, urllib2.HTTPHandler)
  #                     urllib2.install_opener(opener)
  #                     try:
  #                         html = urllib2.urlopen(req, timeout=20).read()
  #                         if (html.find('address') != -1):
  #                             f_w.write(ip+'\n')
  #                             print u'代理IP:' + ip + u' 有效'
  #                         else:
  #                             print u'代理IP:' + ip + u' 已经失效'
  #                             continue
  #                     except Exception, e:
  #                         print u'代理IP:' + ip + u'已经失效'
  #                         continue
  #                 except Exception, e:
  #                     print ip + u'未知错误'
  #                     continue
  #             else:
  #                 continue
  #     print u'IP校验完成'
