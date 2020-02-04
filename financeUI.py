from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
from _financeBox import Ui_FinanceBox
import public
import fineditUI

from finance import Finance
from total import Total

class FinanceBox(object):
    """財務信息编辑盒 - 基类"""

    def __init__(self):
        self.dialog = QtWidgets.QDialog()
        window = Ui_FinanceBox()
        window.setupUi(self.dialog)

        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialog.setWindowIcon(icon)

        self.finance = Finance()
        self.financeTable = window.financeTable
        self.financetableList = []  # Finance
        self.financetableIndex = {}  # Finance -> Item
        self.financeTable.itemSelectionChanged.connect(self.onSelectFinance)
        self.financeTable.activated.connect(self.financeonEdit)

        self.total = Total()
        self.totalTable = window.totalTable
        self.totaltableList = []  # caltable
        self.totaltableIndex = {}  # caltable -> Item

        self.jiesuan1Label = window.jiesuan1Label
        self.shoukuan1Label = window.shoukuan1Label
        self.weifu1Label = window.weifu1Label

        self.jiesuan2Label = window.jiesuan2Label
        self.shoukuan2Label = window.shoukuan2Label
        self.weifu2Label = window.weifu2Label

        self.calcuTable = window.calcuTable
        self.caltableList = []  # caltable
        self.caltableIndex = {}  # caltable -> Item

        self.financetableShow(public.financeManager.financelist())
        self.caltableShow(public.calculatorManager.calculatorlist())

        self.searchEdit = window.searchEdit
        self.pageComboBox = window.pageComboBox
        self.searchBox = window.searchBox
        self.searchBox_2 = window.searchBox_2
        self.searchEdit.textChanged['QString'].connect(self.onQuickSearch)

        # 2020.1.21
        self.financeprintButton = window.financeprintButton
        self.actionFinancePrint = window.actionFinancePrint
        self.financeprintButton.clicked.connect(self.financePrint)
        self.actionFinancePrint.triggered.connect(self.financePrint)

        window.searchBox.currentTextChanged['QString'].connect(self.onSearchBy)
        window.searchBox_2.currentTextChanged['QString'].connect(self.onSearchDate)
        window.pageComboBox.currentTextChanged['QString'].connect(self.onQuickSearch)

        self.searchDate_1 = window.searchDate_1
        self.searchDate_1.dateChanged.connect(self.onstartDateChange)
        self.searchDate_2 = window.searchDate_2
        self.searchDate_2.dateChanged.connect(self.onendDateChange)

        if window.searchBox.currentText() == "客戶":
            self.quickSearchBy = "client"
        else:
            self.quickSearchBy = "notes"

        if self.searchBox_2.currentText() == "結算日期":
            self.quickSearchDate = "date"
        elif self.searchBox_2.currentText() == "收款日期":
            self.quickSearchDate = "date2"
        else:
            self.quickSearchDate = "不限日期"
        self.quickSearchDate = window.searchBox_2.currentText()
        self.pageComboData = self.pageComboBox.currentText()
        self.searchDate_1.setDate(QtCore.QDate.currentDate())
        self.searchDate_2.setDate(QtCore.QDate.currentDate())
        self.caltotal()


    def show(self):
        self.dialog.show()

    def financecopy(self):
        return self.finance.copy()

    def onSearchDate(self, searchDate):
        if self.searchBox_2.currentText() == "結算日期":
            self.quickSearchDate = "date"
        elif self.searchBox_2.currentText() == "收款日期":
            self.quickSearchDate = "date2"
        else:
            self.quickSearchDate = "不限日期"
        self.onQuickSearch()

    def onstartDateChange(self, startdate):
        dayback = self.searchDate_2.date()
        diff_day = startdate.daysTo(dayback)
        if diff_day < 0:
            self.searchDate_2.setDate(startdate)
        self.onQuickSearch()

    def onendDateChange(self, enddate):
        dayup = self.searchDate_1.date()
        diff_day = enddate.daysTo(dayup)
        if diff_day > 0:
            self.searchDate_1.setDate(enddate)
        self.onQuickSearch()

    def onSearchBy(self, searchBy):
        if searchBy == "客戶":
            self.quickSearchBy = "client"
        else:
            self.quickSearchBy = "notes"
        self.onQuickSearch()

    def onQuickSearch(self):
        self.pageComboData = self.pageComboBox.currentText()
        if self.pageComboData == "銷售總賬":
            self.creatTotaltable()
            return
        key = self.searchEdit.text()
        key = ' '.join(key.split())

        result = public.financeManager.search(self.searchDate_1.date(),
                                              self.searchDate_2.date(),
                                              self.quickSearchDate,
                                              self.quickSearchBy, key)
        self.financetableShow(result)

    def financetableShow(self, financeList):
        self.financetableClear()
        for finance in financeList:
            self.financetableAdd(finance)
        self.onSelectFinance()

    def financetableAdd(self, finance):
        item = QtWidgets.QTreeWidgetItem(self.financeTable)
        self.financetableSet(finance, item)
        self.financetableList.append(finance)
        self.financetableIndex[finance] = item

        self.creatTotaltable()
        self.caltotal()

    def financetableSet(self, finance, item=None):
        if item:
            item.setText(0, finance.client)
            item.setText(1, finance.date)
            item.setText(2, finance.unit)
            item.setText(3, finance.jiesuan)
            item.setText(4, finance.notes)
            item.setText(5, finance.shoukuan)
            item.setText(6, finance.date2)
        else:
            self.financetableAdd(finance)

    def financetableClear(self):
        self.financeTable.clear()
        self.financetableList.clear()
        self.financetableIndex.clear()

    def financeonEdit(self):
        finance = self.financeselection
        if not finance:
            return

        def _financeonEdit(_finance):
            if _finance.index != finance.index:
                public.financeManager.delete(finance)
                _finance.copyTo(finance)
                public.financeManager.add(finance)
            else:
                _finance.copyTo(finance)
            if finance in self.financetableIndex:
                self.financetableSet(finance, self.financetableIndex[finance])
        self._fineditBox = fineditUI.FineditBox(finance, _financeonEdit)
        self._fineditBox.show()

    def onSelectFinance(self):
        item = self.financeTable.selectedItems()
        selected = True if item else False
        financeselection = None
        if selected:
            for k, v in self.financetableIndex.items():
                if v == item[0]:
                    financeselection = k
                    break
            else:
                selected = False
        self.financeselection = financeselection

    def creatTotaltable(self):
        self.totaltableClear()
        for finance in self.financetableList:
            status = 0
            for total in self.totaltableList:
                if finance.client == total.client:
                    status = 1
                    if finance.unit == total.unit:
                        total.jiesuan = str(int(total.jiesuan)+int(finance.jiesuan))
                        if finance.shoukuan != '':
                            total.shoukuan = str(int(total.shoukuan)+int(finance.shoukuan))
                        if total.shoukuan == '':
                            total.shoukuan = '0'
                        total.weifu = str(int(total.jiesuan)-int(total.shoukuan))
                        self.totaltableSet(total, self.totaltableIndex[total])
                    else:
                        total = self.total.copy()
                        if self.totaltableList != []:
                            _total = self.totaltableList[-1]
                            total.index = str(int(_total.index) + 1)
                        else:
                            total.index = '1'
                        total.client = finance.client
                        total.unit = finance.unit
                        total.jiesuan = finance.jiesuan
                        if finance.shoukuan == '':
                            total.shoukuan = '0'
                        else:
                            total.shoukuan = finance.shoukuan
                        total.weifu = str(int(total.jiesuan) - int(total.shoukuan))
                        self.totaltableAdd(total)
            if status == 0:
                total = self.total.copy()
                if self.totaltableList != []:
                     _total = self.totaltableList[-1]
                     total.index = str(int(_total.index)+1)
                else:
                    total.index = '1'
                total.client = finance.client
                total.unit = finance.unit
                total.jiesuan = finance.jiesuan
                if finance.shoukuan == '':
                    total.shoukuan = '0'
                else:
                    total.shoukuan = finance.shoukuan
                total.weifu = str(int(total.jiesuan)-int(total.shoukuan))
                self.totaltableAdd(total)

    def caltotal(self):
        total_jiesuan1 = 0
        total_shoukuan1 = 0
        total_weifu1 = 0
        total_jiesuan2 = 0
        total_shoukuan2 = 0
        total_weifu2 = 0
        for finance in self.financetableList:
            if finance.unit == "人民幣":
                total_jiesuan1 += int(finance.jiesuan)
                if finance.shoukuan != '':
                    total_shoukuan1 += int(finance.shoukuan)
            elif finance.unit == "港幣":
                total_jiesuan2 += int(finance.jiesuan)
                if finance.shoukuan != '':
                    total_shoukuan2 += int(finance.shoukuan)
        total_weifu1 = total_jiesuan1 - total_shoukuan1
        total_weifu2 = total_jiesuan2 - total_shoukuan2

        self.jiesuan1Label.setText(str(total_jiesuan1))
        self.shoukuan1Label.setText(str(total_shoukuan1))
        self.weifu1Label.setText(str(total_weifu1))
        self.jiesuan2Label.setText(str(total_jiesuan2))
        self.shoukuan2Label.setText(str(total_shoukuan2))
        self.weifu2Label.setText(str(total_weifu2))

    def totaltableShow(self, totalList):
        self.totaltableClear()
        for total in totalList:
            self.totaltableAdd(total)

    def totaltableAdd(self, total):
        item = QtWidgets.QTreeWidgetItem(self.totalTable)
        self.totaltableSet(total, item)
        self.totaltableList.append(total)
        self.totaltableIndex[total] = item

    def totaltableSet(self, total, item=None):
        if item:
            item.setText(0, total.client)
            item.setText(1, total.unit)
            item.setText(2, total.jiesuan)
            item.setText(3, total.shoukuan)
            item.setText(4, total.weifu)
        else:
            self.totaltableAdd(total)

    def totaltableClear(self):
        self.totalTable.clear()
        self.totaltableList.clear()
        self.totaltableIndex.clear()

    def caltableShow(self, calculatorList):
        self.caltableClear()
        for calculator in calculatorList:
            self.caltableAdd(calculator)
        #self.onSelectcalculator()

    def caltableAdd(self, calculator):
        item = QtWidgets.QTreeWidgetItem(self.calcuTable)
        self.caltableSet(calculator, item)
        self.caltableList.append(calculator)
        self.caltableIndex[calculator] = item

    def caltableSet(self, calculator, item=None):
        if item:
            item.setText(0, calculator.client)
            item.setText(1, calculator.date)
            item.setText(2, calculator.cnumber)
            item.setText(3, calculator.index)
            item.setText(4, calculator.unit)
            item.setText(5, calculator.total)
            item.setText(6, calculator.guihao)
            item.setText(7, calculator.baolaijianshu)
            item.setText(8, calculator.tiguiriqi)
            item.setText(9, calculator.zuguihao)
            item.setText(10, QtCore.QDate.fromString(calculator.zuguiriqi1, "MM/dd/yyyy").toString("MM/dd")+'-'\
                         +QtCore.QDate.fromString(calculator.zuguiriqi2, "MM/dd/yyyy").toString("MM/dd")+'共'\
                         +calculator.zuguidate+'天')
            if calculator.zuguifei == '0':
                item.setText(11, '')
            else:
                item.setText(11, calculator.zuguifei)
            item.setText(12, QtCore.QDate.fromString(calculator.yuanchadianriqi1, "MM/dd/yyyy").toString("MM/dd")+'-'\
                         +QtCore.QDate.fromString(calculator.yuanchadianriqi2, "MM/dd/yyyy").toString("MM/dd")+'共'\
                         +calculator.yuanchadiandate+'天')
            if calculator.yuandaleng == '0':
                item.setText(13, '')
            else:
                item.setText(13, calculator.yuandaleng)

            item.setText(14, QtCore.QDate.fromString(calculator.zuchadianriqi1, "MM/dd/yyyy").toString("MM/dd")+'-'\
                         +QtCore.QDate.fromString(calculator.zuchadianriqi2, "MM/dd/yyyy").toString("MM/dd")+'共'\
                         +calculator.zuchadiandate+'天')
            if calculator.zudaleng == '0':
                item.setText(15, '')
            else:
                item.setText(15, calculator.zudaleng)
            if calculator.zhuanguifei == '0':
                item.setText(16, '')
            else:
                item.setText(16, calculator.zhuanguifei)
            if calculator.dabaofei == '0':
                item.setText(17, '')
            else:
                item.setText(17, calculator.dabaofei)
            if calculator.zhafei == '0':
                item.setText(18, '')
            else:
                item.setText(18, calculator.zhafei)
            if calculator.diaofei == '0':
                item.setText(19, '')
            else:
                item.setText(19, calculator.diaofei)
            if calculator.guobangxiguifei == '0':
                item.setText(20, '')
            else:
                item.setText(20, calculator.guobangxiguifei)
            if calculator.chuanyunfei == '0':
                item.setText(21, '')
            else:
                item.setText(21, calculator.chuanyunfei)
            if calculator.tuochefei == '0':
                item.setText(22, '')
            else:
                item.setText(22, calculator.tuochefei)
            if calculator.weixiufei == '0':
                item.setText(23, '')
            else:
                item.setText(23, calculator.weixiufei)
        else:
            self.caltableAdd(calculator)

    def caltableClear(self):
        self.calcuTable.clear()
        self.caltableList.clear()
        self.caltableIndex.clear()

    #2020.1.21
    def financePrint(self):
        name = "导出做貨工作單..."

        path, ok = QFileDialog.getSaveFileName(
            self.dialog, name, "%userprofile%\财务工作單", "Excel表格(*.xls)")
        if not path:
            return
        financeprintList = self.financetableList.copy()
        public.financeManager.exportAsExcel(path, financeprintList)