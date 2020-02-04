import os
import public
import pickle

from PyQt5 import QtCore

attributeList = [
    ("index", "序號"),
    ("date", "日期"),
    ("client", "客戶"),
    ("unit", "計價貨幣"),
    ("jiesuan", "結算費用"),
    ("notes", "賬單編號"),
    ("shoukuan", "已收款項"),
    ("date2", "收款日期"),
]

class FinanceManager(object):
    """財務管理类, 单例"""

    def __init__(self, path=None):
        # 用于存储所有財務記錄对象
        self.financeList = []
        # 序號 -> 訂單对象
        self.financeIndex = {}

        self.load(path)

        self.emptyFinance = Finance()

    def add(self, finance):
        self.financeList.append(finance)
        self.financeIndex[finance.index] = finance

    def delete(self, finance):
        self.financeIndex.pop(finance.index)
        self.financeList.remove(finance)
        return True


    def search(self, searchstart, searchend, searchdate, searchBy, keyList, searchList=None):
        result = []
        searchList = searchList or self.financeList
        if not keyList and searchdate == '不限日期':
            return searchList.copy()
        elif not keyList and searchdate == 'date':
            for finance in searchList:
                date = QtCore.QDate.fromString(finance.date, "MM/dd/yyyy")
                if date.daysTo(searchstart) > 0 or date.daysTo(searchend) < 0:
                    continue
                result.append(finance)
            return result
        elif not keyList and searchdate == 'date2':
            for finance in searchList:
                date = QtCore.QDate.fromString(finance.date2, "MM/dd/yyyy")
                if date == QtCore.QDate():
                    continue
                if date.daysTo(searchstart) > 0 or date.daysTo(searchend) < 0:
                    continue
                result.append(finance)
            return result
        else:
            keyList = keyList.split()
            if len(keyList) > 1:
                [keyList.pop(i) if not i else None for i in keyList]
            for finance in searchList:
                if (searchdate == 'date'):
                    date = QtCore.QDate.fromString(finance.date, "MM/dd/yyyy")
                elif (searchdate == 'date2'):
                    date = QtCore.QDate.fromString(finance.date2, "MM/dd/yyyy")
                else:
                    date = searchstart
                if date == QtCore.QDate():
                    continue
                if date.daysTo(searchstart) > 0 or date.daysTo(searchend) < 0:
                    continue
                target = getattr(finance, searchBy)
                for key in keyList:
                    if key in target:
                        result.append(finance)
                        break
            return result

    def exportAsExcel(self, path, financeList=None):
        financeList = financeList or self.financeList
        import xlwt
        xls = xlwt.Workbook(encoding='utf-8')
        xlss = xls.add_sheet("財務匯總表")
        attrs = []
        width = [100, 100, 100, 100, 100, 100, 100, 100, 100]
        for header in range(0, len(attributeList)):
            xlss.write(0, header, attributeList[header][1])
            xlss.col(header).width = width[header] * 256 // 9
            attrs.append(attributeList[header][0])
        for row in range(0, len(financeList)):
            finance = financeList[row]
            for column in range(0, len(attrs)):
                value = getattr(finance, attrs[column])
                xlss.write(row + 1, column, value)
        xls.save(path)

    def save(self, path=None):
        path = path or self.path
        f = None
        try:
            f = open(path, 'wb')
            pickle.dump(self.financeList, f)
            pickle.dump(self.financeIndex, f)
            result = True
        except:
            result = False
        finally:
            if f:
                f.close()
            return result

    def load(self, path=None):
        path = path or public.financeDataPath
        self.path = path
        f = None
        try:
            f = open(path, 'rb')
            financeList = pickle.load(f)
            financeIndex = pickle.load(f)
            result = True
        except:
            result = False
            financeList = []
            financeIndex = {}
        finally:
            if f:
                f.close()
            self.financeList = financeList
            self.financeIndex = financeIndex
        return result

    def financelist(self):
        return self.financeList.copy()

class Finance(object):
    """財務类, 用于存储財務信息"""

    def __init__(self, index="", date="", client="", unit="", jiesuan="", notes="",\
                 shoukuan="", date2=""):

        self.index = index
        self.date = date
        self.client = client
        self.unit = unit
        self.jiesuan = jiesuan
        self.notes = notes
        self.shoukuan = shoukuan
        self.date2 = date2

    def copy(self):
        finance = Finance()
        self.copyTo(finance)
        return finance

    def copyTo(self, finance):
        finance.index = self.index
        finance.date = self.date
        finance.client = self.client
        finance.unit = self.unit
        finance.jiesuan = self.jiesuan
        finance.notes = self.notes
        finance.shoukuan = self.shoukuan
        finance.date2 = self.date2

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