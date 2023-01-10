#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2023/1/10
# @file scanner_.py
import os
import re
import json
from collections import defaultdict
from .setting import Setting
from .log import get_logger
from .timer import timer


class Scanner:
    def __init__(self, data_file='data.json'):
        self.data_file = data_file
        # 获取设置信息对象
        setting = Setting()
        # 获取日志记录器
        self.logger = get_logger("Scanner", logger_level=setting.get_log_level())
        self.logger.debug(f"{setting=!s}")
        # 初始化目录数据
        self.data_ = defaultdict(dict)
        # 获取扫描的根路径
        self.scan_root = setting.get('scan_root')
        self.scan_dirs = setting.get('scan_dirs')
        self.logger.debug(f"{self.scan_dirs=}")
        self.logger.debug(f"{self.scan_root=}")
        self.load_()

    def scan_(self):
        for dir_ in self.scan_dirs:
            for root, dirs, files in os.walk(rf"{self.scan_root}\{dir_}"):
                self.data_[root]['dirs'] = dirs
                self.data_[root]['files'] = files
        self.dump_()

    def load_(self):
        if os.path.exists(self.data_file):
            self.scan_()
            self.logger.error(f"file: {self.data_file} not found")
            self.logger.info(f"data_file not exists, auto scan, got: {len(self.data_)} items")
            return
        with open(self.data_file, 'r', encoding='utf-8') as f:
            self.data_ = json.load(f)
        self.logger.info(f"load data from: {self.data_file}, got: {len(self.data_)} items")

    def dump_(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            # 将json写入文件, 设置缩进, 不将中文转换为ascii字符
            json.dump(dirs_data, f, indent=4, ensure_ascii=False)
            self.logger.info(f"dump data to: {self.data_file}, carry")

    @timer
    def search_file(self, name):
        res_data = []
        self.logger.debug(f"searching files like: {name}")
        for dir_path, data in self.data_.items():
            for file_name in data.get('files'):
                if re.match(f".*{name}.*", file_name, re.IGNORECASE):
                    res_data.append({
                        'abs' : os.path.join(dir_path, file_name),
                        'dir' : dir_path,
                        'name': file_name,
                    })
                    self.logger.info(f"got: {dir_path=!s}, {file_name=}")
        self.logger.debug(f"{res_data=!s}")
        return res_data

    def search_dir(self, data, name):
        ...
