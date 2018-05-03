#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：driver.py
# 作者：zhangxiaofei
# 日期：2018-04-24
# 功能：数据抓取类
# -------------------------------------------------------------------------

import ie
import chrome
import firefox

class Driver:




  def get_driver(self):

    if 'firefox' == self.category :
      1111
    elif 'chrome' == self.category :
      222
    else:
      3333

  """
  类初始化
  """
  def __init__(self, category = 'firefox'):

    self.category = category


# if __name__ == '__main__':

#   driver = Driver()
