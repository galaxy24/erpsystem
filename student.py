import os
import public
import pickle

from PyQt5 import QtCore

attributeList = [
    ("index", "序號"),
    ("client", "客戶"),
    ("fuhuo", "付貨人"),
    ("date", "收單日期"),
    ("huoming", "貨名"),
    ("jingzhong", "客戶净重"),
    ("maozhong", "客戶毛重"),
    ("baolaijianshu", "報來件數"),
    ("jianzhong", "件重"),
    ("yuanguihao", "原櫃號"),
    ("zhongwei", "重尾"),
    ("jiwei", "吉尾"),
    ("fangxiangriqi", "放箱日期"),
    ("notes1", "拖重備注"),
    ("zhongweiriqi", "拖重日期"),
    ("bangzhong", "磅重"),
    ("notes2", "過櫃備注"),
    ("guoguiriqi1", "過櫃日期1"),
    ("guoguiguihao1", "過櫃櫃號1"),
    ("guoguiriqi2", "過櫃日期2"),
    ("guoguiguihao2", "過櫃櫃號2"),
    ("guoguiriqi3", "過櫃日期3"),
    ("guoguiguihao3", "過櫃櫃號3"),
    ("guoguiriqi4", "過櫃日期4"),
    ("chukouguihao", "出口櫃號"),
    ("shishoujianshu", "實收件數"),
    ("baozhuang", "包裝"),
    ("chuhuoriqi1", "出貨日期1"),
    ("chuhuojianshu1", "出貨件數1"),
    ("chuhuoguihao1", "出貨櫃號1"),
    ("chuhuoriqi2", "出貨日期2"),
    ("chuhuojianshu2", "出貨件數2"),
    ("chuhuoguihao2", "出貨櫃號2"),
    ("chuhuoriqi3", "出貨日期3"),
    ("chuhuojianshu3", "出貨件數3"),
    ("chuhuoguihao3", "出貨櫃號3"),
    ("chuhuoriqi4", "出貨日期4"),
    ("chuhuojianshu4", "出貨件數4"),
    ("chuhuoguihao4", "出貨櫃號4"),
    ("chuhuoriqi5", "出貨日期5"),
    ("chuhuojianshu5", "出貨件數5"),
    ("chuhuoguihao5", "出貨櫃號5"),
    ("jiedanriqi", "結單日期"),
    ("jiesuanzhuangtai", "結算狀態"),
    ("notes3", "出貨備注"),
    ("notes4", "訂單備注"),
]

