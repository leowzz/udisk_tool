#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2023/1/10
# @file log.py

import os
import logging
import datetime
from logging import DEBUG

today = datetime.datetime.today()


def get_logger(name="logger", logger_level=logging.INFO, log_dir=r'./log', encoding='utf-8', ):
    """
    获取日志记录器
    :param name: logger实例名称
    :param log_dir: 日志文件夹
    :param encoding: 日志文件编码
    :param logger_level: 日志记录等级
    :raises FileExistsError
    :return: logging.RootLogger
    """
    # 日志文件夹处理
    if log_dir != '.':
        if os.path.isfile(log_dir):
            raise FileExistsError(f"file already exists: {os.path.abspath(log_dir)} ")
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

    # 调试日志设置
    # 设置log实例名称
    logger = logging.getLogger(name)
    # 设置日志级别为ERROR，即只有日志级别大于等于ERROR的日志才会输出
    # logger.setLevel(logging.ERROR)
    logger.setLevel(logger_level)
    # 创建一个格式化器
    formatter = logging.Formatter(
        fmt=f"%(asctime)s %(name)-{len(name)}s %(levelname)-5s [line:%(lineno)d] %(funcName)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    # 创建流处理器
    console = logging.StreamHandler()
    # 为处理器设置格式化器
    console.setFormatter(formatter)
    # 创建文件处理器
    from logging.handlers import RotatingFileHandler
    # 定义日志文件名
    # filename = f"{today:%Y%m%d_%H%M%S}.log"
    filename = f"{today:%Y%m%d}.log"
    file_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, filename),
        mode='a',
        maxBytes=1 * 1024 * 1024,  # 单文件最大字节数: 1MB
        backupCount=3,  # 备份日志数
        encoding=encoding,
    )
    # file_handler = logging.FileHandler(
    #     filename=log_path,
    #     mode='a',
    #     encoding=encoding
    # )
    file_handler.setFormatter(formatter)
    # 为实例添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(console)
    return logger
