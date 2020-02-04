# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalculatorBox.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ZuohuoBox(object):
    def setupUi(self, ZuohuoBox):
        ZuohuoBox.setObjectName("ZuohuoBox")
        ZuohuoBox.resize(1000, 540)
        ZuohuoBox.setStyleSheet("#ZuohuoBox{background-color: rgb(190, 190, 190)}")
        self.centralwidget = QtWidgets.QWidget(ZuohuoBox)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(ZuohuoBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 90, 40))
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.zindexEdit = QtWidgets.QLineEdit(ZuohuoBox)
        self.zindexEdit.setGeometry(QtCore.QRect(130, 40, 200, 40))
        self.zindexEdit.setDragEnabled(False)
        self.zindexEdit.setClearButtonEnabled(True)
        self.zindexEdit.setObjectName("zindexEdit")
        self.zindexEdit.setReadOnly(True)

        self.label_2 = QtWidgets.QLabel(ZuohuoBox)
        self.label_2.setGeometry(QtCore.QRect(330, 40, 90, 40))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(ZuohuoBox)
        self.dateEdit.setGeometry(QtCore.QRect(430, 40, 200, 40))
        self.dateEdit.setObjectName("dateEdit")

        self.label_3 = QtWidgets.QLabel(ZuohuoBox)
        self.label_3.setGeometry(QtCore.QRect(630, 40, 90, 40))
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.indexEdit = QtWidgets.QLineEdit(ZuohuoBox)
        self.indexEdit.setGeometry(QtCore.QRect(730, 40, 200, 40))
        self.indexEdit.setClearButtonEnabled(True)
        self.indexEdit.setObjectName("indexEdit")

        self.label_4 = QtWidgets.QLabel(ZuohuoBox)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 90, 40))
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.clientEdit = QtWidgets.QLineEdit(ZuohuoBox)
        self.clientEdit.setGeometry(QtCore.QRect(130, 90, 200, 40))
        self.clientEdit.setClearButtonEnabled(True)
        self.clientEdit.setObjectName("clientEdit")

        self.label_5 = QtWidgets.QLabel(ZuohuoBox)
        self.label_5.setGeometry(QtCore.QRect(330, 90, 90, 40))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.yuanguihaoEdit = QtWidgets.QLineEdit(ZuohuoBox)
        self.yuanguihaoEdit.setGeometry(QtCore.QRect(430, 90, 200, 40))
        self.yuanguihaoEdit.setClearButtonEnabled(True)
        self.yuanguihaoEdit.setObjectName("yuanguihaoEdit")

        self.label_6 = QtWidgets.QLabel(ZuohuoBox)
        self.label_6.setGeometry(QtCore.QRect(630, 90, 90, 40))
        self.label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.jianshuEdit = QtWidgets.QLineEdit(ZuohuoBox)
        self.jianshuEdit.setGeometry(QtCore.QRect(730, 90, 200, 40))
        self.jianshuEdit.setClearButtonEnabled(True)
        self.jianshuEdit.setObjectName("jianshuEdit")

        self.label_7 = QtWidgets.QLabel(ZuohuoBox)
        self.label_7.setGeometry(QtCore.QRect(30, 150, 90, 40))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.jingzhongEdit = QtWidgets.QLineEdit(ZuohuoBox)
        self.jingzhongEdit.setGeometry(QtCore.QRect(130, 150, 200, 40))
        self.jingzhongEdit.setClearButtonEnabled(True)
        self.jingzhongEdit.setObjectName("jingzhongEdit")

        self.label_8 = QtWidgets.QLabel(ZuohuoBox)
        self.label_8.setGeometry(QtCore.QRect(330, 150, 90, 40))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.maozhongEdit = QtWidgets.QLineEdit(ZuohuoBox)
        self.maozhongEdit.setGeometry(QtCore.QRect(430, 150, 200, 40))
        self.maozhongEdit.setClearButtonEnabled(True)
        self.maozhongEdit.setObjectName("maozhongEdit")


        self.label_9 = QtWidgets.QLabel(ZuohuoBox)
        self.label_9.setGeometry(QtCore.QRect(630, 150, 90, 40))
        self.label_9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.huomingEdit = QtWidgets.QLineEdit(ZuohuoBox)
        self.huomingEdit.setGeometry(QtCore.QRect(730, 150, 200, 40))
        self.huomingEdit.setClearButtonEnabled(True)
        self.huomingEdit.setObjectName("huomingEdit")

        self.label_10 = QtWidgets.QLabel(ZuohuoBox)
        self.label_10.setGeometry(QtCore.QRect(30, 210, 90, 40))
        self.label_10.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.shishoujianshuEdit = QtWidgets.QLineEdit(ZuohuoBox)
        self.shishoujianshuEdit.setGeometry(QtCore.QRect(130, 210, 200, 40))
        self.shishoujianshuEdit.setClearButtonEnabled(True)
        self.shishoujianshuEdit.setObjectName("shishoujianshuEdit")

        self.label_11 = QtWidgets.QLabel(ZuohuoBox)
        self.label_11.setGeometry(QtCore.QRect(330, 210, 90, 40))
        self.label_11.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.zhuangguihaoEdit = QtWidgets.QLineEdit(ZuohuoBox)
        self.zhuangguihaoEdit.setGeometry(QtCore.QRect(430, 210, 200, 40))
        self.zhuangguihaoEdit.setClearButtonEnabled(True)
        self.zhuangguihaoEdit.setObjectName("zhuangguihaoEdit")

        self.label_12 = QtWidgets.QLabel(ZuohuoBox)
        self.label_12.setGeometry(QtCore.QRect(30, 270, 90, 40))
        self.label_12.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.baozhuangEdit = QtWidgets.QLineEdit(ZuohuoBox)
        self.baozhuangEdit.setGeometry(QtCore.QRect(130, 270, 800, 40))
        self.baozhuangEdit.setClearButtonEnabled(True)
        self.baozhuangEdit.setObjectName("baozhuangEdit")

        self.label_13 = QtWidgets.QLabel(ZuohuoBox)
        self.label_13.setGeometry(QtCore.QRect(30, 320, 90, 40))
        self.label_13.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.noteEdit = QtWidgets.QPlainTextEdit(ZuohuoBox)
        self.noteEdit.setGeometry(QtCore.QRect(130, 320, 800, 80))
        self.noteEdit.setObjectName("noteEdit")


        self.okButton = QtWidgets.QPushButton(ZuohuoBox)
        self.okButton.setGeometry(QtCore.QRect(300, 440, 120, 40))
        self.okButton.setObjectName("okButton")
        self.okButton.setStyleSheet(
            "QPushButton{color:black;border:1px solid #F3F3F5;border-radius:10px;background:Gray;}"
            "QPushButton:hover{color:black;border:1px solid #F3F3F5;border-radius:10px;background:LightGray;}")

        self.cancelButton = QtWidgets.QPushButton(ZuohuoBox)
        self.cancelButton.setGeometry(QtCore.QRect(500, 440, 120, 40))
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.setStyleSheet(
            "QPushButton{color:black;border:1px solid #F3F3F5;border-radius:10px;background:Gray;}"
            "QPushButton:hover{color:black;border:1px solid #F3F3F5;border-radius:10px;background:LightGray;}")

        self.msg = QtWidgets.QLabel(ZuohuoBox)
        self.msg.setGeometry(QtCore.QRect(10, 5, 600, 40))
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")

        #tab键设置
        self.retranslateUi(ZuohuoBox)
        QtCore.QMetaObject.connectSlotsByName(ZuohuoBox)
        ZuohuoBox.setTabOrder(self.indexEdit, self.dateEdit)
        ZuohuoBox.setTabOrder(self.dateEdit, self.yuanguihaoEdit)
        ZuohuoBox.setTabOrder(self.yuanguihaoEdit, self.jianshuEdit)
        ZuohuoBox.setTabOrder(self.jianshuEdit, self.jingzhongEdit)
        ZuohuoBox.setTabOrder(self.jingzhongEdit, self.maozhongEdit)
        ZuohuoBox.setTabOrder(self.maozhongEdit, self.huomingEdit)
        ZuohuoBox.setTabOrder(self.huomingEdit, self.shishoujianshuEdit)
        ZuohuoBox.setTabOrder(self.shishoujianshuEdit, self.zhuangguihaoEdit)
        ZuohuoBox.setTabOrder(self.zhuangguihaoEdit, self.baozhuangEdit)
        ZuohuoBox.setTabOrder(self.baozhuangEdit, self.noteEdit)
        ZuohuoBox.setTabOrder(self.noteEdit, self.okButton)
        ZuohuoBox.setTabOrder(self.okButton, self.cancelButton)

    def retranslateUi(self, ZuohuoBox):
        _translate = QtCore.QCoreApplication.translate
        ZuohuoBox.setWindowTitle(_translate("ZuohuoBox", "做貨工作單信息"))
        self.label.setText(_translate("ZuohuoBox", "序號"))
        self.label_2.setText(_translate("ZuohuoBox", "日期"))
        self.label_3.setText(_translate("ZuohuoBox", "訂單序號"))
        self.label_4.setText(_translate("ZuohuoBox", "客戶"))
        self.label_5.setText(_translate("ZuohuoBox", "原櫃號"))
        self.label_6.setText(_translate("ZuohuoBox", "件數"))
        self.label_7.setText(_translate("ZuohuoBox", "淨重"))
        self.label_8.setText(_translate("ZuohuoBox", "毛重"))
        self.label_9.setText(_translate("ZuohuoBox", "貨名"))
        self.label_10.setText(_translate("ZuohuoBox", "實收件數"))
        self.label_11.setText(_translate("ZuohuoBox", "轉櫃號"))
        self.label_12.setText(_translate("ZuohuoBox", "包裝"))
        self.label_13.setText(_translate("ZuohuoBox", "備註"))

        self.okButton.setText(_translate("ZuohuoBox", "确定"))
        self.cancelButton.setText(_translate("ZuohuoBox", "取消"))
        self.msg.setText(_translate("ZuohuoBox", "提示信息"))

        #CalculatorBox.setWindowOpacity(0.98)
        #CalculatorBox.setWindowFlag(QtCore.Qt.FramelessWindowHint)