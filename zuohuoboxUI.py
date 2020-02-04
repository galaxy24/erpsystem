from PyQt5 import QtWidgets, QtCore, QtGui
from _zuohuoBox import Ui_ZuohuoBox

from zuohuo import Zuohuo

class ZuohuoBox(object):
    """做貨單信息编辑盒 - 基类"""

    def __init__(self):

        self.dialog = QtWidgets.QDialog()
        window = Ui_ZuohuoBox()
        window.setupUi(self.dialog)

        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialog.setWindowIcon(icon)

        self.zindexEdit = window.zindexEdit
        self.dateEdit = window.dateEdit
        self.indexEdit = window.indexEdit
        self.clientEdit = window.clientEdit
        self.yuanguihaoEdit = window.yuanguihaoEdit
        self.jianshuEdit = window.jianshuEdit
        self.shishoujianshuEdit = window.shishoujianshuEdit
        self.zhuangguihaoEdit = window.zhuangguihaoEdit
        self.jingzhongEdit = window.jingzhongEdit
        self.maozhongEdit = window.maozhongEdit
        self.huomingEdit = window.huomingEdit
        self.baozhuangEdit = window.baozhuangEdit
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

    #zuohuoTable对应显示動作
    def applyToZuohuo(self, zuohuo):
        zuohuo.zindex = self.zindexEdit.text()
        zuohuo.date = self.dateEdit.date().toString("MM/dd/yyyy")
        zuohuo.index = self.indexEdit.text()
        zuohuo.client = self.clientEdit.text()
        zuohuo.yuanguihao = self.yuanguihaoEdit.text()
        zuohuo.jianshu = self.jianshuEdit.text()
        zuohuo.shishoujianshu = self.shishoujianshuEdit.text()
        zuohuo.jingzhong = self.jingzhongEdit.text()
        zuohuo.maozhong = self.maozhongEdit.text()
        zuohuo.huoming = self.huomingEdit.text()
        zuohuo.zhuangguihao = self.zhuangguihaoEdit.text()
        zuohuo.baozhuang = self.baozhuangEdit.text()
        zuohuo.note = self.noteEdit.toPlainText()

    def onFinished(self):
        return False


class ZuohuoEditBox(ZuohuoBox):
    """编辑做貨單信息 - 继承ZuohuoBox"""

    def __init__(self, zuohuo, callback):
        super(ZuohuoEditBox, self).__init__()
        self.callback = callback
        self.zuohuo = Zuohuo()

        self.setTitle("修改做貨單...")
        self.setMsg("")
        self.setButton("修改")

        self.zindexEdit.setText(zuohuo.zindex)
        self.dateEdit.setDate(QtCore.QDate.fromString(zuohuo.date, "MM/dd/yyyy"))
        self.indexEdit.setText(zuohuo.index)
        self.clientEdit.setText(zuohuo.client)
        self.yuanguihaoEdit.setText(zuohuo.yuanguihao)
        self.jianshuEdit.setText(zuohuo.jianshu)
        self.shishoujianshuEdit.setText(zuohuo.shishoujianshu)
        self.jingzhongEdit.setText(zuohuo.jingzhong)
        self.maozhongEdit.setText(zuohuo.maozhong)
        self.huomingEdit.setText(zuohuo.huoming)
        self.zhuangguihaoEdit.setText(zuohuo.zhuangguihao)
        self.baozhuangEdit.setText(zuohuo.baozhuang)
        self.noteEdit.setPlainText(zuohuo.note)


        self._zuohuo = Zuohuo()

    def onFinished(self):
        self.applyToZuohuo(self._zuohuo)
        check, info = self._zuohuo.checkInfo()
        if check:
            self.callback(self._zuohuo)
        else:
            self.setMsg(info)
        return check


class ZuohuoNewBox(ZuohuoBox):
    """新建做貨單档案 - 继承zuohuoBox"""

    def __init__(self, callback):
        super(ZuohuoNewBox, self).__init__()
        self.callback = callback

        self.setTitle("新建做貨單...")
        self.setMsg("")
        self.setButton("新建")

        self.zuohuo = Zuohuo()

    def onFinished(self):
        #pass
        zuohuo = self.zuohuo
        self.applyToZuohuo(zuohuo)
        check, info = zuohuo.checkInfo(True)
        self.callback(self.zuohuo) if check else self.setMsg(info)
        return check
