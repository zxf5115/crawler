#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：main.py
# 作者：zhangxiaofei
# 日期：2018-04-20
# 功能：程序入口文件
# -------------------------------------------------------------------------

import logging
from tools.conf.conf import Conf
from tools.crawler.crawler import Crawler

def get_level(conf):

  # 得到日志信息，当前只有日志级别
  log_level = conf.get_log_conf_info()

  if log_level == 'debug':

    return logging.DEBUG

  elif log_level == 'info':

    return logging.INFO

  else:

    return logging.WARNING

from tools.conf.conf import Conf


if __name__ == '__main__':

  conf = Conf()

  level = get_level(conf)

  # 初始化日志模块
  logging.basicConfig(level=level,
                    format="%(asctime)s %(module)s %(funcName)s[line:%(lineno)d] %(levelname)s %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")


  Crawler(conf, logging)


