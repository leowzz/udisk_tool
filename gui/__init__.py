#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2023/1/10
# @file utils_test.py.py
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox, QMenu
)
from .ui_mainWindow import Ui_MainWindow
from PyQt5.QtCore import Qt as CoreQt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        # 必须在父类初始化之前调用, 否则返回代码 -1073740791 (0xC0000409)
        self.app = QApplication(sys.argv)
        super().__init__()
        # 导入UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 将点击信号绑定到按钮
        # self.ui.pushButton.clicked.connect(self.handle_click)
        # 设置允许弹出菜单  单击右键响应事件
        self.ui.tableWidget.setContextMenuPolicy(CoreQt.CustomContextMenu)
        # 将信号请求连接到一个槽
        self.ui.tableWidget.customContextMenuRequested.connect(self.generateMenu)

    # 槽方法
    def generateMenu(self, pos):
        # pos 为单击鼠标右键的坐标  相对于窗口
        # 鼠标右键单击前两行弹出菜单，单击第三行没响应
        print(pos)
        # 当前选中的行
        rowNum = self.ui.tableWidget.selectionModel().selection().indexes()[0].row()
        colNum = self.ui.tableWidget.selectionModel().selection().indexes()[0].column()
        # for i in self.ui.tableWidget.selectionModel().selection().indexes():
        #     rowNum = i.row()

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

    def handle_click(self):
        info = self.ui.plainTextEdit.toPlainText()

        # 薪资20000 以上 和 以下 的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            # 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            name, salary, age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(
            self.ui.centralwidget,
            '统计结果',
            f'薪资20000 以上的有：\n{salary_above_20k}\n\n'
            f'薪资20000 以下的有：\n{salary_below_20k}'
        )

    def test(self):
        self.ui.tableWidget.setRowCount(3)
        # item = self.ui.tableWidget.verticalHeaderItem(0)
        # item.setText(_translate("MainWindow", "新建行"))
        from PyQt5.Qt import QTableWidgetItem, QAbstractItemView
        # 设置表格内容不可编辑
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem('右键菜单编辑器.exe', ))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("J:01_工具\\键鼠工具\\"))
        self.ui.tableWidget.setItem(1, 0, QTableWidgetItem('右键菜单编辑器右键菜单编辑器.exe', ))
        # item = self.ui.tableWidget.item(0, 0)
        # item.setText(_translate("MainWindow", "右键菜单编辑器.exe"))
        # item = self.ui.tableWidget.item(0, 1)
        # item.setText(_translate("MainWindow", "J:01_工具\\键鼠工具\\"))


if __name__ == '__main__':
    demo = MainWindow()
    demo.test()
    demo.show()
    sys.exit(demo.app.exec_())
