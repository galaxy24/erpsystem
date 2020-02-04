from PyQt5 import QtWidgets, QtCore, QtGui
from _tuozhongBox import Ui_TuozhongBox

from tuozhong import Tuozhong

class TuozhongBox(object):
    """学生信息编辑盒 - 基类"""

    def __init__(self):

        self.dialog = QtWidgets.QDialog()
        window = Ui_TuozhongBox()
        window.setupUi(self.dialog)

        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialog.setWindowIcon(icon)

        self.tindexEdit = window.tindexEdit
        self.dateEdit = window.dateEdit
        self.indexEdit = window.indexEdit
        self.clientEdit = window.clientEdit
        self.yuanguihaoEdit = window.yuanguihaoEdit
        self.zhongweiEdit = window.zhongweiEdit
        self.jiweiEdit = window.jiweiEdit
        self.shishoujianshuEdit = window.shishoujianshuEdit
        self.jingzhongEdit = window.jingzhongEdit
        self.maozhongEdit = window.maozhongEdit
        self.huomingEdit = window.huomingEdit
        self.bangzhongEdit = window.bangzhongEdit
        self.noteEdit = window.noteEdit


        self.msgLabel = window.msg

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

    def setMsg(self, text):
        self.msgLabel.setText(text)

    def setButton(self, ok, cancel=None):
        self.okButton.setText(ok)
        self.cancelButton.setText(cancel) if cancel is not None else None

    #calcuTable对应显示動作
    def applyToTuozhong(self, tuozhong):
        tuozhong.tindex = self.tindexEdit.text()
        tuozhong.date = self.dateEdit.date().toString("MM/dd/yyyy")
        tuozhong.index = self.indexEdit.text()
        tuozhong.client = self.clientEdit.text()
        tuozhong.yuanguihao = self.yuanguihaoEdit.text()
        tuozhong.zhongwei = self.zhongweiEdit.text()
        tuozhong.jiwei = self.jiweiEdit.text()
        tuozhong.shishoujianshu = self.shishoujianshuEdit.text()
        tuozhong.jingzhong = self.jingzhongEdit.text()
        tuozhong.maozhong = self.maozhongEdit.text()
        tuozhong.huoming = self.huomingEdit.text()
        tuozhong.bangzhong = self.bangzhongEdit.text()
        tuozhong.note = self.noteEdit.toPlainText()



    def onFinished(self):
        return False


class TuozhongEditBox(TuozhongBox):
    """编辑拖重單信息 - 继承tuozhongBox"""

    def __init__(self, tuozhong, callback):
        super(TuozhongEditBox, self).__init__()
        self.callback = callback

        self.tuozhong = Tuozhong()

        self.setTitle("修改拖重單...")
        self.setMsg("")
        self.setButton("修改")

        self.indexEdit.setText(tuozhong.index)
        self.dateEdit.setDate(QtCore.QDate.fromString(tuozhong.date, "MM/dd/yyyy"))
        self.indexEdit.setText(tuozhong.index)
        self.clientEdit.setText(tuozhong.client)
        self.yuanguihaoEdit.setText(tuozhong.yuanguihao)
        self.zhongweiEdit.setText(tuozhong.zhongwei)
        self.jiweiEdit.setText(tuozhong.jiwei)
        self.shishoujianshuEdit.setText(tuozhong.shishoujianshu)
        self.jingzhongEdit.setText(tuozhong.jingzhong)
        self.maozhongEdit.setText(tuozhong.maozhong)
        self.huomingEdit.setText(tuozhong.huoming)
        self.bangzhongEdit.setText(tuozhong.bangzhong)
        self.noteEdit.setPlainText(tuozhong.note)


        self._tuozhong = Tuozhong()

    def onFinished(self):
        self.applyToTuozhong(self._tuozhong)
        check, info = self._tuozhong.checkInfo()
        if check:
            self.callback(self._tuozhong)
        else:
            self.setMsg(info)
        return check


class TuozhongNewBox(TuozhongBox):
    """新建拖重單 - 继承tuozhongBox"""

    def __init__(self, callback):
        super(TuozhongNewBox, self).__init__()
        self.callback = callback

        self.setTitle("新建拖重單...")
        self.setMsg("")
        self.setButton("新建")

        self.tuozhong = Tuozhong()

    def onFinished(self):
        #pass
        tuozhong = self.tuozhong
        self.applyToTuozhong(tuozhong)
        check, info = tuozhong.checkInfo(True)
        self.callback(self.tuozhong) if check else self.setMsg(info)
        return check
