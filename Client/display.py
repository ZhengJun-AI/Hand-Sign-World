# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 620)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"border-image: url(:/imgs/background_final.png);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setStyleSheet("font: 24pt \"华文琥珀\";\n"
"color: rgb(0, 0, 255);")
        self.backButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/返回.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon1)
        self.backButton.setIconSize(QtCore.QSize(50, 50))
        self.backButton.setFlat(True)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setStyleSheet("font: 24pt \"华文琥珀\";\n"
"color: rgb(0, 0, 255);")
        self.openButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imgs/摄像头red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openButton.setIcon(icon2)
        self.openButton.setIconSize(QtCore.QSize(50, 50))
        self.openButton.setFlat(True)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout.addWidget(self.openButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setStyleSheet("font: 24pt \"华文琥珀\";\n"
"color: rgb(0, 0, 255);")
        self.saveButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imgs/录制.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon3)
        self.saveButton.setIconSize(QtCore.QSize(50, 50))
        self.saveButton.setFlat(True)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setStyleSheet("font: 24pt \"华文琥珀\";\n"
"color: rgb(0, 0, 255);")
        self.closeButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imgs/关闭摄像头.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon4)
        self.closeButton.setIconSize(QtCore.QSize(50, 50))
        self.closeButton.setFlat(True)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.getbgrButton = QtWidgets.QPushButton(self.centralwidget)
        self.getbgrButton.setText("")
        self.getbgrButton.setFlat(True)
        self.getbgrButton.setObjectName("getbgrButton")
        self.horizontalLayout.addWidget(self.getbgrButton)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 2)
        self.horizontalLayout.setStretch(5, 2)
        self.horizontalLayout.setStretch(6, 2)
        self.horizontalLayout.setStretch(7, 2)
        self.horizontalLayout.setStretch(8, 1)
        self.horizontalLayout.setStretch(9, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.displaylabel = QtWidgets.QLabel(self.centralwidget)
        self.displaylabel.setStyleSheet("background-color: rgba(0, 0, 0, 200);\n"
"")
        self.displaylabel.setText("")
        self.displaylabel.setScaledContents(True)
        self.displaylabel.setObjectName("displaylabel")
        self.verticalLayout.addWidget(self.displaylabel)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 20)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "解印世界"))


