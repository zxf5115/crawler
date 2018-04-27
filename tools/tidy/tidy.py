#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：tidy.py
# 作者：zhangxiaofei
# 日期：2018-04-25
# 功能：用于去掉公司与公司简称
# -------------------------------------------------------------------------

import jieba

class Tidy(object):


  # -----------------------------------------------------------------------
  # 将公司名称分为三部分，该函数返回值包含第三部分的所有关键词

  def exclude_words():

    exclusion = [u'公司',u'有限公司', u'责任公司', u'有限责任公司']

    return exclusion



  # -----------------------------------------------------------------------
  # 取出公司中间部分关键词

  def clean_list(self):

    # 公司开头地域部分列表，需要完善
    region = [u'北京',u'北京市', u'东城', u'西城', u'海淀', u'朝阳', u'丰台', \
              u'门头沟', u'石景山', u'房山', u'通州', u'顺义', u'昌平', u'大兴', \
              u'怀柔', u'平谷', u'延庆', u'密云']

    exclu_words = exclude_words()

    coname_lsts = get_name_list()

    key_name_temp = []  # 未去重列表

    for coname in coname_lsts:

      seg_coname = list(jieba.cut(coname, cut_all=False))

      exclu = [seg for seg in seg_coname if (seg not in exclu_words and seg not in region)]

      #print ''.join(exclu)

      #key_name.append(exclu)

      key_name_temp.append(''.join(exclu))

    #temp_list = list(set(key_name_temp))   # 对列表去重， 然后再次分词
    # key_name = list(jieba.cut(temp_list, cut_all=False))  # 再次分词
    return key_name_temp # 返回嵌套表，公司名称关键词


  # -----------------------------------------------------------------------
  # 对clean_list 的返回列表进行去重后并再次分词

  def duplication():

    dup_key = []

    raw_key = list(set(clean_list()))   # 去重

    for temp in raw_key:

        temp1 = list(jieba.cut(temp, cut_all=False))

        new_temp = [i for i in temp1 if i != [' ', ')']]  # 删除分词后的空格

        dup_key.append(new_temp)

       # print '/'.join(temp1)


    # new_dup_key = [i for i in dup_key if i != ' ']  # delete space ' '

    return dup_key



  # -----------------------------------------------------------------------
  # 将每个公司名称进行拆分

  def seg_company_name(self, data_list):

    co_name = []

    for data in data_list:

      seg_coname = list(jieba.cut(data, cut_all=False))

      co_name.append(seg_coname)

    return co_name



  # -----------------------------------------------------------------------
  # 初始化方法

  def __init__(self, conf, redis, logger):

    jieba.load_userdict('config/dic.ini')





