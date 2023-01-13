#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2023/1/11
# @file window.py
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QMenu
)
from gui.ui_mainWindow import Ui_MainWindow
from PyQt5.QtCore import Qt as CoreQt
import sys
from utils.log import get_logger


class MainWindow(QMainWindow):
    def __init__(self):
        # 必须在父类初始化之前调用, 否则返回代码 -1073740791 (0xC0000409)
        self.app = QApplication(sys.argv)
        super().__init__()
        # 导入UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 获取scanner
        from utils.scanner_ import scanner__
        self._scanner = scanner__
        # 获取setting
        from utils.setting import setting__
        self._setting = setting__
        # 初始化日志记录器
        self.logger = get_logger("gui", self._setting.get_log_level())
        # 记录日志
        self.logger.info(f"finish init MainWindow.")
        self.logger.debug(f"{self._setting}")
        self.logger.debug(f"{self._scanner}")


def connect_to_slot(ui):
    """
    将事件连接到槽
    :param ui:
    :return:
    """
    from slots import (search_click, right_click_menu)

    # 将点击信号绑定到按钮
    # self.ui.pushButton.clicked.connect(self.handle_click)
    # # 设置允许弹出菜单  单击右键响应事件
    # self.ui.tableWidget.setContextMenuPolicy(CoreQt.CustomContextMenu)
    # # 将信号请求连接到一个槽
    # self.ui.tableWidget.customContextMenuRequested.connect(rightClickMenu)

    # 点击搜索按钮

    # 搜索类型切换

    # 右键单击

    # 打开选定文件

    # 打开选定文件夹

    # 编辑设置

    # 获取当前字体大小

    # 更改字体大小


def gui_start():
    ui = MainWindow()
    # 连接信号与槽
    connect_to_slot(ui)

    # 显示界面
    ui.show()
    sys.exit(ui.app.exec_())
