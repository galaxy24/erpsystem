from PyQt5 import QtWidgets, QtCore, QtGui
from _studentBox import Ui_StudentBox

from student import Student

class StudentBox(object):
    """報單信息编辑盒 - 基类"""

    def __init__(self):

        self.dialog = QtWidgets.QDialog()
        window = Ui_StudentBox()
        window.setupUi(self.dialog)

        self.dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialog.setWindowIcon(icon)

        self.indexEdit = window.indexEdit
        self.clientEdit = window.clientEdit
        self.fuhuoEdit = window.fuhuoEdit
        self.dateEdit = window.dateEdit
        self.huomingEdit = window.huomingEdit
        self.jingzhongEdit = window.jingzhongEdit
        self.maozhongEdit = window.maozhongEdit
        self.baolaijianshuEdit = window.baolaijianshuEdit
        self.jianzhongEdit = window.jianzhongEdit
        self.yuanguihaoEdit = window.yuanguihaoEdit
        self.zhongweiEdit = window.zhongweiEdit
        self.jiweiEdit = window.jiweiEdit
        self.fangxiangriqiEdit = window.fangxiangriqiEdit
        self.notes1Edit = window.notes1Edit
        self.zhongweiriqiEdit = window.zhongweiriqiEdit
        self.bangzhongEdit = window.bangzhongEdit
        self.notes2Edit = window.notes2Edit
        self.guoguiriqi1Edit = window.guoguiriqi1Edit
        self.guoguiguihao1Edit = window.guoguiguihao1Edit
        self.guoguiriqi2Edit = window.guoguiriqi2Edit
        self.guoguiguihao2Edit = window.guoguiguihao2Edit
        self.guoguiriqi3Edit = window.guoguiriqi3Edit
        self.guoguiguihao3Edit = window.guoguiguihao3Edit
        self.guoguiriqi4Edit = window.guoguiriqi4Edit
        self.chukouguihaoEdit = window.chukouguihaoEdit
        self.shishoujianshuEdit = window.shishoujianshuEdit
        self.baozhuangEdit = window.baozhuangEdit
        self.chuhuoriqi1Edit = window.chuhuoriqi1Edit
        self.chuhuojianshu1Edit = window.chuhuojianshu1Edit
        self.chuhuoguihao1Edit = window.chuhuoguihao1Edit
        self.chuhuoriqi2Edit = window.chuhuoriqi2Edit
        self.chuhuojianshu2Edit = window.chuhuojianshu2Edit
        self.chuhuoguihao2Edit = window.chuhuoguihao2Edit
        self.chuhuoriqi3Edit = window.chuhuoriqi3Edit
        self.chuhuojianshu3Edit = window.chuhuojianshu3Edit
        self.chuhuoguihao3Edit = window.chuhuoguihao3Edit
        self.chuhuoriqi4Edit = window.chuhuoriqi4Edit
        self.chuhuojianshu4Edit = window.chuhuojianshu4Edit
        self.chuhuoguihao4Edit = window.chuhuoguihao4Edit
        self.chuhuoriqi5Edit = window.chuhuoriqi5Edit
        self.chuhuojianshu5Edit = window.chuhuojianshu5Edit
        self.chuhuoguihao5Edit = window.chuhuoguihao5Edit
        self.jiedanriqiEdit = window.jiedanriqiEdit
        self.jiesuanzhuangtaiEdit = window.jiesuanzhuangtaiEdit
        self.notes3Edit = window.notes3Edit
        self.notes4Edit = window.notes4Edit

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

    #table对应显示动作
    def applyToStudent(self, student):
        student.index = self.indexEdit.text()
        student.client = self.clientEdit.text()
        student.fuhuo = self.fuhuoEdit.text()
        student.date = self.dateEdit.date().toString("MM/dd/yyyy")
        #student.date = self.dateEdit.text()
        student.huoming = self.huomingEdit.text()
        student.jingzhong = self.jingzhongEdit.text()
        student.maozhong = self.maozhongEdit.text()
        student.baolaijianshu = self.baolaijianshuEdit.text()
        student.jianzhong = self.jianzhongEdit.text()
        student.yuanguihao = self.yuanguihaoEdit.text()
        student.zhongwei = self.zhongweiEdit.date().toString("MM/dd/yyyy")
        student.jiwei = self.jiweiEdit.date().toString("MM/dd/yyyy")
        student.fangxiangriqi = self.fangxiangriqiEdit.date().toString("MM/dd/yyyy")
        student.notes1 = self.notes1Edit.toPlainText()
        student.zhongweiriqi = self.zhongweiriqiEdit.date().toString("MM/dd/yyyy")
        student.bangzhong = self.bangzhongEdit.text()
        student.notes2 = self.notes2Edit.toPlainText()
        student.guoguiriqi1 = self.guoguiriqi1Edit.date().toString("MM/dd/yyyy")
        student.guoguiguihao1 = self.guoguiguihao1Edit.text()
        student.guoguiriqi2 = self.guoguiriqi2Edit.date().toString("MM/dd/yyyy")
        student.guoguiguihao2 = self.guoguiguihao2Edit.text()
        student.guoguiriqi3 = self.guoguiriqi3Edit.date().toString("MM/dd/yyyy")
        student.guoguiguihao3 = self.guoguiguihao3Edit.text()
        student.guoguiriqi4 = self.guoguiriqi4Edit.date().toString("MM/dd/yyyy")
        student.chukouguihao = self.chukouguihaoEdit.text()
        student.shishoujianshu = self.shishoujianshuEdit.text()
        student.baozhuang = self.baozhuangEdit.text()
        student.chuhuoriqi1 = self.chuhuoriqi1Edit.date().toString("MM/dd/yyyy")
        student.chuhuojianshu1 = self.chuhuojianshu1Edit.text()
        student.chuhuoguihao1 = self.chuhuoguihao1Edit.text()
        student.chuhuoriqi2 = self.chuhuoriqi2Edit.date().toString("MM/dd/yyyy")
        student.chuhuojianshu2 = self.chuhuojianshu2Edit.text()
        student.chuhuoguihao2 = self.chuhuoguihao2Edit.text()
        student.chuhuoriqi3 = self.chuhuoriqi3Edit.date().toString("MM/dd/yyyy")
        student.chuhuojianshu3 = self.chuhuojianshu3Edit.text()
        student.chuhuoguihao3 = self.chuhuoguihao3Edit.text()
        student.chuhuoriqi4 = self.chuhuoriqi4Edit.date().toString("MM/dd/yyyy")
        student.chuhuojianshu4 = self.chuhuojianshu4Edit.text()
        student.chuhuoguihao4 = self.chuhuoguihao4Edit.text()
        student.chuhuoriqi5 = self.chuhuoriqi5Edit.date().toString("MM/dd/yyyy")
        student.chuhuojianshu5 = self.chuhuojianshu5Edit.text()
        student.chuhuoguihao5 = self.chuhuoguihao5Edit.text()
        student.jiedanriqi = self.jiedanriqiEdit.date().toString("MM/dd/yyyy")
        student.jiesuanzhuangtai = self.jiesuanzhuangtaiEdit.text()
        student.notes3 = self.notes3Edit.toPlainText()
        student.notes4 = self.notes4Edit.toPlainText()

    def onFinished(self):
        return False


