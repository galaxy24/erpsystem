# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentBox.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FinanceBox(object):
    def setupUi(self, FinanceBox):
        FinanceBox.setObjectName("FinanceBox")
        FinanceBox.resize(1780, 880)
        FinanceBox.setStyleSheet("#StudentBox{background-color: rgb(238, 233, 233)}")

        self.searchEdit = QtWidgets.QLineEdit(FinanceBox)
        self.searchEdit.setGeometry(QtCore.QRect(10, 10, 350, 35))
        self.searchEdit.setObjectName("searchEdit")
        self.searchEdit.setStyleSheet("border:1px solid gray;width:300px;"
                                      "border-radius:6px;padding:2px 4px;")

        self.searchBox = QtWidgets.QComboBox(FinanceBox)
        self.searchBox.setGeometry(QtCore.QRect(360, 10, 90, 35))
        self.searchBox.setWhatsThis("")
        self.searchBox.setObjectName("searchBox")
        self.searchBox.addItem("")
        self.searchBox.addItem("")
        self.searchBox.setStyleSheet("border:1px solid gray;width:300px;border-radius:6px;padding:2px 4px;")

        self.searchBox_2 = QtWidgets.QComboBox(FinanceBox)
        self.searchBox_2.setGeometry(QtCore.QRect(460, 10, 90, 35))
        self.searchBox_2.setWhatsThis("")
        self.searchBox_2.setObjectName("searchBox_2")
        self.searchBox_2.addItem("")
        self.searchBox_2.addItem("")
        self.searchBox_2.addItem("")
        self.searchBox_2.setStyleSheet("border:1px solid gray;width:300px;border-radius:6px;padding:2px 4px;")

        self.searchDate_1 = QtWidgets.QDateEdit(FinanceBox)
        self.searchDate_1.setGeometry(QtCore.QRect(560, 10, 140, 35))
        self.searchDate_1.setObjectName("searchDate1")
        self.searchDate_1.setDate(QtCore.QDate.currentDate())
        self.searchDate_1.setStyleSheet("border:1px solid gray;width:300px;border-radius:6px;padding:2px 4px;")
        self.searchDate_2 = QtWidgets.QDateEdit(FinanceBox)
        self.searchDate_2.setGeometry(QtCore.QRect(725, 10, 140, 35))
        self.searchDate_2.setObjectName("searchDate2")
        self.searchDate_2.setDate(QtCore.QDate.currentDate())
        self.searchDate_2.setStyleSheet("border:1px solid gray;width:300px;border-radius:6px;padding:2px 4px;")
        self.label_range = QtWidgets.QLabel(FinanceBox)
        self.label_range.setGeometry(QtCore.QRect(705, 10, 15, 35))

        self.financeTable = QtWidgets.QTreeWidget(FinanceBox)
        self.financeTable.setGeometry(QtCore.QRect(10, 50, 1200, 500))
        self.financeTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.financeTable.setObjectName("financeTable")
        self.financeTable.header().setVisible(True)
        self.financeTable.header().setSortIndicatorShown(True)

        self.totalTable = QtWidgets.QTreeWidget(FinanceBox)
        self.totalTable.setGeometry(QtCore.QRect(10, 50, 1200, 500))
        self.totalTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.totalTable.setObjectName("totalTable")
        self.totalTable.header().setVisible(True)
        self.totalTable.header().setSortIndicatorShown(True)

        self.stackedWidget = QtWidgets.QStackedWidget(FinanceBox)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 50, 1200, 500))
        self.stackedWidget.addWidget(self.financeTable)
        self.stackedWidget.addWidget(self.totalTable)

        self.pageComboBox = QtWidgets.QComboBox(FinanceBox)
        self.pageComboBox.setGeometry(QtCore.QRect(880, 10, 110, 35))
        self.pageComboBox.addItem("賬單信息")
        self.pageComboBox.addItem("銷售總賬")
        self.pageComboBox.activated[int].connect(self.stackedWidget.setCurrentIndex)
        self.pageComboBox.setStyleSheet("border:1px solid gray;width:300px;border-radius:6px;padding:2px 4px;")

        ##2020.1.21
        self.financeprintButton = QtWidgets.QPushButton(FinanceBox)
        self.financeprintButton.setGeometry(QtCore.QRect(1000, 10, 100, 35))
        self.financeprintButton.setObjectName("financeprintButton")
        self.financeprintButton.setStyleSheet(
            "QPushButton{color:black;border:1px solid #F3F3F5;border-radius:10px;background:White;}"
            "QPushButton:hover{color:black;border:1px solid #F3F3F5;border-radius:10px;background:Gray;}")


        self.groupBox = QtWidgets.QGroupBox(FinanceBox)
        self.groupBox.setGeometry(QtCore.QRect(1220, 50, 550, 500))
        #self.groupBox.setStyleSheet("#groupBox{background-color:rgb(250, 250, 250);border:1px solid gray;width:300px;"
        #                            "border-radius:10px;padding:2px 4px;}")
        self.groupBox.setObjectName("groupBox")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 50, 150, 60))
        self.label.setAlignment(QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 150, 60))
        self.label_2.setAlignment(QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 210, 150, 60))
        self.label_3.setAlignment(QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(50, 290, 150, 60))
        self.label_4.setAlignment(QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(50, 370, 150, 60))
        self.label_5.setAlignment(QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(50, 450, 150, 60))
        self.label_6.setAlignment(QtCore.Qt.AlignLeft)
        self.label_6.setObjectName("label_6")

        self.jiesuan1Label = QtWidgets.QLabel(self.groupBox)
        self.jiesuan1Label.setGeometry(QtCore.QRect(240, 50, 200, 60))
        self.jiesuan1Label.setText("")
        self.jiesuan1Label.setAlignment(QtCore.Qt.AlignLeft)
        self.jiesuan1Label.setWordWrap(True)
        self.jiesuan1Label.setObjectName("jiesuan1Label")
        self.shoukuan1Label = QtWidgets.QLabel(self.groupBox)
        self.shoukuan1Label.setGeometry(QtCore.QRect(240, 130, 200, 60))
        self.shoukuan1Label.setText("")
        self.shoukuan1Label.setAlignment(QtCore.Qt.AlignLeft)
        self.shoukuan1Label.setWordWrap(True)
        self.shoukuan1Label.setObjectName("shoukuan1Label")
        self.weifu1Label = QtWidgets.QLabel(self.groupBox)
        self.weifu1Label.setGeometry(QtCore.QRect(240, 210, 200, 60))
        self.weifu1Label.setText("")
        self.weifu1Label.setAlignment(QtCore.Qt.AlignLeft)
        self.weifu1Label.setWordWrap(True)
        self.weifu1Label.setObjectName("weifu1Label")
        self.jiesuan2Label = QtWidgets.QLabel(self.groupBox)
        self.jiesuan2Label.setGeometry(QtCore.QRect(240, 290, 200, 60))
        self.jiesuan2Label.setText("")
        self.jiesuan2Label.setAlignment(QtCore.Qt.AlignLeft)
        self.jiesuan2Label.setWordWrap(True)
        self.jiesuan2Label.setObjectName("jiesuan2Label")
        self.shoukuan2Label = QtWidgets.QLabel(self.groupBox)
        self.shoukuan2Label.setGeometry(QtCore.QRect(240, 370, 200, 60))
        self.shoukuan2Label.setText("")
        self.shoukuan2Label.setAlignment(QtCore.Qt.AlignLeft)
        self.shoukuan2Label.setWordWrap(True)
        self.shoukuan2Label.setObjectName("shoukuan2Label")
        self.weifu2Label = QtWidgets.QLabel(self.groupBox)
        self.weifu2Label.setGeometry(QtCore.QRect(240, 450, 200, 60))
        self.weifu2Label.setText("")
        self.weifu2Label.setAlignment(QtCore.Qt.AlignLeft)
        self.weifu2Label.setWordWrap(True)
        self.weifu2Label.setObjectName("weifu2Label")

        self.calcuTable = QtWidgets.QTreeWidget(FinanceBox)
        self.calcuTable.setGeometry(QtCore.QRect(10, 560, 1760, 300))
        self.calcuTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.calcuTable.setObjectName("calcuTable")
        self.calcuTable.header().setVisible(True)
        self.calcuTable.header().setSortIndicatorShown(True)

        #2020.1.21
        self.actionFinancePrint = QtWidgets.QAction(FinanceBox)
        self.actionFinancePrint.setObjectName("actionFinancePrint")

        self.retranslateUi(FinanceBox)
        QtCore.QMetaObject.connectSlotsByName(FinanceBox)

    def retranslateUi(self, FinanceBox):
        _translate = QtCore.QCoreApplication.translate
        FinanceBox.setWindowTitle(_translate("FinanceBox", "財務信息匯總"))
        self.searchBox.setStatusTip(_translate("MainWindow", "快速检索项"))
        self.searchBox.setItemText(0, _translate("MainWindow", "客戶"))
        self.searchBox.setItemText(1, _translate("MainWindow", "賬單編號"))

        self.searchBox_2.setStatusTip(_translate("MainWindow", "時間檢索項"))
        self.searchBox_2.setItemText(0, _translate("MainWindow", "不限日期"))
        self.searchBox_2.setItemText(1, _translate("MainWindow", "結算日期"))
        self.searchBox_2.setItemText(2, _translate("MainWindow", "收款日期"))

        self.label_range.setText(_translate("MainWindow", "——"))

        self.financeTable.setStatusTip(_translate("MainWindow", "賬單信息"))
        self.financeTable.setSortingEnabled(True)
        self.financeTable.headerItem().setText(0, _translate("MainWindow", "客戶"))
        self.financeTable.headerItem().setText(1, _translate("MainWindow", "賬單日期"))
        self.financeTable.headerItem().setText(2, _translate("MainWindow", "計價貨幣"))
        self.financeTable.headerItem().setText(3, _translate("MainWindow", "結算費用"))
        self.financeTable.headerItem().setText(4, _translate("MainWindow", "賬單編號"))
        self.financeTable.headerItem().setText(5, _translate("MainWindow", "已收款項"))
        self.financeTable.headerItem().setText(6, _translate("MainWindow", "收款日期"))

        self.totalTable.setStatusTip(_translate("MainWindow", "銷售總賬信息"))
        self.totalTable.setSortingEnabled(True)
        self.totalTable.headerItem().setText(0, _translate("MainWindow", "客戶"))
        self.totalTable.headerItem().setText(1, _translate("MainWindow", "計價貨幣"))
        self.totalTable.headerItem().setText(2, _translate("MainWindow", "需結算費用"))
        self.totalTable.headerItem().setText(3, _translate("MainWindow", "已收款項"))
        self.totalTable.headerItem().setText(4, _translate("MainWindow", "未付款項"))

        self.groupBox.setTitle(_translate("MainWindow", "總賬信息"))
        self.label.setText(_translate("MainWindow", "縂結算費用(人民幣)"))
        self.label_2.setText(_translate("MainWindow", "縂收款(人民幣)"))
        self.label_3.setText(_translate("MainWindow", "未付款(人民幣)"))
        self.label_4.setText(_translate("MainWindow", "總結算費用(港幣)"))
        self.label_5.setText(_translate("MainWindow", "縂收款(港幣)"))
        self.label_6.setText(_translate("MainWindow", "未付款(港幣)"))

        self.calcuTable.setStatusTip(_translate("MainWindow", "双击修改信息"))
        self.calcuTable.setSortingEnabled(True)
        self.calcuTable.headerItem().setText(0, _translate("MainWindow", "客戶"))
        self.calcuTable.headerItem().setText(1, _translate("MainWindow", "日期"))
        self.calcuTable.headerItem().setText(2, _translate("MainWindow", "賬單編號"))
        self.calcuTable.headerItem().setText(3, _translate("MainWindow", "訂單序號"))
        self.calcuTable.headerItem().setText(4, _translate("MainWindow", "計價單位"))
        self.calcuTable.headerItem().setText(5, _translate("MainWindow", "合計費用"))
        self.calcuTable.headerItem().setText(6, _translate("MainWindow", "櫃號"))
        self.calcuTable.headerItem().setText(7, _translate("MainWindow", "報來件數"))
        self.calcuTable.headerItem().setText(8, _translate("MainWindow", "提櫃日期"))
        self.calcuTable.headerItem().setText(9, _translate("MainWindow", "租櫃號"))
        self.calcuTable.headerItem().setText(10, _translate("MainWindow", "租櫃日期"))
        self.calcuTable.headerItem().setText(11, _translate("MainWindow", "租櫃費"))
        self.calcuTable.headerItem().setText(12, _translate("MainWindow", "原櫃插電日期"))
        self.calcuTable.headerItem().setText(13, _translate("MainWindow", "原櫃打冷"))
        self.calcuTable.headerItem().setText(14, _translate("MainWindow", "租櫃插電日期"))
        self.calcuTable.headerItem().setText(15, _translate("MainWindow", "租櫃打冷"))
        self.calcuTable.headerItem().setText(16, _translate("MainWindow", "轉櫃號"))
        self.calcuTable.headerItem().setText(17, _translate("MainWindow", "打包費"))
        self.calcuTable.headerItem().setText(18, _translate("MainWindow", "閘費"))
        self.calcuTable.headerItem().setText(19, _translate("MainWindow", "吊費"))
        self.calcuTable.headerItem().setText(20, _translate("MainWindow", "過磅洗櫃費"))
        self.calcuTable.headerItem().setText(21, _translate("MainWindow", "出口船運費"))
        self.calcuTable.headerItem().setText(22, _translate("MainWindow", "拖車費"))
        self.calcuTable.headerItem().setText(23, _translate("MainWindow", "維修費"))

        self.financeprintButton.setStatusTip(_translate("MainWindow", "打印财务單"))
        self.financeprintButton.setText(_translate("MainWindow", "打印财务單"))
        self.actionFinancePrint.setText(_translate("MainWindow", "打印财务單..."))
        self.actionFinancePrint.setStatusTip(_translate("MainWindow", "打印财务單"))