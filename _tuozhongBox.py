# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalculatorBox.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TuozhongBox(object):
    def setupUi(self, TuozhongBox):
        TuozhongBox.setObjectName("TuozhongBox")
        TuozhongBox.resize(1000, 500)
        TuozhongBox.setStyleSheet("#TuozhongBox{background-color: rgb(190, 190, 190)}")
        self.centralwidget = QtWidgets.QWidget(TuozhongBox)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(TuozhongBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 90, 40))
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.tindexEdit = QtWidgets.QLineEdit(TuozhongBox)
        self.tindexEdit.setGeometry(QtCore.QRect(130, 40, 200, 40))
        self.tindexEdit.setDragEnabled(False)
        self.tindexEdit.setClearButtonEnabled(True)
        self.tindexEdit.setObjectName("tindexEdit")
        self.tindexEdit.setReadOnly(True)

        self.label_2 = QtWidgets.QLabel(TuozhongBox)
        self.label_2.setGeometry(QtCore.QRect(330, 40, 90, 40))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(TuozhongBox)
        self.dateEdit.setGeometry(QtCore.QRect(430, 40, 200, 40))
        self.dateEdit.setObjectName("dateEdit")

        self.label_3 = QtWidgets.QLabel(TuozhongBox)
        self.label_3.setGeometry(QtCore.QRect(630, 40, 90, 40))
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.indexEdit = QtWidgets.QLineEdit(TuozhongBox)
        self.indexEdit.setGeometry(QtCore.QRect(730, 40, 200, 40))
        self.indexEdit.setClearButtonEnabled(True)
        self.indexEdit.setObjectName("indexEdit")

        self.label_4 = QtWidgets.QLabel(TuozhongBox)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 90, 40))
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.clientEdit = QtWidgets.QLineEdit(TuozhongBox)
        self.clientEdit.setGeometry(QtCore.QRect(130, 90, 200, 40))
        self.clientEdit.setClearButtonEnabled(True)
        self.clientEdit.setObjectName("clientEdit")
		
        self.label_5 = QtWidgets.QLabel(TuozhongBox)
        self.label_5.setGeometry(QtCore.QRect(330, 90, 90, 40))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.yuanguihaoEdit = QtWidgets.QLineEdit(TuozhongBox)
        self.yuanguihaoEdit.setGeometry(QtCore.QRect(430, 90, 200, 40))
        self.yuanguihaoEdit.setClearButtonEnabled(True)
        self.yuanguihaoEdit.setObjectName("yuanguihaoEdit")

        self.label_6 = QtWidgets.QLabel(TuozhongBox)
        self.label_6.setGeometry(QtCore.QRect(630, 90, 90, 40))
        self.label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.zhongweiEdit = QtWidgets.QLineEdit(TuozhongBox)
        self.zhongweiEdit.setGeometry(QtCore.QRect(730, 90, 200, 40))
        self.zhongweiEdit.setClearButtonEnabled(True)
        self.zhongweiEdit.setObjectName("zhongweiEdit")

        self.label_7 = QtWidgets.QLabel(TuozhongBox)
        self.label_7.setGeometry(QtCore.QRect(30, 150, 90, 40))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.jiweiEdit = QtWidgets.QLineEdit(TuozhongBox)
        self.jiweiEdit.setGeometry(QtCore.QRect(130, 150, 200, 40))
        self.jiweiEdit.setClearButtonEnabled(True)
        self.jiweiEdit.setObjectName("jiweiEdit")

        self.label_8 = QtWidgets.QLabel(TuozhongBox)
        self.label_8.setGeometry(QtCore.QRect(330, 150, 90, 40))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.shishoujianshuEdit = QtWidgets.QLineEdit(TuozhongBox)
        self.shishoujianshuEdit.setGeometry(QtCore.QRect(430, 150, 200, 40))
        self.shishoujianshuEdit.setClearButtonEnabled(True)
        self.shishoujianshuEdit.setObjectName("shishoujianshuEdit")


        self.label_9 = QtWidgets.QLabel(TuozhongBox)
        self.label_9.setGeometry(QtCore.QRect(630, 150, 90, 40))
        self.label_9.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.jingzhongEdit = QtWidgets.QLineEdit(TuozhongBox)
        self.jingzhongEdit.setGeometry(QtCore.QRect(730, 150, 200, 40))
        self.jingzhongEdit.setClearButtonEnabled(True)
        self.jingzhongEdit.setObjectName("jingzhongEdit")

        self.label_10 = QtWidgets.QLabel(TuozhongBox)
        self.label_10.setGeometry(QtCore.QRect(30, 210, 90, 40))
        self.label_10.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.maozhongEdit = QtWidgets.QLineEdit(TuozhongBox)
        self.maozhongEdit.setGeometry(QtCore.QRect(130, 210, 200, 40))
        self.maozhongEdit.setClearButtonEnabled(True)
        self.maozhongEdit.setObjectName("maozhongEdit")

        self.label_11 = QtWidgets.QLabel(TuozhongBox)
        self.label_11.setGeometry(QtCore.QRect(330, 210, 90, 40))
        self.label_11.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.huomingEdit = QtWidgets.QLineEdit(TuozhongBox)
        self.huomingEdit.setGeometry(QtCore.QRect(430, 210, 200, 40))
        self.huomingEdit.setClearButtonEnabled(True)
        self.huomingEdit.setObjectName("huomingEdit")

        self.label_12 = QtWidgets.QLabel(TuozhongBox)
        self.label_12.setGeometry(QtCore.QRect(630, 210, 90, 40))
        self.label_12.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.bangzhongEdit = QtWidgets.QLineEdit(TuozhongBox)
        self.bangzhongEdit.setGeometry(QtCore.QRect(730, 210, 200, 40))
        self.bangzhongEdit.setClearButtonEnabled(True)
        self.bangzhongEdit.setObjectName("bangzhongEdit")

        self.label_13 = QtWidgets.QLabel(TuozhongBox)
        self.label_13.setGeometry(QtCore.QRect(30, 270, 90, 40))
        self.label_13.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.noteEdit = QtWidgets.QPlainTextEdit(TuozhongBox)
        self.noteEdit.setGeometry(QtCore.QRect(130, 270, 800, 80))
        self.noteEdit.setObjectName("noteEdit")


        self.okButton = QtWidgets.QPushButton(TuozhongBox)
        self.okButton.setGeometry(QtCore.QRect(300, 380, 120, 40))
        self.okButton.setObjectName("okButton")
        self.okButton.setStyleSheet(
            "QPushButton{color:black;border:1px solid #F3F3F5;border-radius:10px;background:Gray;}"
            "QPushButton:hover{color:black;border:1px solid #F3F3F5;border-radius:10px;background:LightGray;}")

        self.cancelButton = QtWidgets.QPushButton(TuozhongBox)
        self.cancelButton.setGeometry(QtCore.QRect(500, 380, 120, 40))
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.setStyleSheet(
            "QPushButton{color:black;border:1px solid #F3F3F5;border-radius:10px;background:Gray;}"
            "QPushButton:hover{color:black;border:1px solid #F3F3F5;border-radius:10px;background:LightGray;}")

        self.msg = QtWidgets.QLabel(TuozhongBox)
        self.msg.setGeometry(QtCore.QRect(10, 5, 600, 40))
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")

        #tab键设置
        self.retranslateUi(TuozhongBox)
        QtCore.QMetaObject.connectSlotsByName(TuozhongBox)
        TuozhongBox.setTabOrder(self.indexEdit, self.dateEdit)
        TuozhongBox.setTabOrder(self.dateEdit, self.yuanguihaoEdit)
        TuozhongBox.setTabOrder(self.yuanguihaoEdit, self.zhongweiEdit)
        TuozhongBox.setTabOrder(self.zhongweiEdit, self.jiweiEdit)
        TuozhongBox.setTabOrder(self.jiweiEdit, self.shishoujianshuEdit)
        TuozhongBox.setTabOrder(self.shishoujianshuEdit, self.jingzhongEdit)
        TuozhongBox.setTabOrder(self.jingzhongEdit, self.maozhongEdit)
        TuozhongBox.setTabOrder(self.maozhongEdit, self.huomingEdit)
        TuozhongBox.setTabOrder(self.huomingEdit, self.bangzhongEdit)
        TuozhongBox.setTabOrder(self.bangzhongEdit, self.noteEdit)
        TuozhongBox.setTabOrder(self.noteEdit, self.okButton)
        TuozhongBox.setTabOrder(self.okButton, self.cancelButton)

    def retranslateUi(self, TuozhongBox):
        _translate = QtCore.QCoreApplication.translate
        TuozhongBox.setWindowTitle(_translate("TuozhongBox", "做貨工作單信息"))
        self.label.setText(_translate("TuozhongBox", "序號"))
        self.label_2.setText(_translate("TuozhongBox", "日期"))
        self.label_3.setText(_translate("TuozhongBox", "訂單序號"))
        self.label_4.setText(_translate("TuozhongBox", "客戶"))
        self.label_5.setText(_translate("TuozhongBox", "櫃號"))
        self.label_6.setText(_translate("TuozhongBox", "重尾"))
        self.label_7.setText(_translate("TuozhongBox", "吉尾"))
        self.label_8.setText(_translate("TuozhongBox", "件數"))
        self.label_9.setText(_translate("TuozhongBox", "淨重"))
        self.label_10.setText(_translate("TuozhongBox", "毛重"))
        self.label_11.setText(_translate("TuozhongBox", "貨名"))
        self.label_12.setText(_translate("TuozhongBox", "磅單重量"))
        self.label_13.setText(_translate("TuozhongBox", "備註"))


        self.okButton.setText(_translate("TuozhongBox", "确定"))
        self.cancelButton.setText(_translate("TuozhongBox", "取消"))
        self.msg.setText(_translate("TuozhongBox", "提示信息"))

        #CalculatorBox.setWindowOpacity(0.98)
        #CalculatorBox.setWindowFlag(QtCore.Qt.FramelessWindowHint)