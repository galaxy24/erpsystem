import os
import public
import pickle
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import (QIODevice, QFile, Qt, QMarginsF, QRect)
from PyQt5.QtGui import (QPagedPaintDevice, QPdfWriter, QPainter, QFont)

attributeList = [
    ("zindex", "序號"),
    ("date", "日期"),
    ("index", "訂單序號"),
    ("client", "客戶"),
    ("yuanguihao", "原櫃號"),
    ("jianshu", "件數"),
    ("jingzhong", "淨重"),
    ("maozhong", "毛重"),
    ("huoming", "貨名"),
    ("shishoujianshu", "實收件數"),
    ("zhuangguihao", "轉櫃號"),
    ("baozhuang", "包裝"),
    ("note", "備註"),
]

class ZuohuoManager(object):
    """訂單管理类, 单例"""

    def __init__(self, path=None):
        # 用于存储所有訂單对象
        self.zuohuoList = []
        # 序號 -> 訂單对象
        self.zuohuoIndex = {}

        self.load(path)

        self.emptyZuohuo = Zuohuo()

    def add(self, zuohuo):
        self.zuohuoList.append(zuohuo)
        self.zuohuoIndex[zuohuo.zindex] = zuohuo

    def delete(self, zuohuo):
        self.zuohuoIndex.pop(zuohuo.zindex)
        self.zuohuoList.remove(zuohuo)
        return True

    def exportAsExcel(self, path, zuohuoList=None):
        zuohuoList = zuohuoList or self.zuohuoList
        import xlwt
        xls = xlwt.Workbook(encoding='utf-8')
        xlss = xls.add_sheet("做貨工作單")
        attrs = []
        width = [100, 100, 100, 100, 100, 100, 100,\
                 100, 100, 100, 100, 100, 100, 100]
        for header in range(0, len(attributeList)):
            xlss.write(0, header, attributeList[header][1])
            xlss.col(header).width = width[header] * 256 // 9
            attrs.append(attributeList[header][0])
        for row in range(0, len(zuohuoList)):
            zuohuo = zuohuoList[row]
            for column in range(0, len(attrs)):
                value = getattr(zuohuo, attrs[column])
                xlss.write(row + 1, column, value)
        xls.save(path)

    def save(self, path=None):
        path = path or self.path
        f = None
        try:
            f = open(path, 'wb')
            pickle.dump(self.zuohuoList, f)
            pickle.dump(self.zuohuoIndex, f)
            result = True
        except:
            result = False
        finally:
            if f:
                f.close()
            return result

    def load(self, path=None):
        path = path or public.zuohuoDataPath
        self.path = path
        f = None
        try:
            f = open(path, 'rb')
            zuohuoList = pickle.load(f)
            zuohuoIndex = pickle.load(f)
            result = True
        except:
            result = False
            zuohuoList = []
            zuohuoIndex = {}
        finally:
            if f:
                f.close()
            self.zuohuoList = zuohuoList
            self.zuohuoIndex = zuohuoIndex
        return result

    def zuohuolist(self):
        return self.zuohuoList.copy()

    def search(self, selectdate, searchdate):
        result = []
        searchList = self.zuohuoList
        if searchdate == '不限日期':
            return searchList.copy()
        else:
            for zuohuo in searchList:
                date = QtCore.QDate.fromString(zuohuo.date, "MM/dd/yyyy")
                if date.daysTo(selectdate) != 0:
                    continue
                result.append(zuohuo)
            return result

class Zuohuo(object):
    """做貨單类, 用于存储做貨單基本信息"""

    def __init__(self, zindex="", date="", index="", client="", yuanguihao="", jianshu="", jingzhong="",\
                 maozhong="", huoming="", shishoujianshu="", zhuangguihao="", baozhuang="", note="",):

        self.zindex = zindex
        self.date = date
        self.index = index
        self.client = client
        self.yuanguihao = yuanguihao
        self.jianshu = jianshu
        self.jingzhong = jingzhong
        self.maozhong = maozhong
        self.huoming = huoming
        self.shishoujianshu = shishoujianshu
        self.zhuangguihao = zhuangguihao
        self.baozhuang = baozhuang
        self.note = note

    def copy(self):
        zuohuo = Zuohuo()
        self.copyTo(zuohuo)
        return zuohuo

    def copyTo(self, zuohuo):
        zuohuo.zindex = self.zindex
        zuohuo.date = self.date
        zuohuo.index = self.index
        zuohuo.client = self.client
        zuohuo.yuanguihao = self.yuanguihao
        zuohuo.jianshu = self.jianshu
        zuohuo.jingzhong = self.jingzhong
        zuohuo.maozhong = self.maozhong
        zuohuo.shishoujianshu = self.shishoujianshu
        zuohuo.huoming = self.huoming
        zuohuo.zhuangguihao = self.zhuangguihao
        zuohuo.baozhuang = self.baozhuang
        zuohuo.note = self.note


    def checkInfo(self, new=False):
        '''检查自身信息是否完整合法'''
        # 空值检测
        '''for attr, text in attributeList:
            if not getattr(self, attr):
                return (False, "%s不能为空" % text)'''
        # 重复性检测
        if new and self.zindex in public.zuohuoManager.zuohuoIndex:
            return (False, "序號重复")

        return (True, "")