# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QHeaderView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setObjectName("searchEdit")
        # 搜索输入框背景文字
        self.lineEdit.setPlaceholderText("此处输入要搜索的名称")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.lineEdit)
        # 字体大小提示标签
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        # 字体大小设置
        self.fontSize = QtWidgets.QSpinBox(self.centralwidget)
        self.fontSize.setProperty("value", 12)
        self.fontSize.setObjectName("fontSize")
        self.horizontalLayout.addWidget(self.fontSize)
        # 搜索类型
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName('typeComboBox')
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setObjectName("searchBut")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(600, 240))
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(320)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(320)

        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        # 设置允许按列排序
        self.tableWidget.setSortingEnabled(True)
        """
        # 用户可调整，默认值为setDefaultSectionSized的值
        table_obj.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        # 用户不可调整，默认值为setDefaultSectionSized的值
        table_obj.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        # 用户不可调整,自动平分适应可用区域
        table_obj.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 用户不可调整,自动适应内容的宽度
        table_obj.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # 用户可调整,默认值为setDefaultSectionSized的值
        table_obj.horizontalHeader().setSectionResizeMode(QHeaderView.Custom)
        """
        # 根据内容自动设置列宽
        # self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        # 设置选定列宽度
        # self.tableWidget.setColumnWidth(1, 400)

        self.verticalLayout.addWidget(self.tableWidget)
        # self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(1)
        # sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        # self.textEdit.setSizePolicy(sizePolicy)
        # self.textEdit.setMinimumSize(QtCore.QSize(0, 20))
        # self.textEdit.setMaximumSize(QtCore.QSize(16777212, 3204))
        # self.textEdit.setBaseSize(QtCore.QSize(0, 0))
        # self.textEdit.setObjectName("textEdit")
        # self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 27))
        self.menubar.setObjectName("menubar")
        self.menu_U = QtWidgets.QMenu(self.menubar)
        self.menu_U.setObjectName("menu_U")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        # self.action_2 = QtWidgets.QAction(MainWindow)
        # self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        # self.menu_U.addAction(self.action_2)
        self.menu_U.addAction(self.action)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menubar.addAction(self.menu_U.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "搜索"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "路径"))
        self.label.setText(_translate("MainWindow", "字体大小:"))
        self.comboBox.setCurrentText(_translate("MainWindow", "文件"))
        self.comboBox.setItemText(0, _translate("MainWindow", "文件"))
        self.comboBox.setItemText(1, _translate("MainWindow", "文件夹"))
        self.comboBox.setItemText(2, _translate("MainWindow", "后缀名"))
        # 设置表格标题加粗
        bold_font = self.tableWidget.horizontalHeader().font()
        bold_font.setBold(True)
        self.tableWidget.horizontalHeader().setFont(bold_font)

        # self.textEdit.setHtml(
        #     _translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        #                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        #                              "p, li { white-space: pre-wrap; }\n"
        #                              "</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
        #                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menu_U.setTitle(_translate("MainWindow", "文件"))
        self.menu.setTitle(_translate("MainWindow", "设置"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action.setText(_translate("MainWindow", "重新扫描"))
        # self.action_2.setText(_translate("MainWindow", "打开"))
        self.action_3.setText(_translate("MainWindow", "首选项"))
        self.action_4.setText(_translate("MainWindow", "字体大小"))
