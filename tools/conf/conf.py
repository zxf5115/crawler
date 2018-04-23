#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：selenium_so.py
# 作者：zhangxiaofei
# 日期：2018-004-20
# 功能：结合crontab定时启动每天自动登录so网站,刷银牌用
# -------------------------------------------------------------------------

import configparser

class Conf(object):

  def __init__(self):

    # 新建配置对象
    self.conf = configparser.ConfigParser()

    # 读取配置文件
    self.conf.read("config/config.ini", encoding="utf-8")


  # -----------------------------------------------------------------------
  # 获取 获取IP 相关 配置信息

  def get_ip_conf_info(self):

    path    = self.conf.get('ip', 'path')
    field   = self.conf.get('ip', 'field')
    message = self.conf.get('ip', 'message')

    proxy_ip_url = self.conf.get('ip', 'proxy_ip_url')
    validation_url = self.conf.get('ip', 'validation_url')

    return path, field, message, proxy_ip_url, validation_url



  # -----------------------------------------------------------------------
  # 获取 User Agent 配置信息

  def get_user_agent_conf_info(self):

    path    = self.conf.get('user_agent', 'path')
    field   = self.conf.get('user_agent', 'field')
    message = self.conf.get('user_agent', 'message')

    return path, field, message



  # -----------------------------------------------------------------------
  # 获取 Log 配置信息

  def get_log_conf_info(self):

    level = self.conf.get('log', 'level')

    return level



  # -----------------------------------------------------------------------
  # 获取 Redis 配置信息

  def get_redis_conf_info(self):

    host = self.conf.get("redis", "host")
    port = self.conf.get("redis", "port")

    return host, port
