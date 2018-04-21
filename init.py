#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------
#  程序：init.py
#  作者：zhangxiaofei
#  日期：2018-04-20
#  功能：用于初始化数据
#-------------------------------------------------------------------------

from tools.redis.redis import Redis
from tools.config.conf import Conf
from tools.log.logger import Logger

class Init(object):


  def set_user_agent(self):

    path = 'config/user_agent.ini'
    field = 'user_agent'
    message = 'User Agent 初始化完成'

    self.redis.file_push(path, field, message)



  def set_ip_address(self):

    path = 'config/ip_address.ini'
    field = 'ip_address'
    message = 'IP Address 初始化完成'

    self.redis.file_push(path, field, message)



  def __init__(self):

    try:

      conf = Conf()

      # 得到日志信息，当前只有日志级别
      level = conf.get_log_info()

      # 得到Redis配置信息
      host, port = conf.get_redis_info()

      # 初始化日志模块
      Logger.init(level)

      # 初始化Redis模块
      self.redis = Redis(host, port, Logger)

      self.set_user_agent()

      self.set_ip_address()

    except Exception as e:

      Logger.error(e)


if __name__ == '__main__':

  Init()
