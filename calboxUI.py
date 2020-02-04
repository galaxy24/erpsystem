from PyQt5 import QtWidgets, QtCore, QtGui
from _calculatorBox import Ui_CalculatorBox

from calculator import Calculator


class CalculatorBox(object):
    """結算信息编辑盒 - 基类"""

    def __init__(self):

        self.dialog = QtWidgets.QDialog()
        window = Ui_CalculatorBox()
        window.setupUi(self.dialog)

        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialog.setWindowIcon(icon)

        self.clientEdit = window.clientEdit
        self.dateEdit = window.dateEdit
        self.cnumberEdit = window.cnumberEdit
        #self.cnumberEdit.textChanged.connect(self.onCnumber)
        self.indexEdit = window.indexEdit
        self.cindexEdit = window.cindexEdit
        self.guihaoEdit = window.guihaoEdit
        self.baolaijianshuEdit = window.baolaijianshuEdit
        self.tiguiriqiEdit = window.tiguiriqiEdit
        self.zuguihaoEdit = window.zuguihaoEdit
        self.zuguiriqi1Edit = window.zuguiriqi1Edit
        self.zuguiriqi2Edit = window.zuguiriqi2Edit
        self.zuguiriqi1Edit.dateChanged.connect(self.onZugui1Edit)
        self.zuguiriqi2Edit.dateChanged.connect(self.onZugui2Edit)
        self.zuguidateEdit = window.zuguidateEdit
        self.danjia_1Edit = window.danjia_1Edit
        self.danjia_1Edit.textChanged.connect(self.onDanjia1)
        self.zuguifeiEdit = window.zuguifeiEdit
        self.zuguifeiEdit.textChanged.connect(self.onCaltotal)
        self.danjia_2Edit = window.danjia_2Edit
        self.danjia_2Edit.textChanged.connect(self.onDanjia2)
        self.jianmianEdit = window.jianmianEdit
        self.jianmianEdit.textChanged.connect(self.onJianmian)
        self.yuanchadianriqi1Edit = window.yuanchadianriqi1Edit
        self.yuanchadianriqi2Edit = window.yuanchadianriqi2Edit
        self.yuanchadianriqi1Edit.dateChanged.connect(self.onYuan1Edit)
        self.yuanchadianriqi2Edit.dateChanged.connect(self.onYuan2Edit)
        self.yuanchadiandateEdit = window.yuanchadiandateEdit
        self.yuandalengEdit = window.yuandalengEdit
        self.yuandalengEdit.textChanged.connect(self.onCaltotal)
        self.zuchadianriqi1Edit = window.zuchadianriqi1Edit
        self.zuchadianriqi2Edit = window.zuchadianriqi2Edit
        self.zuchadianriqi1Edit.dateChanged.connect(self.onZu1Edit)
        self.zuchadianriqi2Edit.dateChanged.connect(self.onZu2Edit)
        self.zuchadiandateEdit = window.zuchadiandateEdit
        self.zudalengEdit = window.zudalengEdit
        self.zudalengEdit.textChanged.connect(self.onCaltotal)
        self.zhuanguifeiEdit = window.zhuanguifeiEdit
        self.zhuanguifeiEdit.textChanged.connect(self.onCaltotal)
        self.dabaofeiEdit = window.dabaofeiEdit
        self.dabaofeiEdit.textChanged.connect(self.onCaltotal)
        self.zhafeiEdit = window.zhafeiEdit
        self.zhafeiEdit.textChanged.connect(self.onCaltotal)
        self.diaofeiEdit = window.diaofeiEdit
        self.diaofeiEdit.textChanged.connect(self.onCaltotal)
        self.guobangxiguifeiEdit = window.guobangxiguifeiEdit
        self.guobangxiguifeiEdit.textChanged.connect(self.onCaltotal)
        self.chuanyunfeiEdit = window.chuanyunfeiEdit
        self.chuanyunfeiEdit.textChanged.connect(self.onCaltotal)
        self.tuochefeiEdit = window.tuochefeiEdit
        self.tuochefeiEdit.textChanged.connect(self.onCaltotal)
        self.weixiufeiEdit = window.weixiufeiEdit
        self.weixiufeiEdit.textChanged.connect(self.onCaltotal)
        self.unitEdit = window.unitEdit
        self.totalEdit = window.totalEdit

        self.msgLabel = window.msg

        self.okButton = window.okButton
        self.cancelButton = window.cancelButton
        self.okButton.clicked.connect(self.onOkButtonClicked)
        self.cancelButton.clicked.connect(self.dialog.close)

    def onCaltotal(self):
        if self.zuguifeiEdit.text() == '':
            self.zuguifeiEdit.setText('0')
        if self.yuandalengEdit.text() == '':
            self.yuandalengEdit.setText('0')
        if self.zudalengEdit.text() == '':
            self.zudalengEdit.setText('0')
        if self.zhuanguifeiEdit.text() == '':
            self.zhuanguifeiEdit.setText('0')
        if self.dabaofeiEdit.text() == '':
            self.dabaofeiEdit.setText('0')
        if self.zhafeiEdit.text() == '':
            self.zhafeiEdit.setText('0')
        if self.diaofeiEdit.text() == '':
            self.diaofeiEdit.setText('0')
        if self.guobangxiguifeiEdit.text() == '':
            self.guobangxiguifeiEdit.setText('0')
        if self.chuanyunfeiEdit.text() == '':
            self.chuanyunfeiEdit.setText('0')
        if self.tuochefeiEdit.text() == '':
            self.tuochefeiEdit.setText('0')
        if self.weixiufeiEdit.text() == '':
            self.weixiufeiEdit.setText('0')

        self.totalEdit.setText(str(
            int(self.zuguifeiEdit.text())\
            +int(self.yuandalengEdit.text())\
            +int(self.zudalengEdit.text())\
            +int(self.zhuanguifeiEdit.text())\
            +int(self.dabaofeiEdit.text())\
            +int(self.zhafeiEdit.text())\
            +int(self.diaofeiEdit.text())\
            +int(self.guobangxiguifeiEdit.text())\
            +int(self.chuanyunfeiEdit.text())\
            +int(self.tuochefeiEdit.text())\
            +int(self.weixiufeiEdit.text())))

    def onZugui1Edit(self, startdate):
        enddate = self.zuguiriqi2Edit.date()
        diff_day = startdate.daysTo(enddate)
        if diff_day < 0:
            self.zuguiriqi2Edit.setDate(startdate)

        enddate = self.zuguiriqi2Edit.date()
        self.zuguidateEdit.setText(str(startdate.daysTo(enddate)))
        self.zuguifeiEdit.setText(str(startdate.daysTo(enddate)*(int(self.danjia_1Edit.text()))))

    def onZugui2Edit(self, enddate):
        startdate = self.zuguiriqi1Edit.date()
        diff_day = startdate.daysTo(enddate)
        if diff_day < 0:
            self.zuguiriqi1Edit.setDate(enddate)

        startdate = self.zuguiriqi1Edit.date()
        self.zuguidateEdit.setText(str(startdate.daysTo(enddate)))
        self.zuguifeiEdit.setText(str(startdate.daysTo(enddate) * (int(self.danjia_1Edit.text()))))

    def onDanjia1(self, danjia):
        if danjia == '':
            danjia = '0'
        self.zuguifeiEdit.setText(str((int(self.zuguidateEdit.text()))*(int(danjia))))

    def onDanjia2(self, danjia):
        if danjia == '':
            danjia = '0'
        self.yuandalengEdit.setText(str((int(self.yuanchadiandateEdit.text()))*(int(danjia))))
        self.zudalengEdit.setText(str(((int(self.zuchadiandateEdit.text()))-(int(self.jianmianEdit.text())))\
                                      *(int(danjia))))

    def onJianmian(self, jianmian):
        if jianmian == '':
            jianmian = '0'
        if ((int(self.zuchadiandateEdit.text()))-(int(jianmian))) <= 0:
            self.jianmianEdit.setText(self.zuchadiandateEdit.text())
            self.zudalengEdit.setText('0')
        else:
            self.zudalengEdit.setText(str(((int(self.zuchadiandateEdit.text()))-(int(jianmian)))\
                                          *(int(self.danjia_2Edit.text()))))

    def onYuan1Edit(self, startdate):
        enddate = self.yuanchadianriqi2Edit.date()
        diff_day = startdate.daysTo(enddate)
        if diff_day < 0:
            self.yuanchadianriqi2Edit.setDate(startdate)

        enddate = self.yuanchadianriqi2Edit.date()
        self.yuanchadiandateEdit.setText(str(startdate.daysTo(enddate)))
        self.yuandalengEdit.setText(str(startdate.daysTo(enddate)*(int(self.danjia_2Edit.text()))))

    def onYuan2Edit(self, enddate):
        startdate = self.yuanchadianriqi1Edit.date()
        diff_day = startdate.daysTo(enddate)
        if diff_day < 0:
            self.yuanchadianriqi1Edit.setDate(enddate)

        startdate = self.yuanchadianriqi1Edit.date()
        self.yuanchadiandateEdit.setText(str(startdate.daysTo(enddate)))
        self.yuandalengEdit.setText(str(startdate.daysTo(enddate) * (int(self.danjia_2Edit.text()))))

    def onZu1Edit(self, startdate):
        enddate = self.zuchadianriqi2Edit.date()
        diff_day = startdate.daysTo(enddate)
        if diff_day < 0:
            self.zuchadianriqi2Edit.setDate(startdate)

        enddate = self.zuchadianriqi2Edit.date()
        self.zuchadiandateEdit.setText(str(startdate.daysTo(enddate)))
        self.zudalengEdit.setText(str((startdate.daysTo(enddate)-(int(self.jianmianEdit.text())))\
                                      *(int(self.danjia_2Edit.text()))))

    def onZu2Edit(self, enddate):
        startdate = self.zuchadianriqi1Edit.date()
        diff_day = startdate.daysTo(enddate)
        if diff_day < 0:
            self.zuchadianriqi1Edit.setDate(enddate)

        startdate = self.zuchadianriqi1Edit.date()
        self.zuchadiandateEdit.setText(str(startdate.daysTo(enddate)))
        self.zudalengEdit.setText(str((startdate.daysTo(enddate)-(int(self.jianmianEdit.text())))\
                                      *(int(self.danjia_2Edit.text()))))

    def onOkButtonClicked(self):
        if self.onFinished():
            self.dialog.close()

    def show(self):
        self.dialog.show()

    def setTitle(self, title):
        self.dialog.setWindowTitle(title)

    def setMsg(self, text):
        self.msgLabel.setText(text)

    def setButton(self, ok, cancel=None):
        self.okButton.setText(ok)
        self.cancelButton.setText(cancel) if cancel is not None else None

    #calcuTable对应显示動作
    def applyToCalculator(self, calculator):
        calculator.client = self.clientEdit.text()
        calculator.date = self.dateEdit.date().toString("MM/dd/yyyy")
        calculator.cnumber = self.cnumberEdit.text()
        calculator.index = self.indexEdit.text()
        calculator.cindex = self.cindexEdit.text()
        calculator.guihao = self.guihaoEdit.text()
        calculator.baolaijianshu = self.baolaijianshuEdit.text()
        calculator.tiguiriqi = self.tiguiriqiEdit.text()
        calculator.zuguihao = self.zuguihaoEdit.text()
        calculator.zuguiriqi1 = self.zuguiriqi1Edit.date().toString("MM/dd/yyyy")
        calculator.zuguiriqi2 = self.zuguiriqi2Edit.date().toString("MM/dd/yyyy")
        calculator.zuguidate = self.zuguidateEdit.text()
        calculator.danjia1 = self.danjia_1Edit.text()
        calculator.zuguifei = self.zuguifeiEdit.text()
        calculator.danjia2 = self.danjia_2Edit.text()
        calculator.jianmian = self.jianmianEdit.text()
        calculator.yuanchadianriqi1 = self.yuanchadianriqi1Edit.date().toString("MM/dd/yyyy")
        calculator.yuanchadianriqi2 = self.yuanchadianriqi2Edit.date().toString("MM/dd/yyyy")
        calculator.yuanchadiandate = self.yuanchadiandateEdit.text()
        calculator.yuandaleng = self.yuandalengEdit.text()
        calculator.zuchadianriqi1 = self.zuchadianriqi1Edit.date().toString("MM/dd/yyyy")
        calculator.zuchadianriqi2 = self.zuchadianriqi2Edit.date().toString("MM/dd/yyyy")
        calculator.zuchadiandate = self.zuchadiandateEdit.text()
        calculator.zudaleng = self.zudalengEdit.text()
        calculator.zhuanguifei = self.zhuanguifeiEdit.text()
        calculator.dabaofei = self.dabaofeiEdit.text()
        calculator.zhafei = self.zhafeiEdit.text()
        calculator.diaofei = self.diaofeiEdit.text()
        calculator.guobangxiguifei = self.guobangxiguifeiEdit.text()
        calculator.chuanyunfei = self.chuanyunfeiEdit.text()
        calculator.tuochefei = self.tuochefeiEdit.text()
        calculator.weixiufei = self.weixiufeiEdit.text()
        calculator.unit = str(self.unitEdit.currentText())
        calculator.total = self.totalEdit.text()

    def onFinished(self):
        return False