class EditBox(StudentBox):
    """编辑学生信息 - 继承StudentBox"""

    def __init__(self, student, callback):
        super(EditBox, self).__init__()
        self.callback = callback

        self.student = Student()

        self.setTitle("修改信息...")
        self.setMsg("")
        self.setButton("修改")

        self.indexEdit.setText(student.index)
        self.clientEdit.setText(student.client)
        self.fuhuoEdit.setText(student.fuhuo)
        self.dateEdit.setDate(QtCore.QDate.fromString(student.date, "MM/dd/yyyy"))
        self.huomingEdit.setText(student.huoming)
        self.jingzhongEdit.setText(student.jingzhong)
        self.maozhongEdit.setText(student.maozhong)
        self.baolaijianshuEdit.setText(student.baolaijianshu)
        self.jianzhongEdit.setText(student.jianzhong)
        self.yuanguihaoEdit.setText(student.yuanguihao)
        self.zhongweiEdit.setDate(QtCore.QDate.fromString(student.zhongwei, "MM/dd/yyyy"))
        self.jiweiEdit.setDate(QtCore.QDate.fromString(student.jiwei, "MM/dd/yyyy"))
        self.fangxiangriqiEdit.setDate(QtCore.QDate.fromString(student.fangxiangriqi, "MM/dd/yyyy"))
        self.notes1Edit.setPlainText(student.notes1)
        self.zhongweiriqiEdit.setDate(QtCore.QDate.fromString(student.zhongweiriqi, "MM/dd/yyyy"))
        self.bangzhongEdit.setText(student.bangzhong)
        self.notes2Edit.setPlainText(student.notes2)
        self.guoguiriqi1Edit.setDate(QtCore.QDate.fromString(student.guoguiriqi1, "MM/dd/yyyy"))
        self.guoguiguihao1Edit.setText(student.guoguiguihao1)
        self.guoguiriqi2Edit.setDate(QtCore.QDate.fromString(student.guoguiriqi2, "MM/dd/yyyy"))
        self.guoguiguihao2Edit.setText(student.guoguiguihao2)
        self.guoguiriqi3Edit.setDate(QtCore.QDate.fromString(student.guoguiriqi3, "MM/dd/yyyy"))
        self.chukouguihaoEdit.setText(student.chukouguihao)
        self.shishoujianshuEdit.setText(student.shishoujianshu)
        self.baozhuangEdit.setText(student.baozhuang)
        self.chuhuoriqi1Edit.setDate(QtCore.QDate.fromString(student.chuhuoriqi1, "MM/dd/yyyy"))
        self.chuhuojianshu1Edit.setText(student.chuhuojianshu1)
        self.chuhuoguihao1Edit.setText(student.chuhuoguihao1)
        self.chuhuoriqi2Edit.setDate(QtCore.QDate.fromString(student.chuhuoriqi2, "MM/dd/yyyy"))
        self.chuhuojianshu2Edit.setText(student.chuhuojianshu2)
        self.chuhuoguihao2Edit.setText(student.chuhuoguihao2)
        self.chuhuoriqi3Edit.setDate(QtCore.QDate.fromString(student.chuhuoriqi3, "MM/dd/yyyy"))
        self.chuhuojianshu3Edit.setText(student.chuhuojianshu3)
        self.chuhuoguihao3Edit.setText(student.chuhuoguihao3)
        self.chuhuoriqi4Edit.setDate(QtCore.QDate.fromString(student.chuhuoriqi4, "MM/dd/yyyy"))
        self.chuhuojianshu4Edit.setText(student.chuhuojianshu4)
        self.chuhuoguihao4Edit.setText(student.chuhuoguihao4)
        self.chuhuoriqi5Edit.setDate(QtCore.QDate.fromString(student.chuhuoriqi5, "MM/dd/yyyy"))
        self.chuhuojianshu5Edit.setText(student.chuhuojianshu5)
        self.chuhuoguihao5Edit.setText(student.chuhuoguihao5)
        self.jiedanriqiEdit.setDate(QtCore.QDate.fromString(student.jiedanriqi, "MM/dd/yyyy"))
        self.jiesuanzhuangtaiEdit.setText(student.jiesuanzhuangtai)
        self.notes3Edit.setPlainText(student.notes3)
        self.notes4Edit.setPlainText(student.notes4)
        self._student = Student()

    def onFinished(self):
        self.applyToStudent(self._student)
        check, info = self._student.checkInfo()
        if check:
            self.callback(self._student)
        else:
            self.setMsg(info)
        return check


