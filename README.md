# crawler
网络爬虫


本人一直从事PHP开发，这是第一个Python代码，可能写的不是很好，仅供参考


# 代理IP地址获取

使用的是 GetFreeIP

地址：https://github.com/TurboWay/GetFreeIP

本代码中集成了 GetFreeIP，把代理IP直接保存到了 redis 中

user agent 也保存到了 redis 中

根据代理ip 和 user agent 使用多线程 进行 企业黄页抓取

抓取公司黄页数据
(https://github.com/zxf5115/crawler/master/document/2.png)

剩下的待写！！！