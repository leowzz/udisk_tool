#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2023/1/11
# @file window.py
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QMenu,
)
from PyQt5.Qt import QTableWidgetItem, QAbstractItemView
from gui.ui_mainWindow import Ui_MainWindow
from PyQt5.QtCore import Qt as CoreQt
import sys
from utils.log import get_logger
from utils.util import exec_

fileNameColIndex = 0
dirNameColIndex = 1


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
        # 初始化搜索到的数据为空
        self.table_data = []
        # 初始化搜索类型为按文件名搜索
        self.search_func = self._scanner.search_file
        # 生成测试数据
        self.test()
        self.draw_table()
        # 连接信号与槽
        self.connect_to_slot()

    def test(self):
        self.table_data = [{
            'abs': 'A:\\01_软件环境\\01_工具\\格式转换\\Y右键文件转换FileConverter-1.2.3-x64-setup.msi',
            'dir': 'A:\\01_软件环境\\01_工具\\格式转换', 'name': 'Y右键文件转换FileConverter-1.2.3-x64-setup.msi'
        }, {
            'abs' : 'A:\\01_软件环境\\01_工具\\键鼠工具\\02_右键工具.exe', 'dir': 'A:\\01_软件环境\\01_工具\\键鼠工具',
            'name': '02_右键工具.exe'
        }, {
            'abs': 'A:\\01_软件环境\\01_工具\\键鼠工具\\Y右键菜单神器Easy Context Menu1.6绿色汉化版.rar',
            'dir': 'A:\\01_软件环境\\01_工具\\键鼠工具', 'name': 'Y右键菜单神器Easy Context Menu1.6绿色汉化版.rar'
        }, {
            'abs': 'A:\\01_软件环境\\01_工具\\键鼠工具\\右键菜单编辑器.exe',
            'dir': 'A:\\01_软件环境\\01_工具\\键鼠工具', 'name': '右键菜单编辑器.exe'
        }]
        # # 设置行数
        # self.ui.tableWidget.setRowCount(3)
        # # 设置表格内容不可编辑
        # self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.ui.tableWidget.setItem(0, 0, QTableWidgetItem('右键菜单编辑器.exe', ))
        # self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("J:01_工具\\键鼠工具\\"))
        # self.ui.tableWidget.setItem(1, 0, QTableWidgetItem('右键菜单编辑器右键菜单编辑器.exe', ))

    def search_click(self):
        # 点击搜索按钮
        search_str = self.ui.lineEdit.text()
        self.logger.debug(f"search str: {search_str}, search func: {self.search_func}")
        self.table_data = self.search_func(search_str)
        self.draw_table()

    def draw_table(self):
        """
        渲染表格
        """

        # 设置行数
        self.logger.debug(f"Table rows: {len(self.table_data)}")
        self.ui.tableWidget.setRowCount(len(self.table_data))
        # 设置表格内容不可编辑
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 逐行渲染表格
        for index, item in enumerate(self.table_data):
            self.ui.tableWidget.setItem(
                index,  # 行索引
                0,  # 列索引
                QTableWidgetItem(item.get("name")),  # 表格内容: 文件名
            )
            self.ui.tableWidget.setItem(
                index,  # 行索引
                1,  # 列索引
                QTableWidgetItem(item.get("dir")),  # 表格内容: 文件所在路径
            )
        self.logger.info(f"Complete the table to render")

    # 搜索类型切换
    def search_type_change(self):
        id2fun = {
            0: self._scanner.search_file,
            1: self._scanner.search_dir,
            2: self._scanner.search_ext,
        }
        self.logger.debug(self.ui.comboBox.currentIndex())
        index = self.ui.comboBox.currentIndex()
        self.logger.debug(f"{index=}")
        self.search_func = id2fun.get(index)
        self.logger.debug(f"{self.search_func=}")

    # 打开选定文件
    def open_(self):
        ...

    # 打开选定文件夹

    # 编辑设置

    # 获取当前字体大小

    # 更改字体大小

    def right_click_table_item(self, pos):
        """
        右键菜单有关方法
        :param pos: PyQt5.QtCore.QPoint pyqt坐标对象
        :return:
        """
        # pos 为单击鼠标右键的坐标  相对于窗口
        self.logger.debug(f"{pos=}")
        # 鼠标右键单击前两行弹出菜单，单击第三行没响应
        # 获取当前选中的 行,列 索引
        rowNum = self.ui.tableWidget.selectionModel().selection().indexes()[0].row()
        colNum = self.ui.tableWidget.selectionModel().selection().indexes()[0].column()
        self.logger.info(f"click table item at [row: {rowNum}, col: {colNum}]")
        if colNum == fileNameColIndex:
            menu = QMenu()  # 创建菜单
            item1 = menu.addAction("打开")
            item2 = menu.addAction("打开所在文件夹")
            # 相对于窗口的坐标系转换为相对于屏幕的坐标系  映射到全局
            screePos = self.ui.tableWidget.mapToGlobal(pos)
            action = menu.exec(screePos)  # 获取全局坐标系下该位置的动作
            if action == item1:  # 打开文件
                self.logger.info(f"选择了菜单项: {item1.text()}")
                abs_path = self.table_data[rowNum].get("abs")
                self.logger.debug(f"select file abs path: {abs_path}")
                exec_(abs_path)
            elif action == item2:  # 打开文件夹
                self.logger.info(f"选择了菜单项: {item1.text()}")
                dir_path = self.table_data[rowNum].get("dir")
                self.logger.debug(f"select file abs path: {dir_path}")
                exec_(dir_path)
        elif colNum == dirNameColIndex:
            menu = QMenu()
            item1 = menu.addAction("打开文件夹")
            # 相对于窗口的坐标系转换为相对于屏幕的坐标系  映射到全局
            screePos = self.ui.tableWidget.mapToGlobal(pos)
            action = menu.exec(screePos)  # 获取全局坐标系下该位置的动作
            if action == item1:  # 打开文件
                self.logger.info(f"选择了菜单项: {item1.text()}")
                dir_path = self.table_data[rowNum].get("dir")
                self.logger.debug(f"select file abs path: {dir_path}")
                exec_(dir_path)
        return

    def double_click_table_item(self, index):
        text = index.data()
        row = index.row()
        col = index.column()
        self.logger.debug(f"double clicked: {text}. at: {{{row=}, {col=}}}")
        if col == fileNameColIndex:  # 打开文件
            abs_path = self.table_data[row].get('abs')  # 用户文件的绝对路径
            self.logger.info(f"open file {abs_path}")
            exec_(abs_path)
        elif col == dirNameColIndex:  # 打开文件夹
            abs_path = self.table_data[row].get('dir')  # 用户文件的绝对路径
            self.logger.info(f"open dir {abs_path}")
            exec_(abs_path)

    def connect_to_slot(self):
        """
        将事件连接到槽
        :param self:
        :return:
        """

        # 设置允许弹出菜单 单击右键响应事件
        self.ui.tableWidget.setContextMenuPolicy(CoreQt.CustomContextMenu)
        # 在搜索框按下回车
        self.ui.lineEdit.returnPressed.connect(self.search_click)
        # 点击搜索按钮
        self.ui.pushButton.clicked.connect(self.search_click)
        # 搜索类型切换
        self.ui.comboBox.currentIndexChanged.connect(self.search_type_change)
        # 右键单击
        self.ui.tableWidget.customContextMenuRequested.connect(self.right_click_table_item)
        # 双击打开 文件或文件夹
        self.ui.tableWidget.doubleClicked.connect(self.double_click_table_item)
        # 编辑设置

        # 获取当前字体大小

        # 更改字体大小


def gui_start():
    UI = MainWindow()
    # 显示界面
    UI.show()
    sys.exit(UI.app.exec_())
