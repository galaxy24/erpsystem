from PyQt5 import QtWidgets, QtCore, QtGui
from _fineditBox import Ui_FineditBox

from finance import Finance

class FinanceEditBox(object):
    """財務信息编辑盒 - 基类"""

    def __init__(self):

        self.dialog = QtWidgets.QDialog()
        window = Ui_FineditBox()
        window.setupUi(self.dialog)
        print("test2222222222222222")
        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialog.setWindowIcon(icon)
        self.indexEdit = window.indexEdit
        self.dateEdit = window.dateEdit
        self.clientEdit = window.clientEdit
        self.unitEdit = window.unitEdit
        self.jiesuanEdit = window.jiesuanEdit
        self.notesEdit = window.notesEdit
        self.shoukuanEdit = window.shoukuanEdit
        self.date2Edit = window.date2Edit

        self.okButton = window.okButton
        self.cancelButton = window.cancelButton
        self.okButton.clicked.connect(self.onOkButtonClicked)
        self.cancelButton.clicked.connect(self.dialog.close)

    def onOkButtonClicked(self):
        if self.onFinished():
            self.dialog.close()

    def show(self):
        self.dialog.show()

    def setTitle(self, title):
        self.dialog.setWindowTitle(title)

    def setButton(self, ok, cancel=None):
        self.okButton.setText(ok)
        self.cancelButton.setText(cancel) if cancel is not None else None

    def applyToFinance(self, finance):
        finance.index = self.indexEdit.text()
        finance.date = self.dateEdit.date().toString("MM/dd/yyyy")
        finance.client = self.clientEdit.text()
        finance.unit = self.unitEdit.currentText()
        finance.jiesuan = self.jiesuanEdit.text()
        finance.notes = self.notesEdit.text()
        finance.shoukuan = self.shoukuanEdit.text()
        if finance.shoukuan != '':
            finance.date2 = self.date2Edit.date().toString("MM/dd/yyyy")

    def onFinished(self):
        return False


class FineditBox(FinanceEditBox):
    """編輯財務信息 - 继承FinanceBox"""

    def __init__(self, finance, callback):
        super(FineditBox, self).__init__()
        self.callback = callback
        print("test11111")
        self.finance = Finance()
        self.setTitle("增加財務收款信息...")
        self.setButton("增加收款")

        self.indexEdit.setText(finance.index)
        self.dateEdit.setDate(QtCore.QDate.fromString(finance.date, "MM/dd/yyyy"))
        self.clientEdit.setText(finance.client)
        self.unitEdit.setCurrentText(finance.unit)
        self.jiesuanEdit.setText(finance.jiesuan)
        self.notesEdit.setText(finance.notes)
        self.shoukuanEdit.setText(finance.shoukuan)
        if finance.date2 == '':
            self.date2Edit.setDate(QtCore.QDate.currentDate())
        else:
            self.date2Edit.setDate(QtCore.QDate.fromString(finance.date2, "MM/dd/yyyy"))
    
        self._finance = Finance()

    def onFinished(self):
        self.applyToFinance(self._finance)
        check, info = self._finance.checkInfo()
        if check:
            self.callback(self._finance)
        else:
            self.setMsg(info)
        return check