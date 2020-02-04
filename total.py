import os
import public
import pickle

from PyQt5 import QtCore

attributeList = [
    ("index", "序號"),
    ("client", "客戶"),
    ("unit", "計價貨幣"),
    ("jiesuan", "需結算費用"),
    ("shoukuan", "已收款項"),
    ("weifu", "未付款項"),
]

class TotalManager(object):
    """財務管理类, 单例"""

    def __init__(self, path=None):
        # 用于存储所有財務記錄对象
        self.totalList = []
        # 序號 -> 訂單对象
        self.totalIndex = {}

        self.load(path)

        self.emptyTotal = Total()

    def add(self, total):
        self.totalList.append(total)
        self.totalIndex[total.client] = total

    def delete(self, total):
        self.totalIndex.pop(total.client)
        self.totalList.remove(total)
        return True

    def exportAsExcel(self, path, totalList=None):
        totalList = totalList or self.totalList
        import xlwt
        xls = xlwt.Workbook(encoding='utf-8')
        xlss = xls.add_sheet("財務匯總表")
        attrs = []
        width = [100, 100, 100, 100, 100, 100]
        for header in range(0, len(attributeList)):
            xlss.write(0, header, attributeList[header][1])
            xlss.col(header).width = width[header] * 256 // 9
            attrs.append(attributeList[header][0])
        for row in range(0, len(totalList)):
            total = totalList[row]
            for column in range(0, len(attrs)):
                value = getattr(total, attrs[column])
                xlss.write(row + 1, column, value)
        xls.save(path)

    def save(self, path=None):
        path = path or self.path
        f = None
        try:
            f = open(path, 'wb')
            pickle.dump(self.totalList, f)
            pickle.dump(self.totalIndex, f)
            result = True
        except:
            result = False
        finally:
            if f:
                f.close()
            return result

    def load(self, path=None):
        path = path or public.totalDataPath
        self.path = path
        f = None
        try:
            f = open(path, 'rb')
            totalList = pickle.load(f)
            totalIndex = pickle.load(f)
            result = True
        except:
            result = False
            totalList = []
            totalIndex = {}
        finally:
            if f:
                f.close()
            self.totalList = totalList
            self.totalIndex = totalIndex
        return result

    def totallist(self):
        return self.totalList.copy()

class Total(object):
    """財務类, 用于存储財務信息"""

    def __init__(self, index="", client="", unit="",\
                jiesuan="", shoukuan="", weifu=""):

        self.index = index
        self.client = client
        self.unit = unit
        self.jiesuan = jiesuan
        self.shoukuan = shoukuan
        self.weifu = weifu

    def copy(self):
        total = Total()
        self.copyTo(total)
        return total

    def copyTo(self, total):
        total.index = self.index
        total.client = self.client
        total.unit = self.unit
        total.jiesuan = self.jiesuan
        total.shoukuan = self.shoukuan
        total.weifu = self.weifu

    def checkInfo(self, new=False):
        '''检查自身信息是否完整合法'''
        # 空值检测
        '''for attr, text in attributeList:
            if not getattr(self, attr):
                return (False, "%s不能为空" % text)'''
        # 重复性检测
        # if new and self.cindex in public.calculatorManager.calculatorIndex:
        #     return (False, "序號重复")
        return (True, "")