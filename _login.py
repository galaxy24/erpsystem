# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QPalette


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("#Form{background-color: rgb(45, 46, 47)}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 80, 60, 16))
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: white")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 140, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color: white")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(170, 75, 131, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(175, 140, 121, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setStyleSheet("border:1px solid gray;width:300px;"
                                      "border-radius:6px;padding:2px 4px;")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 210, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton{color:black;border:1px solid #F3F3F5;border-radius:10px;background:Gray;}"
                                      "QPushButton:hover{color:black;border:1px solid #F3F3F5;border-radius:10px;background:LightGray;}")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 210, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{color:black;border:1px solid #F3F3F5;border-radius:10px;background:Gray;}"
                                      "QPushButton:hover{color:black;border:1px solid #F3F3F5;border-radius:10px;background:LightGray;}")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "辉腾報單管理系统"))
        self.label.setText(_translate("Form", "Account:"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.comboBox.setItemText(0, _translate("Form", "Admin"))
        self.comboBox.setItemText(1, _translate("Form", "User"))
        self.pushButton.setText(_translate("Form", "Enter"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        Form.setWindowOpacity(0.95) # 设置窗口透明度
        #Ui_MainWindow3.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
        #pe = QPalette()
        #Form.setAutoFillBackground(True)
        #pe.setColor(QPalette.Window, Qt.darkGray)  #设置背景色
        #pe.setColor(QPalette.Background,Qt.blue)
        #Form.setPalette(pe)

    def close(self):
        self.close()
