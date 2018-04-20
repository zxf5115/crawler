#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------
#  程序：selenium_so.py
#  版本：1.0
#  作者：zhangxiaofei
#  日期：2018-004-20
#  语言：Python 3.6.x
#  操作：python selenuium.py
#  功能：结合crontab定时启动每天自动登录so网站,刷银牌用
#-------------------------------------------------------------------------

import configparser

class Conf(object):

  def __init__(self):

    # 新建配置对象
    self.conf = configparser.ConfigParser()

    # 读取配置文件
    self.conf.read("config/config.ini")


  def get_log_info(self):

    level = self.conf.get('log', 'level')

    return level




  def get_redis_info(self):

    host = self.conf.get("redis", "host")
    port = self.conf.get("redis", "port")

    return host, port
