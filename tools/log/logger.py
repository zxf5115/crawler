#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------
#  程序：logger.py
#  版本：1.0
#  作者：zhangxiaofei
#  日期：2018-04-20
#  语言：Python 3.6.x
#  操作：python logger.py
#  功能：用于操作日志记录
#-------------------------------------------------------------------------

import logging

class Logger(object):

  @classmethod
  def init(cls, log_level = 'info'):

    if log_level == 'debug':

        level = logging.DEBUG

    elif log_level == 'info':

        level = logging.INFO

    else:

        level = logging.WARNING

    logging.basicConfig(level=level,
                        format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
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