class StudentManager(object):
    """訂單管理类, 单例"""

    def __init__(self, path=None):
        # 用于存储所有訂單对象
        self.studentList = []
        # 序號 -> 訂單对象
        self.studentIndex = {}

        self.load(path)

        self.emptyStudent = Student()

    def add(self, student):
        self.studentList.append(student)
        self.studentIndex[student.index] = student

    def delete(self, student):
        self.studentIndex.pop(student.index)
        self.studentList.remove(student)
        return True

    def multiSearch(self, keyList):
        result = self.studentList.copy()
        for searchBy, keyText in keyList:
            if keyText:
                result = self.search(searchBy, keyText, result)
        return result

    def search(self, searchstart, searchend, searchdate, searchBy, keyList, searchList=None):
        result = []
        searchList = searchList or self.studentList
        if not keyList and searchdate == '不限日期':
            return searchList.copy()
        elif not keyList and searchdate == 'zhongwei':
            for student in searchList:
                date = QtCore.QDate.fromString(student.zhongwei, "MM/dd/yyyy")
                if date.daysTo(searchstart) > 0 or date.daysTo(searchend) < 0:
                    continue
                result.append(student)
            return result
        elif not keyList and searchdate == 'zhongweiriqi':
            for student in searchList:
                date = QtCore.QDate.fromString(student.zhongweiriqi, "MM/dd/yyyy")
                if date.daysTo(searchstart) > 0 or date.daysTo(searchend) < 0:
                    continue
                result.append(student)
            return result
        elif not keyList and searchdate == 'jiedanriqi':
            for student in searchList:
                date = QtCore.QDate.fromString(student.jiedanriqi, "MM/dd/yyyy")
                if date.daysTo(searchstart) > 0 or date.daysTo(searchend) < 0:
                    continue
                result.append(student)
            return result
        else:
            keyList = keyList.split()
            if len(keyList) > 1:
                [keyList.pop(i) if not i else None for i in keyList]
            for student in searchList:
                if (searchdate == 'zhongwei'):
                    date = QtCore.QDate.fromString(student.zhongwei, "MM/dd/yyyy")
                elif (searchdate == 'zhongweiriqi'):
                    date = QtCore.QDate.fromString(student.zhongweiriqi, "MM/dd/yyyy")
                elif (searchdate == 'jiedanriqi'):
                    date = QtCore.QDate.fromString(student.jiedanriqi, "MM/dd/yyyy")
                else:
                    date = searchstart
                #date = QtCore.QDate.fromString(student.zhongwei, "yyyy-MM-dd")
                if date.daysTo(searchstart) > 0 or date.daysTo(searchend) < 0:
                    continue
                target = getattr(student, searchBy)
                for key in keyList:
                    if key in target:
                        result.append(student)
                        break
            return result

    def searchtest(self, searchstart, searchend, searchdate, key, searchList=None):
        result = []
        searchList = searchList or self.studentList
        searchByList = ["yuanguihao", "guoguiguihao1", "guoguiguihao2", "guoguiguihao3",
                        "chukouguihao", "chuhuoguihao1","chuhuoguihao2", "chuhuoguihao3",
                        "chuhuoguihao4", "chuhuoguihao5"]
        if key == '':
            return searchList.copy()
        if not searchByList:
            return searchList.copy()
        else:
            for searchBy in searchByList:
                for student in searchList:
                    if (searchdate == 'zhongwei'):
                        date = QtCore.QDate.fromString(student.zhongwei, "MM/dd/yyyy")
                    elif (searchdate == 'zhongweiriqi'):
                        date = QtCore.QDate.fromString(student.zhongweiriqi, "MM/dd/yyyy")
                    elif (searchdate == 'jiedanriqi'):
                        date = QtCore.QDate.fromString(student.jiedanriqi, "MM/dd/yyyy")
                    else:
                        date = searchstart
                    if date.daysTo(searchstart) > 0 or date.daysTo(searchend) < 0:
                        continue

                    target = getattr(student, searchBy)
                    if key in target and student not in result:
                        result.append(student)
                        continue
            return result

    def exportAsExcel(self, path, studentList=None):
        studentList = studentList or self.studentList
        import xlwt
        xls = xlwt.Workbook(encoding='utf-8')
        xlss = xls.add_sheet("訂單匯總表")
        attrs = []
        width = [100, 100, 100, 100, 100, 100, 100,\
                 100, 100, 100, 100, 100, 100, 100,\
                 100, 100, 100, 100, 100, 100, 100,\
                 100, 100, 100, 100, 100, 100, 100,\
                 100, 100, 100, 100, 100, 100, 100,\
                 100, 100, 100, 100, 100, 100, 100,\
                 100, 100, 100, 100]
        for header in range(0, len(attributeList)):
            xlss.write(0, header, attributeList[header][1])
            xlss.col(header).width = width[header] * 256 // 9
            attrs.append(attributeList[header][0])
        for row in range(0, len(studentList)):
            student = studentList[row]
            for column in range(0, len(attrs)):
                value = getattr(student, attrs[column])
                xlss.write(row + 1, column, value)
        xls.save(path)

    def save(self, path=None):
        path = path or self.path
        f = None
        try:
            f = open(path, 'wb')
            pickle.dump(self.studentList, f)
            pickle.dump(self.studentIndex, f)
            result = True
        except:
            result = False
        finally:
            if f:
                f.close()
            return result

    def load(self, path=None):
        path = path or public.defaultDataPath
        self.path = path
        f = None
        try:
            f = open(path, 'rb')
            studentList = pickle.load(f)
            studentIndex = pickle.load(f)
            result = True
        except:
            result = False
            studentList = []
            studentIndex = {}
        finally:
            if f:
                f.close()
            self.studentList = studentList
            self.studentIndex = studentIndex
        return result


