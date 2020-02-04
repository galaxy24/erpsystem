from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from functools import partial
from _mainUI import Ui_MainWindow
import boxUI
import calboxUI
import zuohuoboxUI
import public
import tuozhongboxUI
from financeUI import FinanceBox

class MainWindow(object):
    """主窗口封装类"""

    def __init__(self):

        self.dialog = QtWidgets.QMainWindow()
        window = Ui_MainWindow()
        window.setupUi(self.dialog)
        #self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        #self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinMaxButtonsHint)

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialog.setWindowIcon(icon)

        self.clientLabel = window.clientLabel
        self.dateLabel = window.dateLabel
        self.huomingLabel = window.huomingLabel
        self.baolaijianshuLabel = window.baolaijianshuLabel
        self.yuanguihaoLabel = window.yuanguihaoLabel
        self.zhongweiLabel = window.zhongweiLabel
        self.jiweiLabel = window.jiweiLabel
        self.fangxiangriqiLabel = window.fangxiangriqiLabel
        self.zhongweiriqiLabel = window.zhongweiriqiLabel
        self.bangzhongLabel = window.bangzhongLabel
        self.shishoujianshuLabel = window.shishoujianshuLabel
        self.baozhuangLabel = window.baozhuangLabel
        self.jiedanriqiLabel = window.jiedanriqiLabel
        self.jiesuanzhuangtaiLabel = window.jiesuanzhuangtaiLabel
        self.notes1Label = window.notes1Label
        self.notes2Label = window.notes2Label
        self.notes3Label = window.notes3Label
        self.notes4Label = window.notes4Label

        self.newButtton = window.newButton
        self.actionAdd = window.actionAdd
        self.newButtton.clicked.connect(self.onAddStudent)
        self.actionAdd.triggered.connect(self.onAddStudent)

        self.searchEdit = window.searchEdit
        self.searchEdit.textChanged['QString'].connect(self.onQuickSearch)

        self.stackedWidget = window.stackedWidget

        self.editButton = window.editButton
        self.actionEdit = window.actionEdit
        self.editButton.clicked.connect(self.onEdit)
        self.actionEdit.triggered.connect(self.onEdit)

        self.deleteButton = window.deleteButton
        self.actionDelete = window.actionDelete
        self.deleteButton.clicked.connect(self.onDelete)
        self.deleteButton.setShortcut(QtCore.Qt.Key_Delete)
        self.actionDelete.triggered.connect(self.onDelete)

        self.deleteButton_2 = window.deleteButton_2
        self.actionDelete_2 = window.actionDelete_2
        self.deleteButton_2.clicked.connect(self.onDeleteZuohuo)
        #self.actionDelete_2.setShortcut(QtCore.Qt.Key_Z)
        self.actionDelete_2.triggered.connect(self.onDeleteZuohuo)

        self.deleteButton_3 = window.deleteButton_3
        self.actionDelete_3 = window.actionDelete_3
        self.deleteButton_3.clicked.connect(self.onDeleteTuozhong)
        #self.deleteButton_3.setShortcut(QtCore.Qt.Key_T)
        self.actionDelete_3.triggered.connect(self.onDeleteTuozhong)

        self.deleteButton_4 = window.deleteButton_4
        self.actionDelete_4 = window.actionDelete_4
        self.deleteButton_4.clicked.connect(self.calonDelete)
        #self.deleteButton_4.setShortcut(QtCore.Qt.Key_C)
        self.actionDelete_4.triggered.connect(self.calonDelete)
        self.settleButton = window.settleButton
        self.actionSettle = window.actionSettle
        self.actioncalDelete = window.actioncalDelete
        self.settleButton.clicked.connect(self.onSettle)
        self.actionSettle.triggered.connect(self.onSettle)
        self.actioncalDelete.triggered.connect(self.calonDelete)
        self.actioncalDelete.setShortcut(QtCore.Qt.Key_C)

        self.financeUI = FinanceBox()
        self.finButton = window.finButton
        self.actionFin = window.actionFin
        self.finButton.clicked.connect(self.financeUI.show)
        self.actionFin.triggered.connect(self.financeUI.show)

        #做货按钮
        self.zuohuosettleButton = window.zuohuosettleButton
        self.actionzuohuoSettle = window.actionzuohuoSettle
        self.actionzuohuoDelete = window.actionzuohuoDelete
        self.zuohuosettleButton.clicked.connect(self.zuohuoSettle)
        self.actionzuohuoSettle.triggered.connect(self.zuohuoSettle)
        self.actionzuohuoDelete.triggered.connect(self.onDeleteZuohuo)
        self.actionzuohuoDelete.setShortcut(QtCore.Qt.Key_Z)
        #拖重按钮
        self.tuozhongsettleButton = window.tuozhongsettleButton
        self.actiontuozhongSettle = window.actiontuozhongSettle
        self.actiontuozhongDelete = window.actiontuozhongDelete
        self.tuozhongsettleButton.clicked.connect(self.tuozhongSettle)
        self.actiontuozhongSettle.triggered.connect(self.tuozhongSettle)
        self.actiontuozhongDelete.triggered.connect(self.onDeleteTuozhong)
        self.actiontuozhongDelete.setShortcut(QtCore.Qt.Key_T)

        self.printButton = window.printButton
        self.actionPrint = window.actionPrint
        self.printButton.clicked.connect(self.calonPrint)
        self.actionPrint.triggered.connect(self.calonPrint)

        #2020.1.21
        self.zuohuoprintButton = window.zuohuoprintButton
        self.actionZuohuoPrint = window.actionZuohuoPrint
        self.zuohuoprintButton.clicked.connect(self.zuohuoPrint)
        self.actionZuohuoPrint.triggered.connect(self.zuohuoPrint)

        self.tuozhongprintButton = window.tuozhongprintButton
        self.actionTuozhongPrint = window.actionTuozhongPrint
        self.tuozhongprintButton.clicked.connect(self.tuozhongPrint)
        self.actionTuozhongPrint.triggered.connect(self.tuozhongPrint)

        self.studentTable = window.studentTable
        self.tableList = []  # Student
        self.tableIndex = {}  # Student -> Item
        self.studentTable.itemSelectionChanged.connect(self.onSelectStudent)
        self.studentTable.activated.connect(self.onEdit)

        ####lin
        self.calcuTable = window.calcuTable
        self.caltableList = []  # caltable
        self.caltableIndex = {}  # caltable -> Item
        self.calcuTable.itemSelectionChanged.connect(self.onSelectCalculator)
        self.calcuTable.activated.connect(self.calonEdit)

        self.financeTable = self.financeUI.financeTable
        self.financetableList = []  # financetable
        self.financetableIndex = {}  # finance -> Item

        #做货table
        self.zuohuoTable = window.zuohuoTable
        self.zuohuotableList = []  # Student
        self.zuohuotableIndex = {}  # Student -> Item
        self.zuohuoTable.itemSelectionChanged.connect(self.onSelectZuohuo)
        self.zuohuoTable.activated.connect(self.zuohuoonEdit)

        #拖重table
        self.tuozhongTable = window.tuozhongTable
        self.tuozhongtableList = []  # Student
        self.tuozhongtableIndex = {}  # Student -> Item
        self.tuozhongTable.itemSelectionChanged.connect(self.onSelectTuozhong)
        self.tuozhongTable.activated.connect(self.tuozhongonEdit)

        # 视图
        self.viewMenu = window.viewMenu
        from student import attributeList as attrs
        for i in range(0, len(attrs)):
            action = QtWidgets.QAction(attrs[i][1], self.dialog)
            action.setCheckable(True)
            action.setChecked(True)
            self.viewMenu.addAction(action)
            action.triggered.connect(partial(self.onSetView, i))

        self.searchMode = 0  # 0不搜索 1快速搜索 2高级搜索

        window.exportSelected.triggered.connect(partial(self.onExport, True))
        window.exportAll.triggered.connect(partial(self.onExport, False))

        self.dialog.closeEvent = self.onQuit
        window.actionSave.triggered.connect(public.studentManager.save)
        window.actionSaveAs.triggered.connect(self.onSaveAs)

        window.actionExit.triggered.connect(self.dialog.close)
        window.actionUrl.triggered.connect(self.onVisitWeb)
        window.actionAbout.triggered.connect(self.onAbout)

        window.searchBox.currentTextChanged['QString'].connect(self.onSearchBy)
        window.searchBox_2.currentTextChanged['QString'].connect(self.onSearchDate)
        window.dateComboBox.currentTextChanged['QString'].connect(self.onSearchDate_2)
        window.pageComboBox.currentTextChanged['QString'].connect(self.onQuickSearch2)

        self.searchDate_1 = window.searchDate_1
        self.searchDate_1.dateChanged.connect(self.onstartDateChange)
        self.searchDate_2 = window.searchDate_2
        self.searchDate_2.dateChanged.connect(self.onendDateChange)

        self.searchDate_3 = window.searchDate_3
        self.searchDate_3.dateChanged.connect(self.onDateChange)

        self.pageComboBox = window.pageComboBox

        self.quickSearchDate = "不限日期"
        self.quickSearchDate2 = window.dateComboBox.currentText()
        self.onSearchBy("序號")
        self.zuohuotableShow(public.zuohuoManager.zuohuolist())
        self.tuozhongtableShow(public.tuozhongManager.tuozhonglist())

        if public.calculatorManager.calculatorlast() == None:
            self.cnumberindex = '001'
        else:
            self.cnumberindex = \
                str(format((int((getattr(public.calculatorManager.calculatorlast(), "cnumber"))[6:9]) + 1), '0>3d'))

    def onAbout(self):
        import version
        QMessageBox.information(QtWidgets.QDialog(), "關於", '\n'.join([
            "輝騰訂單管理系统 Build %03d" % version.build,
            "Jeremy作品@galaxy24@github\n",
            "本作品仅供輝騰内部使用!"
        ]))

    def onVisitWeb(self):
        import webbrowser
        webbrowser.open("https://github.com/galaxy24/erpsystem")

    def onSaveAs(self):
        path, ok = QFileDialog.getSaveFileName(
            self.dialog, "另存報表", "C:/", "報表文件(*.stu)")
        if not path:
            return
        public.studentManager.save(path)
        public.zuohuoManager.save(path)
        public.tuozhongManager.save(path)
        public.calculatorManager.save(path)
        public.financeManager.save(path)

    def onExport(self, part):
        name = "导出选中報單..." if part else "导出所有報單..."
        path, ok = QFileDialog.getSaveFileName(
            self.dialog, name, "%userprofile%\報單匯總表", "Excel表格(*.xls)")
        if not path:
            return
        studentList = self.tableList.copy() if part else None
        public.studentManager.exportAsExcel(path, studentList)

    def onSetView(self, index, checked):
        self.studentTable.setColumnHidden(index, not checked)

    def onQuit(self, _):
        public.studentManager.save()
        public.zuohuoManager.save()
        public.tuozhongManager.save()
        public.calculatorManager.save()
        public.financeManager.save()

    def onSearchDate(self, searchDate):
        from student import attributeList as attrs
        self.quickSearchDate = searchDate
        for attr, translate in attrs:
            if searchDate == translate:
                self.quickSearchDate = attr
        self.onQuickSearch()

    def onSearchDate_2(self, searchDate2):
        self.quickSearchDate2 = searchDate2
        self.onQuickSearch2()

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

    def onDateChange(self, date):
        day = self.searchDate_3.date()
        self.searchDate_3.setDate(day)
        self.onQuickSearch2()

    def onSearchBy(self, searchBy):
        from student import attributeList as attrs
        self.quickSearchBy = searchBy
        for attr, translate in attrs:
            if searchBy == translate:
                self.quickSearchBy = attr
        self.onQuickSearch()

    def onQuickSearch(self):
        key = self.searchEdit.text()
        if self.quickSearchBy == '櫃號':
            result = public.studentManager.searchtest(self.searchDate_1.date(),
                                                      self.searchDate_2.date(),
                                                      self.quickSearchDate, key)
        else:
            key = ' '.join(key.split())
            result = public.studentManager.search(self.searchDate_1.date(),
                                                  self.searchDate_2.date(),
                                                  self.quickSearchDate,
                                                  self.quickSearchBy, key)
        self.tableShow(result)

    def onQuickSearch2(self):
        key = self.pageComboBox.currentText()
        if key == '做貨工作單':
            result = public.zuohuoManager.search(self.searchDate_3.date(), self.quickSearchDate2)
            self.zuohuotableShow(result)
        elif key == '拖重工作單':
            result = public.tuozhongManager.search(self.searchDate_3.date(), self.quickSearchDate2)
            self.tuozhongtableShow(result)

    def onSearch(self):
        def _onSaerch(keyList):
            result = public.studentManager.multiSearch(keyList)
            self.tableShow(result)
        self._saerchBox = boxUI.SearchBox(_onSaerch)
        self._saerchBox.show()

    def onAddStudent(self):
        def _onAddStudent(_student):
            student = _student.copy()
            public.studentManager.add(student)
            self.tableSet(student)
        self._newBox = boxUI.NewBox(_onAddStudent)
        self._newBox.indexEdit.setText(str(len(self.tableIndex) + 1))
        self._newBox.show()

    def onSettle(self):
        student = self.selection
        if not student:
            return
        confirm = QMessageBox.warning(QtWidgets.QWidget(),
                                      "結算訂單", "确认結算此報單?",
                                      QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            # to do calculate
            def _onAddCalculator(_calculatort):
                calculator = _calculatort.copy()
                public.calculatorManager.add(calculator)
                self.caltableSet(calculator)
            self._calnewBox = calboxUI.CalNewBox(_onAddCalculator)
            ####lin
            former = 'HT'+QtCore.QDate.currentDate().toString('yy')+QtCore.QDate.currentDate().toString('MM')
            '''QtCore.QDate.fromString(student.date, "MM/dd/yyyy").toString('yy')'''
            if public.calculatorManager.calculatorlast() == None\
                    or former != (getattr(public.calculatorManager.calculatorlast(), "cnumber"))[0:6]:
                self.cnumberindex = '001'

            self._calnewBox.cnumberEdit.setText('HT'+QtCore.QDate.currentDate().toString('yy')
                                                +QtCore.QDate.currentDate().toString('MM')+str(self.cnumberindex))
            self._calnewBox.clientEdit.setText(student.client)
            self._calnewBox.cindexEdit.setText(str(len(self.caltableIndex)+1))
            self._calnewBox.dateEdit.setDate(QtCore.QDate.currentDate())
            self._calnewBox.indexEdit.setText(student.index)
            self._calnewBox.guihaoEdit.setText(student.yuanguihao)
            self._calnewBox.baolaijianshuEdit.setText(student.baolaijianshu)
            self._calnewBox.tiguiriqiEdit.setText(QtCore.QDate.fromString(student.zhongweiriqi, "MM/dd/yyyy").toString("MM/dd"))

            guoguiguihao=[student.guoguiguihao3,
                          student.guoguiguihao2,
                          student.guoguiguihao1]
            for i in range(3):
                if guoguiguihao[i] == '':
                    continue
                else:
                    self._calnewBox.zuguihaoEdit.setText(guoguiguihao[i])
                    break

            #租柜日期=过柜日期4-过柜日期1 or 结单日期-过柜日期1
            if student.guoguiriqi1 != '01/01/2000':
                first_guoguiriqi = student.guoguiriqi1

            if student.guoguiriqi4 != '01/01/2000':
                last_guoguiriqi = student.guoguiriqi4
            elif student.jiedanriqi != '01/01/2000':
                last_guoguiriqi = student.jiedanriqi
            else:
                last_guoguiriqi = '01/01/2000'

            if last_guoguiriqi == '01/01/2000' and first_guoguiriqi != '01/01/2000':
                last_guoguiriqi = QtCore.QDate.currentDate()

            if first_guoguiriqi != '01/01/2000':
                first_guoguiriqi = QtCore.QDate.fromString(first_guoguiriqi, "MM/dd/yyyy")
                last_guoguiriqi = QtCore.QDate.fromString(last_guoguiriqi, "MM/dd/yyyy")
                day_diff = first_guoguiriqi.daysTo(last_guoguiriqi)
                self._calnewBox.zuguiriqi1Edit.setDate(first_guoguiriqi)
                self._calnewBox.zuguiriqi2Edit.setDate(last_guoguiriqi)
                self._calnewBox.zuguidateEdit.setText(str(day_diff))
            else:
                day_diff = int('0')
                self._calnewBox.zuguiriqi1Edit.setDate(QtCore.QDate.currentDate())
                self._calnewBox.zuguiriqi2Edit.setDate(QtCore.QDate.currentDate())
                self._calnewBox.zuguidateEdit.setText(str(day_diff))

            zuguifei = day_diff * (int(self._calnewBox.danjia_1Edit.text()))
            self._calnewBox.zuguifeiEdit.setText(str(zuguifei))

            #原櫃插电日期=（過櫃时间-重尾日期)
            first_daleng = student.zhongweiriqi
            if student.guoguiriqi1 != "01/01/2000":
                last_daleng = student.guoguiriqi1
            else:
                last_daleng = student.guoguiriqi4

            if last_daleng == '01/01/2000':
                last_daleng = QtCore.QDate.currentDate()
            else:
                last_daleng = QtCore.QDate.fromString(last_daleng, "MM/dd/yyyy")
            self._calnewBox.yuanchadianriqi2Edit.setDate(last_daleng)

            first_daleng = QtCore.QDate.fromString(first_daleng, "MM/dd/yyyy")
            self._calnewBox.yuanchadianriqi1Edit.setDate(first_daleng)
            if student.zhongweiriqi != '01/01/2000':
                yuandaleng = first_daleng.daysTo(last_daleng)
            else:
                yuandaleng = int('0')

            self._calnewBox.yuanchadiandateEdit.setText(str(yuandaleng))
            yuandalengfei = yuandaleng * (int(self._calnewBox.danjia_2Edit.text()))
            self._calnewBox.yuandalengEdit.setText(str(yuandalengfei))

            # 租櫃插电日期=（出貨日期-過櫃日期)
            first_zudaleng = last_daleng

            chuhuoriqi = [student.chuhuoriqi5,
                          student.chuhuoriqi4,
                          student.chuhuoriqi3,
                          student.chuhuoriqi2,
                          student.chuhuoriqi1]

            last_zudaleng = QtCore.QDate.currentDate()
            for i in range(5):
                if (chuhuoriqi[i]) == '01/01/2000':
                    continue
                else:
                    last_zudaleng = QtCore.QDate.fromString(chuhuoriqi[i], "MM/dd/yyyy")
                    break

            self._calnewBox.zuchadianriqi1Edit.setDate(first_zudaleng)
            self._calnewBox.zuchadianriqi2Edit.setDate(last_zudaleng)
            zudaleng = first_zudaleng.daysTo(last_zudaleng)

            if zudaleng < 0:
                zudaleng = 0

            self._calnewBox.zuchadiandateEdit.setText(str(zudaleng))
            if zudaleng > int(self._calnewBox.jianmianEdit.text()):
                zudalengfei = (zudaleng-int(self._calnewBox.jianmianEdit.text()))\
                              * (int(self._calnewBox.danjia_2Edit.text()))
            else:
                zudalengfei = zudaleng * (int(self._calnewBox.danjia_2Edit.text()))
            self._calnewBox.zudalengEdit.setText(str(zudalengfei))

            self._calnewBox.zhuanguifeiEdit.setText('0')
            self._calnewBox.dabaofeiEdit.setText('0')
            self._calnewBox.zhafeiEdit.setText('0')
            self._calnewBox.diaofeiEdit.setText('0')
            self._calnewBox.guobangxiguifeiEdit.setText('0')
            self._calnewBox.chuanyunfeiEdit.setText('0')
            self._calnewBox.tuochefeiEdit.setText('0')
            self._calnewBox.weixiufeiEdit.setText('0')

            self._calnewBox.totalEdit.setText(str(zudalengfei+yuandalengfei+zuguifei))

            if student.jiedanriqi != '01/01/2000':
                student.jiesuanzhuangtai = '已結單'
            else:
                student.jiesuanzhuangtai = '月結,未結單'

            self._calnewBox.show()


    def onDelete(self):
        student = self.selection
        if not student:
            return
        confirm = QMessageBox.warning(QtWidgets.QWidget(),
                                      "删除報單", "确认删除此報單?",
                                      QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            item = self.tableIndex[student]
            n = self.studentTable.topLevelItemCount()
            for i in range(0, n):
                if self.studentTable.topLevelItem(i) == item:
                    self.studentTable.takeTopLevelItem(i)
                    self.tableList.remove(student)
                    self.tableIndex.pop(student)
                    break
            public.studentManager.delete(student)

    def onEdit(self):
        self.stackedWidget.setCurrentIndex(0)
        student = self.selection
        if not student:
            return

        def _onEdit(_student):
            if _student.index != student.index:
                public.studentManager.delete(student)
                _student.copyTo(student)
                public.studentManager.add(student)
            else:
                _student.copyTo(student)
            if student in self.tableIndex:
                self.tableSet(student, self.tableIndex[student])
        self._editBox = boxUI.EditBox(student, _onEdit)
        self._editBox.show()

    def setStudentInfo(self, student=None):
        student = student or public.studentManager.emptyStudent
        self.clientLabel.setText(student.client)
        self.dateLabel.setText(student.date)
        self.huomingLabel.setText(student.huoming)
        self.baolaijianshuLabel.setText(student.baolaijianshu)
        self.yuanguihaoLabel.setText(student.yuanguihao)
        self.zhongweiLabel.setText(student.zhongwei)
        self.jiweiLabel.setText(student.jiwei)
        self.fangxiangriqiLabel.setText(student.fangxiangriqi)
        self.zhongweiriqiLabel.setText(student.zhongweiriqi)
        self.bangzhongLabel.setText(student.bangzhong)
        self.shishoujianshuLabel.setText(student.shishoujianshu)
        self.baozhuangLabel.setText(student.baozhuang)
        self.jiedanriqiLabel.setText(student.jiedanriqi)
        self.jiesuanzhuangtaiLabel.setText(student.jiesuanzhuangtai)
        self.notes1Label.setText(student.notes1)
        self.notes2Label.setText(student.notes2)
        self.notes3Label.setText(student.notes3)
        self.notes4Label.setText(student.notes4)

    def show(self):
        self.dialog.show()

    def tableShow(self, studentList):
        self.tableClear()
        for student in studentList:
            self.tableAdd(student)
        self.onSelectStudent()

    def tableAdd(self, student):
        item = QtWidgets.QTreeWidgetItem(self.studentTable)
        self.tableSet(student, item)
        self.tableList.append(student)
        self.tableIndex[student] = item

    def tableSet(self, student, item=None):
        if item:
            item.setText(0, student.index)
            item.setText(1, student.client)
            item.setText(2, str(student.date))
            if str(student.jiedanriqi) == '01/01/2000':
                item.setText(3, '')
            else:
                item.setText(3, str(student.jiedanriqi))
            item.setText(4, student.jiesuanzhuangtai)
            item.setText(5, student.yuanguihao)
            item.setText(6, student.zhongwei)
            item.setText(7, student.jiwei)

            if str(student.fangxiangriqi) == '01/01/2000':
                item.setText(8, '')
            else:
                item.setText(8, str(student.fangxiangriqi))
            if str(student.zhongweiriqi) == '01/01/2000':
                item.setText(9, '')
            else:
                item.setText(9, str(student.zhongweiriqi))
            item.setText(10, student.notes2)
            item.setText(11, student.notes3)
            item.setText(12, student.notes4)
            item.setText(13, student.notes1)
            item.setText(14, student.fuhuo)
            item.setText(15, student.huoming)
            item.setText(16, student.jingzhong)
            item.setText(17, student.maozhong)
            item.setText(18, student.baolaijianshu)
            item.setText(19, student.jianzhong)
            item.setText(20, student.bangzhong)
            item.setText(21, student.shishoujianshu)
            item.setText(22, student.baozhuang)

            if str(student.guoguiriqi1) == '01/01/2000':
                item.setText(23, '')
            else:
                item.setText(23, str(student.guoguiriqi1))
            item.setText(24, student.guoguiguihao1)
            if str(student.guoguiriqi2) == '01/01/2000':
                item.setText(25, '')
            else:
                item.setText(25, str(student.guoguiriqi2))
            item.setText(26, student.guoguiguihao2)
            if str(student.guoguiriqi3) == '01/01/2000':
                item.setText(27, '')
            else:
                item.setText(27, str(student.guoguiriqi3))
            item.setText(28, student.guoguiguihao3)
            if str(student.guoguiriqi4) == '01/01/2000':
                item.setText(29, '')
            else:
                item.setText(29, str(student.guoguiriqi4))
            item.setText(30, student.chukouguihao)

            if str(student.chuhuoriqi1) == '01/01/2000':
                item.setText(31, '')
            else:
                item.setText(31, str(student.chuhuoriqi1))
            item.setText(32, student.chuhuojianshu1)
            item.setText(33, student.chuhuoguihao1)
            if str(student.chuhuoriqi2) == '01/01/2000':
                item.setText(34, '')
            else:
                item.setText(34, str(student.chuhuoriqi2))
            item.setText(35, student.chuhuojianshu2)
            item.setText(36, student.chuhuoguihao2)
            if str(student.chuhuoriqi3) == '01/01/2000':
                item.setText(37, '')
            else:
                item.setText(37, str(student.chuhuoriqi3))
            item.setText(38, student.chuhuojianshu3)
            item.setText(39, student.chuhuoguihao3)
            if str(student.chuhuoriqi4) == '01/01/2000':
                item.setText(40, '')
            else:
                item.setText(40, str(student.chuhuoriqi4))
            item.setText(41, student.chuhuojianshu4)
            item.setText(42, student.chuhuoguihao4)
            if str(student.chuhuoriqi5) == '01/01/2000':
                item.setText(43, '')
            else:
                item.setText(43, str(student.chuhuoriqi5))
            item.setText(44, student.chuhuojianshu5)
            item.setText(45, student.chuhuoguihao5)

        elif self.searchMode == 0:
            self.tableAdd(student)

    def tableClear(self):
        self.studentTable.clear()
        self.tableList.clear()
        self.tableIndex.clear()

    def onSelectStudent(self):
        self.calcuTable.clearSelection()
        item = self.studentTable.selectedItems()
        selected = True if item else False
        selection = None
        if selected:
            for k, v in self.tableIndex.items():
                if v == item[0]:
                    selection = k
                    break
            else:
                selected = False
        self.selection = selection
        self.setStudentInfo(selection)
        self.editButton.setEnabled(selected)
        self.actionEdit.setEnabled(selected)
        self.deleteButton.setEnabled(selected)
        self.actionDelete.setEnabled(selected)
        self.settleButton.setEnabled(selected)
        self.actionSettle.setEnabled(selected)
        self.deleteButton_2.setEnabled(False)
        self.actionDelete_2.setEnabled(False)
        self.deleteButton_3.setEnabled(False)
        self.actionDelete_3.setEnabled(False)
        self.deleteButton_4.setEnabled(False)
        self.actionDelete_4.setEnabled(False)
        self.zuohuosettleButton.setEnabled(selected)
        self.actionzuohuoSettle.setEnabled(selected)
        self.tuozhongsettleButton.setEnabled(selected)
        self.actiontuozhongSettle.setEnabled(selected)

    ###lin
    def caltableShow(self, calculatorList):
        self.caltableClear()
        for calculator in calculatorList:
            self.caltableAdd(calculator)
        #self.onSelectStudent()

    def caltableAdd(self, calculator):
        item = QtWidgets.QTreeWidgetItem(self.calcuTable)
        self.caltableSet(calculator, item)
        self.caltableList.append(calculator)
        self.caltableIndex[calculator] = item

    def caltableSet(self, calculator, item=None):
        if item:
            item.setText(0, calculator.cindex)
            item.setText(1, calculator.guihao)
            item.setText(2, calculator.baolaijianshu)
            item.setText(3, calculator.tiguiriqi)
            item.setText(4, calculator.zuguihao)
            item.setText(5, QtCore.QDate.fromString(calculator.zuguiriqi1, "MM/dd/yyyy").toString("MM/dd")+'-'\
                         +QtCore.QDate.fromString(calculator.zuguiriqi2, "MM/dd/yyyy").toString("MM/dd")+'共'\
                         +calculator.zuguidate+'天')
            if calculator.zuguifei == '0':
                item.setText(6, '')
            else:
                item.setText(6, calculator.zuguifei)
            item.setText(7, QtCore.QDate.fromString(calculator.yuanchadianriqi1, "MM/dd/yyyy").toString("MM/dd")+'-'\
                         +QtCore.QDate.fromString(calculator.yuanchadianriqi2, "MM/dd/yyyy").toString("MM/dd")+'共'\
                         +calculator.yuanchadiandate+'天')
            if calculator.yuandaleng == '0':
                item.setText(8, '')
            else:
                item.setText(8, calculator.yuandaleng)

            item.setText(9, QtCore.QDate.fromString(calculator.zuchadianriqi1, "MM/dd/yyyy").toString("MM/dd")+'-'\
                         +QtCore.QDate.fromString(calculator.zuchadianriqi2, "MM/dd/yyyy").toString("MM/dd")+'共'\
                         +calculator.zuchadiandate+'天')
            if calculator.zudaleng == '0':
                item.setText(10, '')
            else:
                item.setText(10, calculator.zudaleng)
            if calculator.zhuanguifei == '0':
                item.setText(11, '')
            else:
                item.setText(11, calculator.zhuanguifei)
            if calculator.dabaofei == '0':
                item.setText(12, '')
            else:
                item.setText(12, calculator.dabaofei)
            if calculator.zhafei == '0':
                item.setText(13, '')
            else:
                item.setText(13, calculator.zhafei)
            if calculator.diaofei == '0':
                item.setText(14, '')
            else:
                item.setText(14, calculator.diaofei)
            if calculator.guobangxiguifei == '0':
                item.setText(15, '')
            else:
                item.setText(15, calculator.guobangxiguifei)
            if calculator.chuanyunfei == '0':
                item.setText(16, '')
            else:
                item.setText(16, calculator.chuanyunfei)
            if calculator.tuochefei == '0':
                item.setText(17, '')
            else:
                item.setText(17, calculator.tuochefei)
            if calculator.weixiufei == '0':
                item.setText(18, '')
            else:
                item.setText(18, calculator.weixiufei)
            item.setText(19, calculator.unit)
            item.setText(20, calculator.total)

        elif self.searchMode == 0:
            self.caltableAdd(calculator)

    def caltableClear(self):
        self.calcuTable.clear()
        self.caltableList.clear()
        self.caltableIndex.clear()

    def calonPrint(self):
        name = "导出結算表單..."
        calprintList = self.caltableList.copy()
        total = 0
        for calculator in calprintList:
            total += int(calculator.total)
        path, ok = QFileDialog.getSaveFileName(
            self.dialog, name, "%userprofile%\結算單"+calculator.cnumber, "Excel表格(*.xls)")
        if not path:
            return
        if public.calculatorManager.exportAsExcel(path, calprintList) == False:
            return

        self.financeUI.finance.index = str(len(public.financeManager.financeIndex)+1)
        self.financeUI.finance.jiesuan = str(total)
        self.financeUI.finance.date = str(calculator.date)
        self.financeUI.finance.client = calculator.client
        self.financeUI.finance.unit = calculator.unit
        self.financeUI.finance.notes = calculator.cnumber
        self.financeUI.financetableAdd(self.financeUI.finance)
        finance = self.financeUI.financecopy()
        finance.index = self.financeUI.finance.index
        finance.jiesuan = self.financeUI.finance.jiesuan
        finance.date = self.financeUI.finance.date
        finance.client = self.financeUI.finance.client
        finance.unit = self.financeUI.finance.unit
        finance.notes = self.financeUI.finance.notes
        public.financeManager.add(finance)
        public.financeManager.save()

        public.calculatorManager.save()
        public.calculatorManager.load()
        self.cnumberindex = str(format((int(self.cnumberindex)+1),'0>3d'))
        self.caltableClear()
        self.financeUI.caltableShow(public.calculatorManager.calculatorlist())

    def calonDelete(self):
        calcutor = self.calselection
        if not calcutor:
            return
        confirm = QMessageBox.warning(QtWidgets.QWidget(),
                                      "删除結算單", "确认删除此結算單?",
                                      QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            item = self.caltableIndex[calcutor]
            n = self.calcuTable.topLevelItemCount()
            for i in range(0, n):
                if self.calcuTable.topLevelItem(i) == item:
                    self.calcuTable.takeTopLevelItem(i)
                    self.caltableList.remove(calcutor)
                    self.caltableIndex.pop(calcutor)
                    break
            public.calculatorManager.delete(calcutor)

    def calonEdit(self):
        calcutor = self.calselection
        if not calcutor:
            return

        def _calonEdit(_calcutor):
            if _calcutor.cindex != calcutor.cindex:
                public.calculatorManager.delete(calcutor)
                _calcutor.copyTo(calcutor)
                public.calculatorManager.add(calcutor)
            else:
                _calcutor.copyTo(calcutor)
            if calcutor in self.caltableIndex:
                self.caltableSet(calcutor, self.caltableIndex[calcutor])
        self._caleditBox = calboxUI.CalEditBox(calcutor, _calonEdit)
        self._caleditBox.show()

    def onSelectCalculator(self):
        item = self.calcuTable.selectedItems()
        selected = True if item else False
        calselection = None
        if selected:
            for k, v in self.caltableIndex.items():
                if v == item[0]:
                    calselection = k
                    break
            else:
                selected = False
        self.calselection = calselection
        self.editButton.setEnabled(False)
        self.actionEdit.setEnabled(False)
        self.deleteButton.setEnabled(False)
        self.actionDelete.setEnabled(False)
        self.deleteButton_2.setEnabled(False)
        self.actionDelete_2.setEnabled(False)
        self.deleteButton_3.setEnabled(False)
        self.actionDelete_3.setEnabled(False)
        self.deleteButton_4.setEnabled(selected)
        self.actionDelete_4.setEnabled(selected)
        self.zuohuosettleButton.setEnabled(False)
        self.actionzuohuoSettle.setEnabled(False)
        self.tuozhongsettleButton.setEnabled(False)
        self.actiontuozhongSettle.setEnabled(False)
        self.settleButton.setEnabled(False)
        self.actionSettle.setEnabled(False)
        self.printButton.setEnabled(selected)
        self.actionPrint.setEnabled(selected)

    #做货表单2020.01.12
    def zuohuotableShow(self, zuohuoList):
        self.zuohuotableClear()
        for zuohuo in zuohuoList:
            self.zuohuotableAdd(zuohuo)
        #self.onSelectZuohuo()

    def zuohuotableAdd(self, zuohuo):
        item = QtWidgets.QTreeWidgetItem(self.zuohuoTable)
        self.zuohuotableSet(zuohuo, item)
        self.zuohuotableList.append(zuohuo)
        self.zuohuotableIndex[zuohuo] = item

    def zuohuotableSet(self, zuohuo, item=None):
        if item:
            item.setText(0, zuohuo.index)
            item.setText(1, zuohuo.date)
            item.setText(2, zuohuo.yuanguihao)
            item.setText(3, zuohuo.jianshu)
            item.setText(4, zuohuo.jingzhong)
            item.setText(5, zuohuo.maozhong)
            item.setText(6, zuohuo.huoming)
            item.setText(7, zuohuo.shishoujianshu)
            item.setText(8, zuohuo.zhuangguihao)
            item.setText(9, zuohuo.baozhuang)
            item.setText(10, zuohuo.note)
        else:
            self.zuohuotableAdd(zuohuo)

    def zuohuotableClear(self):
        self.zuohuoTable.clear()
        self.zuohuotableList.clear()
        self.zuohuotableIndex.clear()

    def zuohuoSettle(self):
        student = self.selection
        if not student:
            return

        def _onAddZuohuo(_zuohuo):
            zuohuo = _zuohuo.copy()
            public.zuohuoManager.add(zuohuo)
            self.zuohuotableSet(zuohuo)

        self._zuohuonewBox = zuohuoboxUI.ZuohuoNewBox(_onAddZuohuo)
        self._zuohuonewBox.zindexEdit.setText(str(len(self.zuohuotableList) + 1))
        self._zuohuonewBox.dateEdit.setDate(QtCore.QDate.currentDate())
        self._zuohuonewBox.indexEdit.setText(student.index)
        self._zuohuonewBox.clientEdit.setText(student.client)
        self._zuohuonewBox.yuanguihaoEdit.setText(student.yuanguihao)
        self._zuohuonewBox.jianshuEdit.setText(student.baolaijianshu)
        self._zuohuonewBox.jingzhongEdit.setText(student.jingzhong)
        self._zuohuonewBox.maozhongEdit.setText(student.maozhong)
        self._zuohuonewBox.huomingEdit.setText(student.huoming)
        self._zuohuonewBox.shishoujianshuEdit.setText(student.shishoujianshu)
        self._zuohuonewBox.zhuangguihaoEdit.setText(student.guoguiguihao1)
        self._zuohuonewBox.baozhuangEdit.setText(student.baozhuang)
        self._zuohuonewBox.noteEdit.setPlainText(student.notes2)

        ####
        self._zuohuonewBox.show()

    def zuohuoonEdit(self):
        zuohuo = self.zuohuoselection
        if not zuohuo:
            return

        def _zuohuoonEdit(_zuohuo):
            if _zuohuo.index != zuohuo.index:
                public.zuohuoManager.delete(zuohuo)
                _zuohuo.copyTo(zuohuo)
                public.zuohuoManager.add(zuohuo)
            else:
                _zuohuo.copyTo(zuohuo)
            if zuohuo in self.zuohuotableIndex:
                self.zuohuotableSet(zuohuo, self.zuohuotableIndex[zuohuo])
        self._zuohuoeditBox = zuohuoboxUI.ZuohuoEditBox(zuohuo, _zuohuoonEdit)
        self._zuohuoeditBox.show()
    #2020.1.21
    def zuohuoPrint(self):
        name = "导出做貨工作單..."

        path, ok = QFileDialog.getSaveFileName(
            self.dialog, name, "%userprofile%\做貨工作單", "Excel表格(*.xls)")
        if not path:
            return
        zuohuoprintList = self.zuohuotableList.copy()
        public.zuohuoManager.exportAsExcel(path, zuohuoprintList)

    def onDeleteZuohuo(self):
        zuohuo = self.zuohuoselection
        if not zuohuo:
            return
        confirm = QMessageBox.warning(QtWidgets.QWidget(),
                                      "删除做貨單", "确认删除此做貨單?",
                                      QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            item = self.zuohuotableIndex[zuohuo]
            n = self.zuohuoTable.topLevelItemCount()
            for i in range(0, n):
                if self.zuohuoTable.topLevelItem(i) == item:
                    self.zuohuoTable.takeTopLevelItem(i)
                    self.zuohuotableList.remove(zuohuo)
                    self.zuohuotableIndex.pop(zuohuo)
                    break
            public.zuohuoManager.delete(zuohuo)

    def onSelectZuohuo(self):
        item = self.zuohuoTable.selectedItems()
        selected = True if item else False
        zuohuoselection = None
        if selected:
            for k, v in self.zuohuotableIndex.items():
                if v == item[0]:
                    zuohuoselection = k
                    break
            else:
                selected = False
        self.zuohuoselection = zuohuoselection
        self.editButton.setEnabled(False)
        self.actionEdit.setEnabled(False)
        self.deleteButton.setEnabled(False)
        self.actionDelete.setEnabled(False)
        self.deleteButton_2.setEnabled(selected)
        self.actionDelete_2.setEnabled(selected)
        self.deleteButton_3.setEnabled(False)
        self.actionDelete_3.setEnabled(False)
        self.deleteButton_4.setEnabled(False)
        self.actionDelete_4.setEnabled(False)
        self.settleButton.setEnabled(False)
        self.actionSettle.setEnabled(False)
        self.zuohuosettleButton.setEnabled(False)
        self.actionzuohuoSettle.setEnabled(False)
        self.tuozhongsettleButton.setEnabled(False)
        self.actiontuozhongSettle.setEnabled(False)
        self.printButton.setEnabled(False)
        self.actionPrint.setEnabled(False)

    #拖重表单2020.1.12
    def tuozhongtableShow(self, tuozhongList):
        self.tuozhongtableClear()
        for tuozhong in tuozhongList:
            self.tuozhongtableAdd(tuozhong)
        #self.onSelectTuozhong()

    def tuozhongtableAdd(self, tuozhong):
        item = QtWidgets.QTreeWidgetItem(self.tuozhongTable)
        self.tuozhongtableSet(tuozhong, item)
        self.tuozhongtableList.append(tuozhong)
        self.tuozhongtableIndex[tuozhong] = item

    def tuozhongtableSet(self, tuozhong, item=None):
        # tuozhong = self.student or public.studentManager.emptyStudent
        if item:
            item.setText(0, tuozhong.index)
            item.setText(1, tuozhong.date)
            item.setText(2, tuozhong.yuanguihao)
            item.setText(3, tuozhong.zhongwei)
            item.setText(4, tuozhong.jiwei)
            item.setText(5, tuozhong.shishoujianshu)
            item.setText(6, tuozhong.jingzhong)
            item.setText(7, tuozhong.maozhong)
            item.setText(8, tuozhong.huoming)
            item.setText(9, tuozhong.bangzhong)
            item.setText(10, tuozhong.note)
            # print('1111')

        elif self.searchMode == 0:
            self.tuozhongtableAdd(tuozhong)
            # print('222')

    def tuozhongtableClear(self):
        self.tuozhongTable.clear()
        self.tuozhongtableList.clear()
        self.tuozhongtableIndex.clear()

    def tuozhongSettle(self):
        student = self.selection
        if not student:
            return

        def _onAddTuozhong(_tuozhong):
            tuozhong = _tuozhong.copy()
            public.tuozhongManager.add(tuozhong)
            self.tuozhongtableSet(tuozhong)
        self._tuozhongnewBox = tuozhongboxUI.TuozhongNewBox(_onAddTuozhong)
        self._tuozhongnewBox.tindexEdit.setText(str(len(self.tuozhongtableList) + 1))
        self._tuozhongnewBox.dateEdit.setDate(QtCore.QDate.currentDate())
        self._tuozhongnewBox.indexEdit.setText(student.index)
        self._tuozhongnewBox.clientEdit.setText(student.client)
        self._tuozhongnewBox.yuanguihaoEdit.setText(student.yuanguihao)
        self._tuozhongnewBox.zhongweiEdit.setText(student.zhongwei)
        self._tuozhongnewBox.jiweiEdit.setText(student.jiwei)
        self._tuozhongnewBox.shishoujianshuEdit.setText(student.shishoujianshu)
        self._tuozhongnewBox.jingzhongEdit.setText(student.jingzhong)
        self._tuozhongnewBox.maozhongEdit.setText(student.maozhong)
        self._tuozhongnewBox.huomingEdit.setText(student.huoming)
        self._tuozhongnewBox.bangzhongEdit.setText(student.bangzhong)
        self._tuozhongnewBox.noteEdit.setPlainText(student.notes1)

        ####
        self._tuozhongnewBox.show()

    def tuozhongonEdit(self):
        tuozhong = self.tuozhongselection
        if not tuozhong:
            return

        def _tuozhongonEdit(_tuozhong):
            if _tuozhong.index != tuozhong.index:
                public.tuozhongManager.delete(tuozhong)
                _tuozhong.copyTo(tuozhong)
                public.tuozhongManager.add(tuozhong)
            else:
                _tuozhong.copyTo(tuozhong)
            if tuozhong in self.tuozhongtableIndex:
                self.tuozhongtableSet(tuozhong, self.tuozhongtableIndex[tuozhong])
        self._tuozhongeditBox = tuozhongboxUI.TuozhongEditBox(tuozhong, _tuozhongonEdit)
        self._tuozhongeditBox.show()

    #2020.1.21
    def tuozhongPrint(self):
        name = "导出拖重工作單..."

        path, ok = QFileDialog.getSaveFileName(
            self.dialog, name, "%userprofile%\拖重工作單", "Excel表格(*.xls)")
        if not path:
            return
        tuozhongprintList = self.tuozhongtableList.copy()
        public.tuozhongManager.exportAsExcel(path, tuozhongprintList)

    def onDeleteTuozhong(self):
        tuozhong = self.tuozhongselection
        if not tuozhong:
            return
        confirm = QMessageBox.warning(QtWidgets.QWidget(),
                                      "删除拖重單", "确认删除此拖重單?",
                                      QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            item = self.tuozhongtableIndex[tuozhong]
            n = self.tuozhongTable.topLevelItemCount()
            for i in range(0, n):
                if self.tuozhongTable.topLevelItem(i) == item:
                    self.tuozhongTable.takeTopLevelItem(i)
                    self.tuozhongtableList.remove(tuozhong)
                    self.tuozhongtableIndex.pop(tuozhong)
                    break
            public.tuozhongManager.delete(tuozhong)

    def onSelectTuozhong(self):
        item = self.tuozhongTable.selectedItems()
        selected = True if item else False
        tuozhongselection = None
        if selected:
            for k, v in self.tuozhongtableIndex.items():
                if v == item[0]:
                    tuozhongselection = k
                    break
            else:
                selected = False
        self.tuozhongselection = tuozhongselection
        self.editButton.setEnabled(False)
        self.actionEdit.setEnabled(False)
        self.deleteButton.setEnabled(False)
        self.actionDelete.setEnabled(False)
        self.deleteButton_2.setEnabled(False)
        self.actionDelete_2.setEnabled(False)
        self.deleteButton_3.setEnabled(selected)
        self.actionDelete_3.setEnabled(selected)
        self.deleteButton_4.setEnabled(False)
        self.actionDelete_4.setEnabled(False)
        self.settleButton.setEnabled(False)
        self.actionSettle.setEnabled(False)
        self.zuohuosettleButton.setEnabled(False)
        self.actionzuohuoSettle.setEnabled(False)
        self.tuozhongsettleButton.setEnabled(False)
        self.actiontuozhongSettle.setEnabled(False)
        self.printButton.setEnabled(False)
        self.actionPrint.setEnabled(False)
