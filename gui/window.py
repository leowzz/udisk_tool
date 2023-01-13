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
        self.ui.textEdit.setText(search_str)

    def draw_table(self):
        """
        渲染表格
        """

        # 设置行数
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


        # 搜索类型切换

        # 打开选定文件

        # 打开选定文件夹

        # 编辑设置

        # 获取当前字体大小

        # 更改字体大小

    def right_click_menu(self, pos):
        print(self, pos)
        # 右键单击
        # pos 为单击鼠标右键的坐标  相对于窗口
        # 鼠标右键单击前两行弹出菜单，单击第三行没响应
        print(pos)
        # 当前选中的行
        rowNum = self.ui.tableWidget.selectionModel().selection().indexes()[0].row()
        colNum = self.ui.tableWidget.selectionModel().selection().indexes()[0].column()
        # for i in self.ui.tableWidget.selectionModel().selection().indexes():
        #     rowNum = i.row()
        print(rowNum, colNum)
        # 如果选择的行索引小于2，弹出上下文菜单
        if rowNum < 2:
            menu = QMenu()
            item1 = menu.addAction("打开")
            item2 = menu.addAction("打开所在文件夹")
            item3 = menu.addAction("菜单项3")
            # 相对于窗口的坐标系转换为相对于屏幕的坐标系  映射到全局
            screePos = self.ui.tableWidget.mapToGlobal(pos)
            print(screePos)
            # 被阻塞
            # action = menu.exec(pos)
            action = menu.exec(screePos)
            if action == item1:
                print('选择了第1个菜单项',
                      self.ui.tableWidget.item(rowNum, colNum).text(),
                      self.ui.tableWidget.item(rowNum, 0).text(),
                      self.ui.tableWidget.item(rowNum, 1).text())
            elif action == item2:
                print('选择了第2个菜单项', self.ui.tableWidget.item(rowNum, 0).text(),
                      self.ui.tableWidget.item(rowNum, 1).text())
            elif action == item3:
                print('选择了第3个菜单项', self.ui.tableWidget.item(rowNum, 0).text(),
                      self.ui.tableWidget.item(rowNum, 1).text())
            else:
                return

    def connect_to_slot(self):
        """
        将事件连接到槽
        :param self:
        :return:
        """

        # 将点击信号绑定到按钮
        # self.ui.pushButton.clicked.connect(self.handle_click)
        # # 设置允许弹出菜单  单击右键响应事件
        self.ui.tableWidget.setContextMenuPolicy(CoreQt.CustomContextMenu)
        # # 将信号请求连接到一个槽
        self.ui.tableWidget.customContextMenuRequested.connect(self.right_click_menu)
        # self.ui.tableWidget.customContextMenuRequested.connect(
        #     lambda customContextMenuRequested: right_click_menu(self, customContextMenuRequested)
        # )

        # 点击搜索按钮
        self.ui.pushButton.clicked.connect(self.search_click)
        # 搜索类型切换

        # 右键单击

        # 打开选定文件

        # 打开选定文件夹

        # 编辑设置

        # 获取当前字体大小

        # 更改字体大小


def gui_start():
    UI = MainWindow()
    # 显示界面
    UI.show()
    sys.exit(UI.app.exec_())
