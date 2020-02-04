import os
import public
import pickle

from PyQt5 import QtCore

attributeList = [
    ("tindex", "序號"),
    ("date", "日期"),
    ("index", "訂單序號"),
    ("client", "客戶"),
    ("yuanguihao", "櫃號"),
    ("zhongwei", "重尾"),
    ("jiwei", "吉尾"),
    ("shishoujianshu", "件數"),
    ("jingzhong", "淨重"),
    ("maozhong", "毛重"),
    ("huoming", "貨名"),
    ("bangzhong", "磅單重量"),
    ("note", "備註"),
]

class TuozhongManager(object):
    """訂單管理类, 单例"""

    def __init__(self, path=None):
        # 用于存储所有訂單对象
        self.tuozhongList = []
        # 序號 -> 訂單对象
        self.tuozhongIndex = {}

        self.load(path)

        self.emptyTuozhong = Tuozhong()

    def add(self, tuozhong):
        self.tuozhongList.append(tuozhong)
        self.tuozhongIndex[tuozhong.tindex] = tuozhong

    def delete(self, tuozhong):
        self.tuozhongIndex.pop(tuozhong.tindex)
        self.tuozhongList.remove(tuozhong)
        return True

    def exportAsExcel(self, path, tuozhongList=None):
        tuozhongList = tuozhongList or self.tuozhongList
        import xlwt
        xls = xlwt.Workbook(encoding='utf-8')
        xlss = xls.add_sheet("拖重工作單")
        attrs = []
        width = [100, 100, 100, 100, 100, 100, 100,\
                 100, 100, 100, 100, 100, 100, 100]
        for header in range(0, len(attributeList)):
            xlss.write(0, header, attributeList[header][1])
            xlss.col(header).width = width[header] * 256 // 9
            attrs.append(attributeList[header][0])
        for row in range(0, len(tuozhongList)):
            zuohuo = tuozhongList[row]
            for column in range(0, len(attrs)):
                value = getattr(zuohuo, attrs[column])
                xlss.write(row + 1, column, value)
        xls.save(path)

    def save(self, path=None):
        path = path or self.path
        f = None
        try:
            f = open(path, 'wb')
            pickle.dump(self.tuozhongList, f)
            pickle.dump(self.tuozhongIndex, f)
            result = True
        except:
            result = False
        finally:
            if f:
                f.close()
            return result

    def load(self, path=None):
        path = path or public.tuozhongDataPath
        self.path = path
        f = None
        try:
            f = open(path, 'rb')
            tuozhongList = pickle.load(f)
            tuozhongIndex = pickle.load(f)
            result = True
        except:
            result = False
            tuozhongList = []
            tuozhongIndex = {}
        finally:
            if f:
                f.close()
            self.tuozhongList = tuozhongList
            self.tuozhongIndex = tuozhongIndex
        return result

    def tuozhonglist(self):
        return self.tuozhongList.copy()

    def search(self, selectdate, searchdate):
        result = []
        searchList = self.tuozhongList
        if searchdate == '不限日期':
            return searchList.copy()
        else:
            for tuozhong in searchList:
                date = QtCore.QDate.fromString(tuozhong.date, "MM/dd/yyyy")
                print(date)
                print(searchdate)
                if date.daysTo(selectdate) != 0:
                    continue
                result.append(tuozhong)
            return result

class Tuozhong(object):
    """訂單类, 用于存储訂單基本信息"""

    def __init__(self, tindex="", date="", index="", client="", yuanguihao="", zhongwei="",\
                 jiwei="", shishoujianshu="", jingzhong="", maozhong="", huoming="", bangzhong="", note="",):

        self.tindex = tindex
        self.date = date
        self.index = index
        self.client = client
        self.yuanguihao = yuanguihao
        self.zhongwei = zhongwei
        self.jiwei = jiwei
        self.shishoujianshu = shishoujianshu
        self.jingzhong = jingzhong
        self.maozhong = maozhong
        self.huoming = huoming
        self.bangzhong = bangzhong
        self.note = note

    def copy(self):
        tuozhong = Tuozhong()
        self.copyTo(tuozhong)
        return tuozhong

    def copyTo(self, tuozhong):
        tuozhong.tindex = self.tindex
        tuozhong.date = self.date
        tuozhong.index = self.index
        tuozhong.client = self.client
        tuozhong.yuanguihao = self.yuanguihao
        tuozhong.zhongwei = self.zhongwei
        tuozhong.jiwei = self.jiwei
        tuozhong.shishoujianshu = self.shishoujianshu
        tuozhong.jingzhong = self.jingzhong
        tuozhong.maozhong = self.maozhong
        tuozhong.huoming = self.huoming
        tuozhong.bangzhong = self.bangzhong
        tuozhong.note = self.note


    def checkInfo(self, new=False):
        '''检查自身信息是否完整合法'''
        # 空值检测
        '''for attr, text in attributeList:
            if not getattr(self, attr):
                return (False, "%s不能为空" % text)'''
        # 重复性检测
        if new and self.tindex in public.tuozhongManager.tuozhongIndex:
            return (False, "序號重复")

        return (True, "")