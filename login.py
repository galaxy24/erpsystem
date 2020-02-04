from PyQt5 import QtWidgets, QtCore, QtGui
from _login import Ui_Form
from PyQt5.QtCore import *
from mainUI import MainWindow
from mainUI_2 import MainWindow_2
from PyQt5.QtWidgets import *
#from PyQt5.QtWidgets import QMessageBox
import public
import sys


class LoginWindow(object):
    """主窗口封装类"""

    def __init__(self):

        self.dialog = QtWidgets.QMainWindow()
        window = Ui_Form()
        window.setupUi(self.dialog)
        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialog.setWindowIcon(icon)

        self.label = window.label
        self.label_2 = window.label_2
        self.comboBox = window.comboBox
        self.lineEdit = window.lineEdit
        self.pushButton = window.pushButton
        self.pushButton_2 = window.pushButton_2

        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton.setShortcut(QtCore.Qt.Key_Return)
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)

    def show(self):
        self.dialog.show()

    def on_pushButton_clicked(self):
        # 账号判断
        public.loginDialog = MainWindow()
        public.loginDialog_2 = MainWindow_2()
        account = self.comboBox.currentText()
        pwd = self.lineEdit.text()
        print(account, pwd)
        if account == "Admin" and pwd == "111111":
            #print("111")
            public.loginDialog.show()
            self.close()
        else:
            if account == "User" and pwd == "222222":
                public.loginDialog_2.show()
                self.close()
            else:
                QMessageBox.warning(QtWidgets.QWidget(), "警告", "用户名或密码错误！", QMessageBox.Ok)
                self.lineEdit.setFocus()

    def close(self):
        self.dialog.close()

        # 通过验证，关闭对话框并返回1
        #self.accept()
