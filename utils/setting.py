#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2023/1/10
# @file setting.py
import os
import json
from .log import get_logger, DEBUG


class Setting:
    _default_setting = {
        "scan_dirs"    : [
            "01_工具",
            "02_环境",
            "03_Tool"
        ],
        'from_drive'   : False,
        # 'scan_root' : os.getcwd(),
        'scan_root'    : r"A:\01_软件环境",
        'auto_save'    : True,
        "logging_level": 10,
    }

    def __init__(self, setting_path='setting.json'):
        """
        设置信息类,
        :param setting_path: 设置文件所在路径
        """
        self.logger = get_logger('Setting', logger_level=DEBUG)
        self.logger.debug(f"{setting_path=}")
        self.setting_path = setting_path
        self.data = self.load_setting()
        self.logger.debug(f"got setting from file: {self.data=!s}")

        if not self.data:
            self.data = self.default_setting
            self.logger.debug(f"no setting data, set to default: {self.data=!s}")

        # setting.json中的设置信息不全, 使用默认参数更新
        # elif len(self.data) < len(self.default_setting):
        #     for key, value in self.default_setting.items():
        #         if key not in self.data:
        #             self.data[key] = value

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
        with open(self.setting_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_setting(self):
        """
        将设置信息保存到setting.json文件中
        """
        print(os.path.abspath(self.setting_path))
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
