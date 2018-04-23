#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：ip.py
# 作者：zhangxiaofei
# 日期：2018-04-20
# 功能：用于初始化数据
# -------------------------------------------------------------------------

import datetime

class Datetime(object):

  # -----------------------------------------------------------------------
  # 得到当前时间

  @classmethod
  def get_now_time(cls):

    return datetime.datetime.now()




  # -----------------------------------------------------------------------
  # 计算时间差,格式: 时分秒

  @classmethod
  def get_time_diff(cls, start, end):

    seconds = (end - start).seconds

    m, s = divmod(seconds, 60)

    h, m = divmod(m, 60)

    diff = ("%02d:%02d:%02d" % (h, m, s))

    return diff


