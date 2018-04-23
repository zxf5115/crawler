#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：ip.py
# 作者：zhangxiaofei
# 日期：2018-04-20
# 功能：用于初始化数据
# -------------------------------------------------------------------------

import requests

class Check(object):


  # -----------------------------------------------------------------------
  # 检查IP是否可以使用

  def check_ip(self, targeturl, headers, ip_address):

    proxies = {"http": "http://"+ip_address, "https": "http://"+ip_address}  # 代理ip

    try:

        response = requests.get(url=targeturl, proxies = proxies, headers = headers, timeout = 5).status_code

        if response == 200 :

            return True

        else:

            return False

    except Exception as e:

        self.logger.error(e)




  # -----------------------------------------------------------------------
  # 初始化方法

  def __init__(self, logger):

    self.logger = logger
