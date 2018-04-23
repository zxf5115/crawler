#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：user_agent.py
# 作者：zhangxiaofei
# 日期：2018-04-21
# 功能：用于创建和读取 User Agent
# -------------------------------------------------------------------------

class UserAgent(object):


  # -----------------------------------------------------------------------
  # 初始化可用 User Agent 代理地址

  def init_user_agent(self):

    self.redis.file_push(self.path, self.field, self.message)




  # -----------------------------------------------------------------------
  # 随机获取 User Agent

  def get_user_agent(self):

    try:

      user_agent = self.redis.srandmember(self.field, 1)

      data = user_agent[0].decode()

    except Exception as e:

      self.logger.error(e)

    return data



  # -----------------------------------------------------------------------
  # 初始化方法

  def __init__(self, conf, redis, logger):

    self.redis = redis
    self.logger = logger

    self.path, self.field, self.message = conf.get_user_agent_conf_info()
