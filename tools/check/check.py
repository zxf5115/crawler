#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：check.py
# 作者：zhangxiaofei
# 日期：2018-04-22
# 功能：用于检查的类
# -------------------------------------------------------------------------

import requests

class Check:


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

        return False




  # -----------------------------------------------------------------------
  # 初始化方法

  def __init__(self, logger):

    self.logger = logger