class NewBox(StudentBox):
    """新建報單 - 继承StudentBox"""

    def __init__(self, callback):
        super(NewBox, self).__init__()
        self.callback = callback

        self.setTitle("新建報單...")
        self.setMsg("")
        self.setButton("新建")

        self.student = Student()
        #self.indexEdit.setText(string(int(slef.student.index) + 1))
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.zhongweiEdit.setDate(QtCore.QDate.currentDate())
        self.jiweiEdit.setDate(QtCore.QDate.currentDate())

    def onFinished(self):
        student = self.student
        self.applyToStudent(student)
        check, info = student.checkInfo(True)
        self.callback(self.student) if check else self.setMsg(info)
        return check


class SearchBox(StudentBox):
    """高级搜索框 - 继承StudentBox"""

    def __init__(self, callback):
        super(SearchBox, self).__init__()
        self.callback = callback

        self.setTitle("高级搜索...")
        self.setMsg("请输入检索关键词")
        self.setButton("搜索")

    def onFinished(self):
        keyList = [
            ("index", ' '.join(self.indexEdit.text().split())),
            ("client", ' '.join(self.clientEdit.text().split())),
            ("fuhuo", ' '.join(self.fuhuoEdit.text().split())),
            ("date", ' '.join(self.dateEdit.text().split())),
            ("huoming", ' '.join(self.huomingEdit.text().split())),
            ("jianzhong", ' '.join(self.jianzhongEdit.text().split())),
            ("yuanguihao", ' '.join(self.yuanguihaoEdit.text().split())),
            ("zhongwei", ' '.join(self.zhongweiEdit.text().split())),
            ("jiwei", ' '.join(self.jiweiEdit.text().split())),
            ("zhongweiriqi", ' '.join(self.zhongweiriqiEdit.text().split())),
            ("jiweiriqi", ' '.join(self.jiweiriqiEdit.text().split())),
        ]
        self.callback(keyList)
        return True
