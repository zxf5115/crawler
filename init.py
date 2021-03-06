#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：init.py
# 作者：zhangxiaofei
# 日期：2018-04-20
# 功能：用于初始化数据
# -------------------------------------------------------------------------

import logging

from tools.ip.ip import Ip
from tools.conf.conf import Conf
from tools.file.file import File
from tools.redis.redis import Redis
from tools.user_agent.user_agent import UserAgent

class Init:


  def get_level(self, conf):

    # 得到日志信息，当前只有日志级别
    log_level = conf.get_log_conf_info()

    if log_level == 'debug':

      return logging.DEBUG

    elif log_level == 'info':

      return logging.INFO

    else:

      return logging.WARNING


  # -----------------------------------------------------------------------
  # 初始化方法，用于数据初始化

  def __init__(self):

    try:

      conf = Conf()

      level = self.get_level(conf)

      # 初始化日志模块
      logging.basicConfig(level=level,
                        format="%(asctime)s %(module)s %(funcName)s[line:%(lineno)d] %(levelname)s %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")

      # 初始化Redis模块
      self.redis = Redis(conf, logging)

      # 生成 User Agent 对象
      user_agent = UserAgent(conf, self.redis, logging)

      # 将 User Agent 数据初始化到 Redis 中
      user_agent.init_user_agent()

      # 生成可用代理IP
      ip = Ip(self.redis, user_agent, conf, logging)

    except Exception as e:

      logging.error(e)


if __name__ == '__main__':

  Init()
