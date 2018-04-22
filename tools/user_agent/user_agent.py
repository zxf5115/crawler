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
  # 根据配置文件将 User Agent 保存到redis

  set_user_agent(self):

    self.redis.file_push(self.path, self.field, self.message)




  # -----------------------------------------------------------------------
  # 随机获取 User Agent

  get_user_agent(self)

    try:

      user_agent = self.redis.srandmember(self.field, 1)

      data = user_agent[0].decode()

    except Exception as e:

      Logger.error(e)

    return data



  # -----------------------------------------------------------------------
  # 初始化方法

  def __init__(self, conf, redis, logger):

    self.redis = redis
    self.logger = logger

    self.path, self.field, self.message = conf.get_user_agent_conf_info()
