#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：redis.py
# 作者：zhangxiaofei
# 日期：2018-04-20
# 功能：用于操作reids
# -------------------------------------------------------------------------

import redis

class Redis(object):


  # -----------------------------------------------------------------------
  # 初始化方法

  def __init__(self, conf, logger):

    try:

      # 得到Redis配置信息
      host, port = conf.get_redis_conf_info()

      # 打开连接
      self.handle = redis.Redis(host = host, port = port)
      self.logger = logger

    except Exception as e:

      self.logger.error(e)




  # -----------------------------------------------------------------------
  # 判断 字段是否存在，如果存在清空内容

  def exists(self, field):

    if self.handle.exists(field):

        self.handle.delete(field)




  # -----------------------------------------------------------------------
  # 判断 list 长度

  def scard(self, field):

    return self.handle.scard(field)




  # -----------------------------------------------------------------------
  # 往 list 中 添加数据

  def lpush(self, field, value):

    try:

      # 打开连接
      self.handle.lpush(field, value)

    except Exception as e:

      self.logger.error(e)


  # -----------------------------------------------------------------------
  # 给 set 中 添加数据

  def sadd(self, field, value):

    try:

      # 打开连接
      self.handle.sadd(field, value)

    except Exception as e:

      self.logger.error(e)

  # -----------------------------------------------------------------------
  # 从 set 中 随机取出数据

  def srandmember(self, field, number = 1):

    try:

      return self.handle.srandmember(field, number)

    except Exception as e:

      self.logger.error(e)



  # -----------------------------------------------------------------------
  # 从配置文件中读取信息保存到redis中

  def file_push(self, path, field, message):

    try:

      # 判断是否存在，如果存在删除内容
      self.handle.exists(field)

      with open(path, 'r') as file:

        for line in file:

          self.handle.sadd(field, line)

      self.logger.info(message)

    except Exception as e:

      self.logger.error(e)
