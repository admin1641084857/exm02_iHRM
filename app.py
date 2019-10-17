"""
    架构介绍:
        核心: api + case + data
         |-- api:请求业务(requests)
         |-- case:测试用例(unittest)
         |-- data:参数化(json文件封装数据)
         调用关系: 调用者 case 被调用者 api + data

        报告: report + tools + run_suite.py
         |-- report: 保存测试报告
         |-- tools: 存储工具
         |-- run_suite.py: 组织测试套件，调用工具生成测试报告

        配置: app.py
         配置程序的常量、全局变量、方法.....

        需求: 为程序运行添加日志
        流程:
            配置
                1.导包
                2.获取日志器对象
                3.设置日志处理器(控制输出目标)
                4.设置格式化器
                5.组织上述对象
            调用
                先执行初始化配置
                logging.INFO("------")
"""

import os

import logging
import logging.handlers

# 封装 URL 的前缀
import time

BASE_URL = "http://182.92.81.159/api/sys/"
# 动态获取绝对路径
PRO_PATH = os.path.dirname(os.path.abspath(__file__))


def my_log_config():
    # 2.
    # 获取日志器对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 3.
    # 设置日志处理器(控制输出目标)
    to1 = logging.StreamHandler()  # 默认控制台
    filename = PRO_PATH + "/log/myAuto" + time.strftime("%Y%m%d%H%M%S") + ".log"
    to2 = logging.handlers.TimedRotatingFileHandler(filename=filename, when="h", interval=10, backupCount=20,
                                                    encoding="utf-8")
    # 4.
    # 设置格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 5.
    # 组织上述对象
    to1.setFormatter(formatter)
    to2.setFormatter(formatter)
    logger.addHandler(to1)
    logger.addHandler(to2)


TOKEN = None