class CalEditBox(CalculatorBox):
    """编辑結算信息 - 继承calculatorBox"""

    def __init__(self, calculator, callback):
        super(CalEditBox, self).__init__()
        self.callback = callback

        self.calculator = Calculator()

        self.setTitle("修改結算單...")
        self.setMsg("")
        self.setButton("修改")

        
        self.clientEdit.setText(calculator.client)
        self.dateEdit.setDate(QtCore.QDate.fromString(calculator.date, "MM/dd/yyyy"))
        self.cnumberEdit.setText(calculator.cnumber)
        self.indexEdit.setText(calculator.index)
        self.cindexEdit.setText(calculator.cindex)
        self.guihaoEdit.setText(calculator.guihao)
        self.baolaijianshuEdit.setText(calculator.baolaijianshu)
        self.tiguiriqiEdit.setText(calculator.tiguiriqi)
        self.zuguihaoEdit.setText(calculator.zuguihao)
        self.zuguiriqi1Edit.setDate(QtCore.QDate.fromString(calculator.zuguiriqi1, "MM/dd/yyyy"))
        self.zuguiriqi2Edit.setDate(QtCore.QDate.fromString(calculator.zuguiriqi2, "MM/dd/yyyy"))
        self.zuguidateEdit.setText(calculator.zuguidate)
        self.zuguifeiEdit.setText(calculator.zuguifei)
        self.danjia_1Edit.setText(calculator.danjia1)
        self.danjia_2Edit.setText(calculator.danjia2)
        self.jianmianEdit.setText(calculator.jianmian)
        self.yuanchadianriqi1Edit.setDate(QtCore.QDate.fromString(calculator.yuanchadianriqi1, "MM/dd/yyyy"))
        self.yuanchadianriqi2Edit.setDate(QtCore.QDate.fromString(calculator.yuanchadianriqi2, "MM/dd/yyyy"))
        self.yuanchadiandateEdit.setText(calculator.yuanchadiandate)
        self.yuandalengEdit.setText(calculator.yuandaleng)
        self.zuchadianriqi1Edit.setDate(QtCore.QDate.fromString(calculator.zuchadianriqi1, "MM/dd/yyyy"))
        self.zuchadianriqi2Edit.setDate(QtCore.QDate.fromString(calculator.zuchadianriqi2, "MM/dd/yyyy"))
        self.zuchadiandateEdit.setText(calculator.zuchadiandate)
        self.zudalengEdit.setText(calculator.zudaleng)
        self.zhuanguifeiEdit.setText(calculator.zhuanguifei)
        self.dabaofeiEdit.setText(calculator.dabaofei)
        self.zhafeiEdit.setText(calculator.zhafei)
        self.diaofeiEdit.setText(calculator.diaofei)
        self.guobangxiguifeiEdit.setText(calculator.guobangxiguifei)
        self.chuanyunfeiEdit.setText(calculator.chuanyunfei)
        self.tuochefeiEdit.setText(calculator.tuochefei)
        self.weixiufeiEdit.setText(calculator.weixiufei)
        self.unitEdit.setCurrentText(calculator.unit)
        self.totalEdit.setText(calculator.total)

        self._calculator = Calculator()

    def onFinished(self):
        self.applyToCalculator(self._calculator)
        check, info = self._calculator.checkInfo()
        if check:
            self.callback(self._calculator)
        else:
            self.setMsg(info)
        return check


class CalNewBox(CalculatorBox):
    """新建学生档案 - 继承calculatorBox"""

    def __init__(self, callback):
        super(CalNewBox, self).__init__()
        self.callback = callback

        self.setTitle("新建結算單...")
        self.setMsg("")
        self.setButton("新建")

        self.calculator = Calculator()

    def onFinished(self):
        #pass
        calculator = self.calculator
        self.applyToCalculator(calculator)
        check, info = calculator.checkInfo(True)
        self.callback(self.calculator) if check else self.setMsg(info)
        return check