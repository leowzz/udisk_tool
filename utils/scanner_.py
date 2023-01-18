#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2023/1/10
# @file scanner_.py
import os
import re
import json
from collections import defaultdict
from utils.log import get_logger
from utils.setting import setting__
from utils.timer import timer, timer_ns


class Scanner:
    def __init__(self):
        # 获取日志记录器
        self.logger = get_logger("Scanner", logger_level=setting__.get_log_level())
        self.logger.debug(f"got setting: {setting__!s}")
        # 初始化目录数据
        self.data_ = defaultdict(dict)
        # 获取扫描的根路径
        self.scan_root = setting__.get('scan_root')
        self.scan_dirs = setting__.get('scan_dirs')
        self.logger.debug(f"{self.scan_dirs=}")
        self.logger.debug(f"{self.scan_root=}")
        # 从设置信息中获取数据文件存储位置
        self.data_file = setting__.get('data_file')

        # 读取数据文件
        self.load_()

    @timer_ns
    def scan_(self):
        # 扫描磁盘
        for dir_ in self.scan_dirs:
            for root, dirs, files in os.walk(rf"{self.scan_root}\{dir_}"):
                self.data_[root]['dirs'] = dirs
                self.data_[root]['files'] = files
        self.logger.debug(f"scan data from disk, got: {len(self.data_)}")
        # 将扫描到的数据保存到文件
        self.dump_()

    def load_(self):
        self.logger.debug(f"got data_file path from setting: {os.path.abspath(self.data_file)}")
        if not os.path.exists(self.data_file):
            # 数据文件不存在, 重新扫描磁盘, 生成数据文件
            self.scan_()
            self.logger.warning(f"file: {os.path.abspath(self.data_file)} not found. auto scan")
            self.logger.info(f"data_file not exists, auto scan, got: {len(self.data_)} items")
            return
        with open(self.data_file, 'r', encoding='utf-8') as f:
            self.data_ = json.load(f)
        self.logger.info(f"load data from: {os.path.abspath(self.data_file)}, got: {len(self.data_)} items")

    def dump_(self):
        # 将数据保存到文件
        with open(self.data_file, 'w', encoding='utf-8') as f:
            # 将json写入文件, 设置缩进, 不将中文转换为ascii字符
            json.dump(self.data_, f, indent=4, ensure_ascii=False)
            self.logger.info(f"dump data to: {os.path.abspath(self.data_file)}, carry: {len(self.data_)}")

    @timer_ns
    def _search(self, name, Pattern, dict_attr='files', ignore_case=True):
        # 搜索文件夹名称
        res_data = []  # 待返回的数据
        match_flags = 0  # 正则匹配方式, 初始化为默认值
        if Pattern:  # 不为空则使用传递的参数
            _Pattern = Pattern
        else:  # 使用默认值
            _Pattern = f".*{name}.*"
        if ignore_case:
            # 不匹配大小写
            match_flags = re.IGNORECASE

        self.logger.debug(f"searching {dict_attr} like: {name}")
        for dir_path, data in self.data_.items():
            for file_name in data.get(dict_attr):
                if re.match(_Pattern, file_name, match_flags):
                    res_data.append({
                        'abs' : os.path.join(dir_path, file_name),
                        'dir' : dir_path,
                        'name': file_name,
                    })
                    self.logger.info(f"got: {dir_path=!s}, {file_name=}")
        self.logger.debug(f"{res_data=!s}")
        return res_data

    def search_file(self, name):
        # 搜索文件, 模糊匹配
        return self._search(name=name, Pattern=f".*{name}.*", dict_attr='files')

    def search_dir(self, name):
        # 搜索文件夹, 模糊匹配
        return self._search(name=name, Pattern=f".*{name}.*", dict_attr='dirs')

    def search_ext(self, ext):
        # 搜索指定后缀名的文件
        return self._search(name=f"*.{ext}", Pattern=f".*{ext}$", dict_attr='files')

    def search_with_type(self, name: str, type_=0):
        type2reg = {
            0: [f".*{name}.*", 'files'],  # 类型索引: 正则字符串, 待搜索的数据类型
            1: [f".*{name}.*", 'dirs'],
            2: [f".*{ext}$", 'files'],
        }
        return self._search(name, *type2reg.get(type_))


scanner__ = Scanner()
scanner__.logger.info(f"use scanner at: {id(scanner__)}")
