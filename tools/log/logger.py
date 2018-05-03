#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：logger.py
# 作者：zhangxiaofei
# 日期：2018-04-20
# 功能：弃用，因为无法显示错误文件地址
# -------------------------------------------------------------------------

import logging

class Logger:


  # -----------------------------------------------------------------------
  # 弃用

  @classmethod
  def init(cls, conf):

    # 得到日志信息，当前只有日志级别
    log_level = conf.get_log_conf_info()

    if log_level == 'debug':

        level = logging.DEBUG

    elif log_level == 'info':

        level = logging.INFO

    else:

        level = logging.WARNING

    logging.basicConfig(level=level,
                        format="%(asctime)s %(module)s %(funcName)s[line:%(lineno)d] %(levelname)s %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")


  @classmethod
  def info(cls, message):

    logging.info(message)



  @classmethod
  def debug(cls, message):

    logging.debug(message)



  @classmethod
  def warning(cls, message):

    logging.warning(message)



  @classmethod
  def error(cls, message):

    logging.error(message)
    exit()
