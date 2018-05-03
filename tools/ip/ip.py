#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：ip.py
# 作者：zhangxiaofei
# 日期：2018-04-20
# 功能：操作IP的类
# -------------------------------------------------------------------------

import requests
import threading
from bs4 import BeautifulSoup

from ..file.file import File
from ..check.check import Check
from ..datetime.datetime import Datetime

class Ip:

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

      soup=BeautifulSoup(html,'html.parser')

      all=soup.find_all('tr',class_='odd')

      for i in all:

        t=i.find_all('td')

        ip=t[1].text+':'+t[2].text

        is_avail = self.check.check_ip(self.validation_url, headers, ip)

        if is_avail == True:

          self.redis.sadd(self.field, ip)

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
      for category in range(4):

        for page in range(1, 2):

          t = threading.Thread(target = self.get_ip_address,
                               args=(category, page))

          threads.append(t)

      self.logger.info('开始爬取代理ip')

      for thread_start in threads: # 开启多线程爬取
        thread_start.start()

      for thread_end in threads: # 等待所有线程结束
        thread_end.join()

      self.logger.info('爬取完成')

      end = Datetime.get_now_time() # 结束时间

      diff = Datetime.get_time_diff(start, end)  # 计算耗时

      # 读取爬到的ip数量
      ips = self.redis.scard(self.field)

      self.logger.info('一共爬取代理ip: %s 个,共耗时: %s \n' % (ips, diff))

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

