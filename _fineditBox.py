# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fineditBox.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FineditBox(object):
    def setupUi(self, FineditBox):
        FineditBox.setObjectName("FineditBox")
        FineditBox.resize(450, 530)
        FineditBox.setStyleSheet("#FineditBox{background-color: rgb(190, 190, 190)}")
        self.centralwidget = QtWidgets.QWidget(FineditBox)
        self.centralwidget.setObjectName("FineditBox")

        self.label = QtWidgets.QLabel(FineditBox)
        self.label.setGeometry(QtCore.QRect(40, 50, 80, 40))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FineditBox)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 80, 40))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(FineditBox)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 80, 40))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FineditBox)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 80, 40))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(FineditBox)
        self.label_5.setGeometry(QtCore.QRect(40, 250, 80, 40))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(FineditBox)
        self.label_6.setGeometry(QtCore.QRect(40, 300, 80, 40))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(FineditBox)
        self.label_7.setGeometry(QtCore.QRect(40, 350, 80, 40))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(FineditBox)
        self.label_8.setGeometry(QtCore.QRect(40, 400, 80, 40))
        self.label_8.setObjectName("label_8")

        self.indexEdit = QtWidgets.QLineEdit(FineditBox)
        self.indexEdit.setGeometry(QtCore.QRect(160, 50, 201, 40))
        self.indexEdit.setClearButtonEnabled(True)
        self.indexEdit.setObjectName("indexEdit")
        self.indexEdit.setReadOnly(True)

        self.dateEdit = QtWidgets.QDateEdit(FineditBox)
        self.dateEdit.setGeometry(QtCore.QRect(160, 100, 201, 40))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setReadOnly(True)

        self.clientEdit = QtWidgets.QLineEdit(FineditBox)
        self.clientEdit.setGeometry(QtCore.QRect(160, 150, 201, 40))
        self.clientEdit.setClearButtonEnabled(True)
        self.clientEdit.setObjectName("clientEdit")
        self.clientEdit.setReadOnly(True)

        self.unitEdit = QtWidgets.QComboBox(FineditBox)
        self.unitEdit.setGeometry(QtCore.QRect(160, 200, 201, 40))
        self.unitEdit.addItem("人民幣")
        self.unitEdit.addItem("港幣")
        self.unitEdit.setObjectName("unitEdit")

        self.jiesuanEdit = QtWidgets.QLineEdit(FineditBox)
        self.jiesuanEdit.setGeometry(QtCore.QRect(160, 250, 201, 40))
        self.jiesuanEdit.setClearButtonEnabled(True)
        self.jiesuanEdit.setObjectName("jiesuanEdit")
        self.notesEdit = QtWidgets.QLineEdit(FineditBox)
        self.notesEdit.setGeometry(QtCore.QRect(160, 300, 201, 40))
        self.notesEdit.setClearButtonEnabled(True)
        self.notesEdit.setObjectName("jiesuanEdit")
        self.shoukuanEdit = QtWidgets.QLineEdit(FineditBox)
        self.shoukuanEdit.setGeometry(QtCore.QRect(160, 350, 201, 40))
        self.shoukuanEdit.setClearButtonEnabled(True)
        self.shoukuanEdit.setObjectName("shoukuanEdit")
        self.date2Edit = QtWidgets.QDateEdit(FineditBox)
        self.date2Edit.setGeometry(QtCore.QRect(160, 400, 201, 40))
        self.date2Edit.setObjectName("dateEdit")

        self.okButton = QtWidgets.QPushButton(FineditBox)
        self.okButton.setGeometry(QtCore.QRect(50, 460, 120, 40))
        self.okButton.setObjectName("okButton")
        self.okButton.setStyleSheet(
            "QPushButton{color:black;border:1px solid #F3F3F5;border-radius:10px;background:Gray;}"
            "QPushButton:hover{color:black;border:1px solid #F3F3F5;border-radius:10px;background:LightGray;}")

        self.cancelButton = QtWidgets.QPushButton(FineditBox)
        self.cancelButton.setGeometry(QtCore.QRect(220, 460, 120, 40))
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.setStyleSheet(
            "QPushButton{color:black;border:1px solid #F3F3F5;border-radius:10px;background:Gray;}"
            "QPushButton:hover{color:black;border:1px solid #F3F3F5;border-radius:10px;background:LightGray;}")

        # tab键设置
        self.retranslateUi(FineditBox)
        QtCore.QMetaObject.connectSlotsByName(FineditBox)
        FineditBox.setTabOrder(self.dateEdit, self.clientEdit)
        FineditBox.setTabOrder(self.clientEdit, self.unitEdit)
        FineditBox.setTabOrder(self.unitEdit, self.jiesuanEdit)
        FineditBox.setTabOrder(self.jiesuanEdit, self.notesEdit)
        FineditBox.setTabOrder(self.notesEdit, self.shoukuanEdit)
        FineditBox.setTabOrder(self.shoukuanEdit, self.date2Edit)
        FineditBox.setTabOrder(self.date2Edit, self.okButton)
        FineditBox.setTabOrder(self.okButton, self.cancelButton)

    def retranslateUi(self, FinanceBox):
        _translate = QtCore.QCoreApplication.translate
        FinanceBox.setWindowTitle(_translate("FinanceBox", "財務信息"))

        self.label.setText(_translate("FinanceBox", "序號"))
        self.label_2.setText(_translate("FinanceBox", "日期"))
        self.label_3.setText(_translate("FinanceBox", "客戶"))
        self.label_4.setText(_translate("FinanceBox", "計價單位"))
        self.label_5.setText(_translate("FinanceBox", "結算費用"))
        self.label_6.setText(_translate("FinanceBox", "賬單編號"))
        self.label_7.setText(_translate("FinanceBox", "已收款項"))
        self.label_8.setText(_translate("FinanceBox", "收款日期"))
        self.okButton.setText(_translate("FinanceBox", "确定"))
        self.cancelButton.setText(_translate("FinanceBox", "取消"))
