#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：file.py
# 作者：zhangxiaofei
# 日期：2018-04-20
# 功能：用于文件操作
# -------------------------------------------------------------------------

class File:


  # -----------------------------------------------------------------------
  # 初始化方法

  def __init__(self, logger):

    self.logger = logger




  # -----------------------------------------------------------------------
  # 写方法

  def write(self, path, operation, content, encoding='utf-8'):

    try:

      with open(path, operation, 1, encoding) as file:

        f.writelines(content)
        f.write('\n')

    except Exception as e:

      self.logger.error(e)




  # -----------------------------------------------------------------------
  # 读方法

  def read(self, path, operation, encoding='utf-8'):

    try:

      lists = []

      with open(path, operation, 1, 'utf-8') as file:

        for line in file:

          lists.append(line)

      return lists

    except Exception as e:

      self.logger.error(e)




  # -----------------------------------------------------------------------
  # 清除方法

  def clear(self, path, operation, encoding='utf-8'):

    try:

      with open(path, operation, 1, encoding) as file:

        return file.truncate()

    except Exception as e:

      self.logger.error(e)