class Student(object):
    """訂單类, 用于存储訂單基本信息"""

    def __init__(self, index="", client="", fuhuo="", date="", huoming="", jingzhong="", maozhong="",\
                 baolaijianshu="", jianzhong="", yuanguihao="", zhongwei="", jiwei="", fangxiangriqi="", notes1="",\
                 zhongweiriqi="", bangzhong="", notes2="", guoguiriqi1="", guoguiguihao1="", guoguiriqi2="",\
                 guoguiguihao2="", guoguiriqi3="", guoguiguihao3="", guoguiriqi4="", chukouguihao="",\
                 shishoujianshu="", baozhuang="", chuhuoriqi1="", chuhuojianshu1="", chuhuoguihao1="",\
                 chuhuoriqi2="", chuhuojianshu2="", chuhuoguihao2="", chuhuoriqi3="", chuhuojianshu3="",\
                 chuhuoguihao3="", chuhuoriqi4="", chuhuojianshu4="", chuhuoguihao4="", chuhuoriqi5="",\
                 chuhuojianshu5="", chuhuoguihao5="", jiedanriqi="", jiesuanzhuangtai="", notes3="", notes4=""):

        self.index = index
        self.client = client
        self.fuhuo = fuhuo
        self.date = date
        self.huoming = huoming
        self.jingzhong = jingzhong
        self.maozhong = maozhong
        self.baolaijianshu = baolaijianshu
        self.jianzhong = jianzhong
        self.yuanguihao = yuanguihao
        self.zhongwei = zhongwei
        self.jiwei = jiwei
        self.fangxiangriqi = fangxiangriqi
        self.notes1 = notes1
        self.zhongweiriqi = zhongweiriqi
        self.bangzhong = bangzhong
        self.notes2 = notes2
        self.guoguiriqi1 = guoguiriqi1
        self.guoguiguihao1 = guoguiguihao1
        self.guoguiriqi2 = guoguiriqi2
        self.guoguiguihao2 = guoguiguihao2
        self.guoguiriqi3 = guoguiriqi3
        self.guoguiguihao3 = guoguiguihao3
        self.guoguiriqi4 = guoguiriqi4
        self.chukouguihao = chukouguihao
        self.shishoujianshu = shishoujianshu
        self.baozhuang = baozhuang
        self.chuhuoriqi1 = chuhuoriqi1
        self.chuhuojianshu1 = chuhuojianshu1
        self.chuhuoguihao1 = chuhuoguihao1
        self.chuhuoriqi2 = chuhuoriqi2
        self.chuhuojianshu2 = chuhuojianshu2
        self.chuhuoguihao2 = chuhuoguihao2
        self.chuhuoriqi3 = chuhuoriqi3
        self.chuhuojianshu3 = chuhuojianshu3
        self.chuhuoguihao3 = chuhuoguihao3
        self.chuhuoriqi4 = chuhuoriqi4
        self.chuhuojianshu4 = chuhuojianshu4
        self.chuhuoguihao4 = chuhuoguihao4
        self.chuhuoriqi5 = chuhuoriqi5
        self.chuhuojianshu5 = chuhuojianshu5
        self.chuhuoguihao5 = chuhuoguihao5
        self.jiedanriqi  = jiedanriqi
        self.jiesuanzhuangtai = jiesuanzhuangtai
        self.notes3 = notes3
        self.notes4 = notes4

    def copy(self):
        student = Student()
        self.copyTo(student)
        return student

    def copyTo(self, student):
        student.index = self.index
        student.client = self.client
        student.fuhuo = self.fuhuo
        student.date = self.date
        student.huoming = self.huoming
        student.jingzhong = self.jingzhong
        student.maozhong = self.maozhong
        student.baolaijianshu = self.baolaijianshu
        student.jianzhong = self.jianzhong
        student.yuanguihao = self.yuanguihao
        student.zhongwei = self.zhongwei
        student.jiwei = self.jiwei
        student.fangxiangriqi = self.fangxiangriqi
        student.notes1 = self.notes1
        student.zhongweiriqi = self.zhongweiriqi
        student.bangzhong = self.bangzhong
        student.notes2 = self.notes2
        student.guoguiriqi1 = self.guoguiriqi1
        student.guoguiguihao1 = self.guoguiguihao1
        student.guoguiriqi2 = self.guoguiriqi2
        student.guoguiguihao2 = self.guoguiguihao2
        student.guoguiriqi3 = self.guoguiriqi3
        student.guoguiguihao3 = self.guoguiguihao3
        student.guoguiriqi4 = self.guoguiriqi4
        student.chukouguihao = self.chukouguihao
        student.shishoujianshu = self.shishoujianshu
        student.baozhuang = self.baozhuang
        student.chuhuoriqi1 = self.chuhuoriqi1
        student.chuhuojianshu1 = self.chuhuojianshu1
        student.chuhuoguihao1 = self.chuhuoguihao1
        student.chuhuoriqi2 = self.chuhuoriqi2
        student.chuhuojianshu2 = self.chuhuojianshu2
        student.chuhuoguihao2 = self.chuhuoguihao2
        student.chuhuoriqi3 = self.chuhuoriqi3
        student.chuhuojianshu3 = self.chuhuojianshu3
        student.chuhuoguihao3 = self.chuhuoguihao3
        student.chuhuoriqi4 = self.chuhuoriqi4
        student.chuhuojianshu4 = self.chuhuojianshu4
        student.chuhuoguihao4 = self.chuhuoguihao4
        student.chuhuoriqi5 = self.chuhuoriqi5
        student.chuhuojianshu5 = self.chuhuojianshu5
        student.chuhuoguihao5 = self.chuhuoguihao5
        student.jiedanriqi = self.jiedanriqi
        student.jiesuanzhuangtai = self.jiesuanzhuangtai
        student.notes3 = self.notes3
        student.notes4 = self.notes4

    def checkInfo(self, new=False):
        '''检查自身信息是否完整合法'''
        # 空值检测
        '''for attr, text in attributeList:
            if not getattr(self, attr):
                return (False, "%s不能为空" % text)'''
        # 重复性检测
        if new and self.index in public.studentManager.studentIndex:
            return (False, "序號重复")

        return (True, "")