#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------
#  程序：file.py
#  作者：zhangxiaofei
#  日期：2018-04-20
#  功能：用于文件操作
#-------------------------------------------------------------------------

class File(object):

  def __init__(self, logger):

    self.logger = logger





  def open(self, path, operation, encoding='utf-8'):

    try:

      return self.handle = open(path, operation)

    except Exception as e:

      self.logger.error(e)





  def write(self, content):

    try:

      return self.handle.write(content)

    except Exception as e:

      self.logger.error(e)





  def read(self, count = ''):

    try:

      return self.handle.read(count)

    except Exception as e:

      self.logger.error(e)




  def clear(self):

    try:

      return self.handle.truncate()

    except Exception as e:

      self.logger.error(e)





  def close(self):

    try:

      return self.handle.close()

    except Exception as e:

      self.logger.error(e)
