#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：crawler.py
# 作者：zhangxiaofei
# 日期：2018-04-24
# 功能：数据抓取类
# -------------------------------------------------------------------------

import json
import requests
import threading
from bs4 import BeautifulSoup

from ..conf.conf import Conf
from ..redis.redis import Redis
from ..datetime.datetime import Datetime

class Crawler(object):


  # -----------------------------------------------------------------------
  # 得到 header 头信息

  def get_headers(self, user_agent):

    # 得到配置文件中的headers信息
    header = self.conf.get_header_conf_info()

    # 重新定义 user agent 信息
    user_agent = {"User-Agent": user_agent}

    # 替换配置文件中的 user agent 信息
    header = json.loads(header)

    header.update(user_agent)

    return header




  # -----------------------------------------------------------------------
  # 得到页面数据

  def get_html_info(self, url, field):

    try:

      # 获取redis中ip信息的field
      ip_field = self.conf.get_ip_field_conf_info()

      # 获取redis中user agent信息的field
      user_agent_field = self.conf.get_user_agent_field_conf_info()

      # 随机获取ip地址
      ip_address = self.redis.srandmember(ip_field)

      ip_address = ip_address[0].decode().strip()

      proxy = { "http": "http://"+ip_address, "https": "http://"+ip_address}

      # 随机获取 user agent 信息
      user_agent = self.redis.srandmember(user_agent_field)

      user_agent = user_agent[0].decode().strip()


      # 得到真实header头信息
      header = self.get_headers(user_agent)

      html = requests.get(url, headers = header, proxies=proxy, timeout=30).text

      soup=BeautifulSoup(html,'html.parser')

      data = soup.find_all('div', class_ = 'hy_companylist')


      self.redis.sadd(field, data)

      # return html

    except Exception as e:

      self.logger.error(e)




  # -----------------------------------------------------------------------
  # 多线程抓取数据

  def run(self):

    try:

      # 开始时间
      start = Datetime.get_now_time()

      threads = []

      # 四种类型ip,每种类型取前三页,共12条线程
      for vo in range(1, self.page):

        url = "%s%d" % (self.url,vo)

        t = threading.Thread(target = self.get_html_info,
                             args=(url,vo))

        threads.append(t)

      self.logger.info('开始爬取数据')

      # 开启多线程爬取
      for thread_start in threads:
        thread_start.start()

      # 等待所有线程结束
      for thread_end in threads:
        thread_end.join()

      self.logger.info('爬取完成')

      end = Datetime.get_now_time() # 结束时间

      diff = Datetime.get_time_diff(start, end)  # 计算耗时

      # 读取爬到的ip数量
      ips = self.redis.scard('page_info')

      self.logger.info('一共爬取页面: %s 个,共耗时: %s \n' % (ips, diff))

    except Exception as e:

      self.logger.error(e)





  # -----------------------------------------------------------------------
  # 初始化方法

  def __init__(self, conf, logger):

    self.conf = conf

    self.logger = logger

    # 初始化Redis模块
    self.redis = Redis(self.conf, self.logger)

    self.url, self.page = conf.get_crawler_conf_info()

    self.run()
