#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2023/1/10
# @file setting.py
import os
import json
from logging import DEBUG
from utils.log import get_logger


class Setting:
    _default_setting = {
        "scan_dirs"    : [
            "01_工具",
            "01_环境"
        ],
        'from_drive'   : True,  # 从驱动器根路径开始扫描
        'scan_root'    : os.getcwd(),
        # 'scan_root'    : r"A:\01_软件环境",
        'auto_save'    : True,  # 设置信息自动保存控制
        "logging_level": 20,  # 日志记录等级 10: debug, 20: info
        'data_file'    : 'data.json',
    }

    def __init__(self, setting_path='./setting.json'):
        """
        设置信息类
        :param setting_path: 设置文件所在路径
        """
        # 获取日志记录器
        self.logger = get_logger('Setting', logger_level=DEBUG)
        # 默认先记录一下设置文件所在位置
        self.logger.debug(f"{setting_path=}")
        self.setting_path = setting_path
        self.data = self.load_setting()

        if not self.data:
            # 没有从设置文件中获得到信息
            self.data = self._default_setting  # 将设置信息设为默认值
            self.logger.debug(f"no setting data, set to default: {self.data=!s}")
            self.save_setting()  # 保存设置信息到文件
        elif len(self.data) < len(self._default_setting):
            # setting.json中的设置信息不全, 使用默认参数更新
            self.logger.info(f"update setting from default")
            self.logger.debug(f"got setting from file: {self.data}")
            for key, value in self._default_setting.items():
                if key not in self.data:
                    self.logger.info(f"update setting with: {key} {value}")
                    self.data[key] = value
            self.save_setting()

        # 获取完设置信息, 将日志记录器的日志等级 更改为设置信息内的等级
        self.logger.setLevel(self.get_log_level())
        # 初始化数据
        if self.data['from_drive']:
            # 如果设置为从磁盘根路径开始扫描, 则将scan_root设置为盘符
            self.data['scan_root'] = os.path.splitdrive(self.data['scan_root'])[0] + '\\'
        self._autosave = self.data.get('auto_save')
        self.logger.debug(f"scan disk from: {self.data['scan_root']}")
        self.logger.info(f"{self._autosave=}")

    def load_setting(self):
        """
        从setting.json中加载设置信息
        :return: setting: dict
        """
        if not os.path.isfile(self.setting_path):
            self.logger.info(f"file not exists: {self.setting_path}")
            return
        try:
            with open(self.setting_path, 'r', encoding='utf-8') as f:
                __setting = json.load(f)
                self.logger.debug(f"got setting from {os.path.abspath(self.setting_path)!s}: {__setting}")
                return __setting
        except json.decoder.JSONDecodeError as e:
            # setting.json 文件内容错误
            self.logger.error(f"catch err in reading setting.json -> {e}")
            self.logger.info(f'can not get setting from {os.path.abspath(self.setting_path)!s}, set setting to default')
            return

    def save_setting(self):
        """
        将设置信息保存到setting.json文件中
        """
        self.logger.info(f"setting_file path: {os.path.abspath(self.setting_path)}")
        with open(self.setting_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    def __getitem__(self, key):
        return self.data.get(key)

    def __setitem__(self, name, value):
        """Set the value of a setting."""
        self.data[name] = value

        if self.data.get('auto_save'):
            self.save_setting()

    def __delitem__(self, name):
        """Remove a setting."""
        self.data.pop(name)

        if self._autosave:
            self.save_setting()

    def get(self, key):
        return self.__getitem__(key)

    def set_(self, key, value):
        self.__setitem__(key, value)

    def __str__(self):
        return f"{self.data}"

    def get_log_level(self):
        log_level = DEBUG
        setting_level = self.get('logging_level')
        if setting_level:
            log_level = setting_level
        return log_level


# 获取设置信息对象
setting__ = Setting()
setting__.logger.info(f'use global setting: {setting__}, at{id(setting__)}')
