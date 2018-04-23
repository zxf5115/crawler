#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：init.py
# 作者：zhangxiaofei
# 日期：2018-04-20
# 功能：用于初始化数据
# -------------------------------------------------------------------------

from tools.redis.redis import Redis
from tools.conf.conf import Conf
from tools.log.logger import Logger
from tools.ip.ip import Ip
from tools.user_agent.user_agent import UserAgent
from tools.file.file import File

class Init(object):


  # -----------------------------------------------------------------------
  # 初始化方法，用于数据初始化

  def __init__(self):

    try:

      conf = Conf()

      # 初始化日志模块
      Logger.init(conf)

      # 初始化Redis模块
      self.redis = Redis(conf, Logger)

      # 生成 User Agent 对象
      user_agent = UserAgent(conf, self.redis, Logger)

      # 将 User Agent 数据初始化到 Redis 中
      user_agent.init_user_agent()

      # 生成可用代理IP
      ip = Ip(self.redis, user_agent, conf, Logger)

    except Exception as e:

      Logger.error(e)


if __name__ == '__main__':

  Init()
