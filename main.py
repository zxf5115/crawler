#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：main.py
# 作者：zhangxiaofei
# 日期：2018-04-20
# 功能：程序入口文件
# -------------------------------------------------------------------------

import re
import random
import requests

from tools.conf.conf import Conf

# class Crawler(object):


  # -----------------------------------------------------------------------
  # 初始化方法

def run(url, user_agent):

  '''参数引入及头信息'''
  if len(user_agent) < 10:
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0'

  # 此处修改头字段,
  headers = {
    'Host': "www.51sole.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    'Cache-Control': 'no-cache',
    "Connection": "keep-alive",
    "User-Agent": user_agent,
    'Referer': 'http://www.51sole.com/'
  }

  try:
    html = requests.get(url, headers=headers, timeout=20).text
    # print html
    return html

  except Exception as e:
    print(e)






if __name__ == '__main__':

  conf = Conf()


  url = conf.get_crawler_conf_info()

  # 导入数据集并随机获取一个User-Agent
  user_agent_list = []
  f = open('user_agent.txt', 'r')
  for date_line in f:

    user_agent_list.append(date_line.strip('\r\n'))
  user_agent = random.choice(user_agent_list)

  # 发起请求
  html_body = run(url, user_agent)
  print(html_body)
  exit()


#-------------------测试结果-------------------------------
# 将此链接放在浏览器中可以直接播放,虽然有广告....至于别的数据太简单那就不抓了.
#[
# u'http://player.youku.com/player.php/sid/XMTgzNDI0MjkzNg==/v.swf',
# u'http://player.youku.com/player.php/sid/XMTgzNDI0MjkzNg==/v.swf'
#]
