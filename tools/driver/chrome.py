#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：driver.py
# 作者：zhangxiaofei
# 日期：2018-04-24
# 功能：数据抓取类
# -------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Driver(object):


  def set_firefox_driver(self):

    try:

      profile = webdriver.FirefoxProfile()

      # 禁止不安全提示
      profile.set_preference("security.insecure_field_warning.contextual.enabled", False)

      # 禁止下载和加载图片
      profile.set_preference('permissions.default.image', 2)
      # 禁用图片 某些需要加上这个
      profile.set_preference('browser.migration.version', 9001)

      # 禁止自动更新
      profile.set_preference("app.update.enabled", False)

      # 禁用样式表文件
      profile.set_preference('permissions.default.stylesheet', 2)

      # 禁用flash
      profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)

      # 禁止 Javascript 的执行
      profile.set_preference('javascript.enabled', False)

      # 强制刷新缓存
      profile.set_preference("browser.cache.check_doc_frequency", 1)
      profile.set_preference("browser.cache.disk.enable", False)
      profile.set_preference("browser.cache.memory.enable", False)
      profile.set_preference("browser.cache.offline.enable", False)
      profile.set_preference("network.http.use-cache", False)
      profile.set_preference("browser.cache.disk_cache_ssl", False)

      self._set_proxy_plugin(profile)

      # 获得初始化生成的IP随机地址 样式：'119.28.152.208:80'
      ip_address = self.proxy.get_ip_address()
      print(ip_address)
      if ip_address:
        profile = self._set_proxy(profile, ip_address)

      # 获得初始化生成的 User Agent 信息 样式：'Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'
      user_agent = self.proxy.get_user_agent()

      if user_agent:
        profile = self._set_user_agent(profile, user_agent)

      # profile.update_preferences()

      driver = webdriver.Firefox(profile, executable_path='lib/geckodriver.exe')

      # 设置 Cookie 信息
      self._set_cookie(driver)

    except Exception as e:

      self.logger.error(e)

    return driver


  def get_driver(self):




  def _set_proxy_plugin(self, profile):

    try:

      # add new header
      profile.add_extension("lib/modify_headers-0.7.1.1-fx.xpi")
      profile.set_preference("extensions.modify_headers.currentVersion", "0.7.1.1-fx")
      profile.set_preference("modifyheaders.config.active", True)
      profile.set_preference("modifyheaders.config.alwaysOn", True)

      profile.set_preference("modifyheaders.headers.count", 1)
      profile.set_preference("modifyheaders.headers.action0", "Add")
      profile.set_preference("modifyheaders.headers.name0", "Proxy-Switch-Ip")
      profile.set_preference("modifyheaders.headers.value0", "yes")
      profile.set_preference("modifyheaders.headers.enabled0", True)

      Logger.info('启用代理 IP 插件')

    except Exception as e:

      Logger.error(e)

    return profile




  """
  设置IP代理
  """
  def _set_proxy(self, profile, proxy_host):

    try:

      proxy_list = proxy_host.split(':')

      agent_ip = proxy_list[0]
      agent_port = proxy_list[1]

      # 使用手动代理
      profile.set_preference('network.proxy.type', 1)

      # 所有协议公用一种代理配置
      profile.set_preference('network.proxy.share_proxy_settings', True)
      profile.set_preference('network.proxy.http', agent_ip)
      profile.set_preference('network.proxy.http_port', int(agent_port))

      # 如果是 HTTPS 需要配置
      profile.set_preference('network.proxy.ssl', agent_ip)
      profile.set_preference('network.proxy.ssl_port', int(agent_port))

      # profile.set_preference("network.proxy.user_name", 'aaaaa')
      # profile.set_preference("network.proxy.password", 'bbbbb')
      # 对于localhost的不用代理，这里必须要配置，否则无法和 webdriver 通讯
      profile.set_preference('network.proxy.no_proxies_on', 'localhost,127.0.0.1')
      profile.set_preference('network.http.use-cache', False)


      # # Proxy auto login
      # profile.add_extension('closeproxy.xpi')
      # credentials = '{user}:{pass}'.format(**proxy)
      # credentials = b64encode(credentials.encode('ascii')).decode('utf-8')
      # profile.set_preference('extensions.closeproxyauth.authtoken', credentials)

      Logger.info('代理 IP 设置完成')

    except Exception as e:

      Logger.error(e)

    return profile



  """
  设置 User Agent 信息
  """
  def _set_user_agent(self, profile, user_agent):

    try:

      profile.set_preference("general.useragent.override", user_agent)

      Logger.info('User Agent 设置完成')

    except Exception as e:

      Logger.error(e)

    return profile


  """
  获取网站 Cookie 信息
  """
  def _get_cookie(self, driver):

    try:

      cookie = driver.get_cookies()

      if cookie:

        for vo in cookie:
          Logger.info("%s -> %s" % (cookie['name'], cookie['value']))

    except Exception as e:

      Logger.error(e)

    return cookie



  """
  设置网站 Cookie 信息
  """
  def _set_cookie(self, driver):

    try:

      # info = self._get_cookie(driver)

      # out1={ u'domain':u'www.factual.com',u'expiry':2147385600, u'httpOnly':True ,
      # u'secure': False ,u'name':u'_www_session',u'value':u'ekRNZHU2YkxUK3JiNTlJcEhWWGs5'}
      # 删除一个特定的cookie
      # driver.delete_cookie("CookieName")

      # 删除所有cookie
      driver.delete_all_cookies()

      # if info:
        # 添加cookie信息
        # driver.add_cookie(info)

      Logger.info('Cookie 设置完成')

    except Exception as e:

      Logger.error(e)





  """
  类初始化
  """
  def _start_load_plugin():

    if firebug == 1:
      profile.add_extension(capture_path + '/firebug-2.0.8.xpi')
      profile.set_preference("extensions.firebug.currentVersion", "2.0.8")
      profile.set_preference("extensions.firebug.allPagesActivation", "on")
      profile.set_preference("extensions.firebug.defaultPanelName", "net")
      profile.set_preference("extensions.firebug.net.enableSites", True)
      profile.set_preference("extensions.firebug.delayLoad", False)
      profile.set_preference("extensions.firebug.onByDefault", True)
      profile.set_preference("extensions.firebug.showFirstRunPage", False)
      profile.set_preference("extensions.firebug.net.defaultPersist", True)
    if netexport == 1:
      profile.add_extension(capture_path + '/netExport-0.9b7.xpi')
      profile.set_preference("extensions.firebug.DBG_NETEXPORT", True)
      profile.set_preference("extensions.firebug.netexport.alwaysEnableAutoExport", True)
      profile.set_preference("extensions.firebug.netexport.defaultLogDir", capture_path + "/har/"+url)
      profile.set_preference("extensions.firebug.netexport.includeResponseBodies", True)




  """
  类初始化
  """
  def __init__(self, category = 'firefox'):

    self.category = category


# if __name__ == '__main__':

#   driver = Driver()
