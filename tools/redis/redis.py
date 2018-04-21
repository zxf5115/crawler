#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------
#  程序：redis.py
#  版本：1.0
#  作者：zhangxiaofei
#  日期：2018-04-20
#  语言：Python 3.6.x
#  操作：python redis.py
#  功能：用于操作reids
#-------------------------------------------------------------------------

import redis

class Redis(object):


  def __init__(self, host, port, logger):

    try:

      # 打开连接
      self.handle = redis.Redis(host=host, port=port)
      self.logger = logger

    except Exception as e:

      self.logger.error(e)



  def exists(self, field):

    if self.handle.exists(field):

        self.handle.delete(field)


  def lpush(self, field, value):

    try:

      # 打开连接
      self.handle.lpush(field, value)

    except Exception as e:

      self.logger.error(e)



  def srandmember(self, field, number):

    try:

      self.handle.srandmember(field, number)

    except Exception as e:

      self.logger.error(e)




  def file_push(self, path, field, message):

    try:

      # 判断是否存在，如果存在删除内容
      self.handle.exists(field)

      with open(path, 'r') as file:

        for line in file:

          self.handle.lpush(field, line)

      self.logger.info(message)

    except Exception as e:

      self.logger.error(e)


  # def update(self):

  # def select(self):

  # def remove(self):

  # def close(self):
