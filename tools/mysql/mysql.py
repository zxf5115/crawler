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

import pymysql

class Mysql(object):

  """
  连接数据库
  """
  def connect(host, username, password, dbname):
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='python', charset='utf8')

    return db

# (host='127.0.0.1', port=3306, user='root', passwd='', db='tkq1', charset='utf8')
  """
  插入数据表操作
  """
  def insert(self, table, field, value):

    # 使用cursor()方法获取操作游标
    cursor = self.cursor()

    # SQL 插入语句
    sql = "INSERT INTO %s (`%s`) VALUES ('%s')" % (table, field, value)

    try:
      # 执行sql语句
      cursor.execute(sql)
      # 提交到数据库执行
      self.commit()
    except Exception as e:
      print(e)
      # 如果发生错误则回滚
      self.rollback()

    # 关闭游标
    cursor.close()


  """
  删除数据
  """
  def delete(self, table, where):

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 删除语句
    sql = "DELETE FROM %s %s" % (table, where)

    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 提交修改
       db.commit()
    except:
       # 发生错误时回滚
       db.rollback()

    # 关闭连接
    db.close()



  """
  更新数据
  """
  def update(self, table, field, value, where = ""):

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句
    sql = "UPDATE %s SET %s = %s WHERE %s " % (table, field, value, where)

    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 提交到数据库执行
       db.commit()
    except:
       # 发生错误时回滚
       db.rollback()

    # 关闭数据库连接
    db.close()

  """
  查询数据
    fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    fetchall(): 接收全部的返回结果行.
    rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。

  """
  def select(self, table, field = '*', where = "", group = "", order = ""):

    # 使用cursor()方法获取操作游标
    cursor = self.cursor()

    # SQL 查询语句
    sql = "SELECT %s FROM %s %s %s %s " % (field, table, where, group, order)

    try:
      # 执行SQL语句
      cursor.execute(sql)

      # 返回查询结果
      return cursor.fetchall()
    except:
      print ("Error: unable to fetch data")

    # 关闭游标
    cursor.close()

    # 关闭数据库连接
    self.close()

  # 事务
  def transaction(self):
    # SQL删除记录语句
    sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 向数据库提交
       db.commit()
    except:
       # 发生错误时回滚
       db.rollback()


  def close2(self):
    # 关闭数据库连接
    self.close()

  # def __init__(self):


# if __name__ == '__main__':


