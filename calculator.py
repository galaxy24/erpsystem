import os
import public
import pickle

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox

attributeList = [
    ("client", "客戶"),
    ("date", "日期"),
    ("cnumber", "賬單編號"),
    ("index", "訂單序號"),
    ("cindex", "序號"),
    ("guihao", "櫃號"),
    ("baolaijianshu", "報來件數"),
    ("tiguiriqi", "提櫃日期"),
    ("zuguihao", "租櫃號"),
    ("zuguiriqi1", "租櫃始日期"),
    ("zuguiriqi2", "租櫃末日期"),
    ("zuguidate", "租櫃天數"),
    ("danjia1", "單價1"),
    ("zuguifei", "租櫃費"),
    ("danjia2", "單價2"),
    ("jianmian", "減免(天)"),
    ("yuanchadianriqi1", "原櫃插電始日期"),
    ("yuanchadianriqi2", "原櫃插電末日期"),
    ("yuanchadiandate", "原櫃插電天數"),
    ("yuandaleng", "原櫃打冷"),
    ("zuchadianriqi1", "租櫃插電始日期"),
    ("zuchadianriqi2", "租櫃插電末日期"),
    ("zuchadiandate", "租櫃插電天數"),
    ("zudaleng", "租櫃打冷"),
    ("zhuanguifei", "轉櫃費"),
    ("dabaofei", "打包費"),
    ("zhafei", "閘費"),
    ("diaofei", "吊費"),
    ("guobangxiguifei", "過磅洗櫃費"),
    ("chuanyunfei", "出口船運費"),
    ("tuochefei", "拖車費"),
    ("weixiufei", "維修費"),
    ("unit", "計價單位"), #港幣/人民幣
    ("total", "合計"),
]

class CalculatorManager(object):
    """結算管理类, 单例"""

    def __init__(self, path=None):
        # 用于存储所有訂單对象
        self.calculatorList = []
        # 序號 -> 訂單对象
        self.calculatorIndex = {}

        self.load(path)

        self.emptyCalculator = Calculator()

    def add(self, calculator):
        self.calculatorList.append(calculator)
        self.calculatorIndex[calculator.index] = calculator

    def delete(self, calculator):
        self.calculatorIndex.pop(calculator.index)
        self.calculatorList.remove(calculator)
        return True

    def set_style(self, name, height, bold=False, format_str='', align='center'):
        import xlwt
        style = xlwt.XFStyle()  # 初始化样式

        font = xlwt.Font()  # 为样式创建字体
        font.name = name  # 'Times New Roman'
        font.bold = bold
        font.height = height

        borders = xlwt.Borders()  # 为样式创建边框
        borders.left = 0
        borders.right = 0
        borders.top = 0
        borders.bottom = 0

        alignment = xlwt.Alignment()  # 设置排列
        if align == 'center':
            alignment.horz = xlwt.Alignment.HORZ_CENTER
            alignment.vert = xlwt.Alignment.VERT_CENTER
        elif align == 'left':
            alignment.horz = xlwt.Alignment.HORZ_LEFT
            alignment.vert = xlwt.Alignment.VERT_BOTTOM
        else:
            alignment.horz = xlwt.Alignment.HORZ_RIGHT
            alignment.vert = xlwt.Alignment.VERT_BOTTOM

        style.font = font
        style.borders = borders
        style.num_format_str = format_str
        style.alignment = alignment

        return style

    def exportAsExcel(self, path, calculatorList=None):
        calculatorList = calculatorList or self.calculatorList
        import xlwt
        import datetime
        xls = xlwt.Workbook(encoding='utf-8')
        xlss = xls.add_sheet("結算表單")
        xlss.write_merge(
            0,
            1,
            0,
            4,
            '輝騰物流有限公司',
            self.set_style(
                'Times New Roman',
                380,
                bold=True,
                format_str=''))  # 合并单元格
        xlss.write_merge(
            2,
            3,
            0,
            4,
            'Phaeton Logistics Limited',
            self.set_style(
                'Times New Roman',
                340,
                bold=True,
                format_str=''))  # 合并单元格
        xlss.write_merge(
            4,
            4,
            0,
            4,
            '通訊地址：上水文錦渡52約437地段',
            self.set_style(
                'Times New Roman',
                280,
                bold=True,
                format_str=''))  # 合并单元格
        xlss.write_merge(
            5,
            5,
            0,
            4,
            '電話（852）23059299  傳真（852）23059233',
            self.set_style(
                'Times New Roman',
                240,
                bold=True,
                format_str=''))  # 合并单元格
        xlss.write_merge(
            6,
            6,
            0,
            4,
            '電郵 gaola678@gmail.com',
            self.set_style(
                'Times New Roman',
                240,
                bold=True,
                format_str=''))  # 合并单元格
        xlss.write_merge(
            1,
            3,
            6,
            8,
            '發票',
            self.set_style(
                'Times New Roman',
                400,
                bold=True,
                format_str=''))  # 合并单元格
        styleOK = xlwt.easyxf()
        styleText = xlwt.easyxf()

        pattern = xlwt.Pattern()  # 一个实例化的样式类
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # 固定的样式
        pattern.pattern_fore_colour = xlwt.Style.colour_map['gray40']  # 背景颜色

        borders = xlwt.Borders()  # 为样式创建边框
        borders.left = 2
        borders.right = 2
        borders.top = 6
        borders.bottom = 2

        font = xlwt.Font()  # 为样式创建字体
        font.name = 'Times New Roman'
        font.bold = True
        font.height = 220

        al = xlwt.Alignment()
        al.horz = xlwt.Alignment.HORZ_CENTER    # 设置水平居中
        al.vert = xlwt.Alignment.VERT_CENTER    # 设置垂直居中

        styleOK.pattern = pattern
        styleOK.borders = borders
        styleOK.font = font
        styleOK.alignment = al

        styleText.borders = borders
        styleText.font = font

        xlss.write(8, 0, '客戶：', style=styleText)
        xlss.write_merge(9, 9, 0, 3, '備註：', style=styleText)
        xlss.write(7, 10, '日期：', style=styleText)
        xlss.write(9, 10, '賬單編號：', style=styleText)
        datestyle = xlwt.XFStyle()
        datestyle.num_format_str = 'MM/DD/YYYY'
        xlss.write(7, 11, datetime.datetime.now(), datestyle)
        xlss.write(8, 1, getattr(calculatorList[0], "client"), style=styleText)
        xlss.write(9, 11, getattr(calculatorList[0], "cnumber"), style=styleText)

        attrs = []
        width = [50, 125, 80, 80, 125, 150, 60, 150, 60, 80, 90, 100, 90, 100, 80, 80, 100, 100, 100, 100]
        #for header in range(1, len(attributeList)):
        xlss.write(10, 0, attributeList[4][1], style=styleOK)
        xlss.col(0).width = width[0] * 256 // 9
        attrs.append(attributeList[4][0])

        xlss.write(10, 1, attributeList[5][1], style=styleOK)
        xlss.col(1).width = width[1] * 256 // 9
        attrs.append(attributeList[5][0])

        xlss.write(10, 2, attributeList[6][1], style=styleOK)
        xlss.col(2).width = width[2] * 256 // 9
        attrs.append(attributeList[6][0])

        xlss.write(10, 3, attributeList[7][1], style=styleOK)
        xlss.col(3).width = width[3] * 256 // 9
        attrs.append(attributeList[7][0])

        xlss.write(10, 4, attributeList[8][1], style=styleOK)
        xlss.col(4).width = width[4] * 256 // 9
        attrs.append(attributeList[8][0])

        xlss.write(10, 5, "租櫃日期", style=styleOK)   #attributeList[11][1]
        xlss.col(5).width = width[5] * 256 // 9
        attrs.append(attributeList[11][0])

        xlss.write(10, 6, attributeList[13][1], style=styleOK)
        xlss.col(6).width = width[6] * 256 // 9
        attrs.append(attributeList[13][0])

        xlss.write(10, 7, "插電日期", style=styleOK)  #attributeList[18][1]
        xlss.col(7).width = width[7] * 256 // 9
        attrs.append(attributeList[18][0])

        xlss.write(10, 8, "打冷", style=styleOK)   #attributeList[19][1]
        xlss.col(8).width = width[8] * 256 // 9
        attrs.append(attributeList[19][0])

        xlss.write(10, 9, attributeList[24][1], style=styleOK)
        xlss.col(9).width = width[9] * 256 // 9
        attrs.append(attributeList[24][0])

        xlss.write(10, 10, attributeList[25][1], style=styleOK)
        xlss.col(10).width = width[10] * 256 // 9
        attrs.append(attributeList[25][0])

        xlss.write(10, 11, attributeList[26][1], style=styleOK)
        xlss.col(11).width = width[11] * 256 // 9
        attrs.append(attributeList[26][0])

        xlss.write(10, 12, attributeList[27][1], style=styleOK)
        xlss.col(12).width = width[12] * 256 // 9
        attrs.append(attributeList[27][0])

        xlss.write(10, 13, attributeList[28][1], style=styleOK)
        xlss.col(13).width = width[13] * 256 // 9
        attrs.append(attributeList[28][0])

        xlss.write(10, 14, attributeList[30][1], style=styleOK)
        xlss.col(14).width = width[14] * 256 // 9
        attrs.append(attributeList[30][0])

        xlss.write(10, 15, attributeList[33][1], style=styleOK)
        xlss.col(15).width = width[15] * 256 // 9
        attrs.append(attributeList[33][0])

        i = 0
        total = 0
        for row in range(0, len(calculatorList)):
            calculator = calculatorList[row]
            for column in range(0, 4):
                value = getattr(calculator, attrs[column])
                xlss.write(row + 11 + i, column, value,
                           style=self.set_style('Times New Roman',220,align='center',bold=False,format_str=''))
            value = getattr(calculator, attrs[4])
            xlss.write(row + 11 + i+1, 4, value,
                       style=self.set_style('Times New Roman',220,align='center',bold=False,format_str=''))

            zuguiriqi1 = getattr(calculator, "zuguiriqi1")
            zuguiriqi2 = getattr(calculator, "zuguiriqi2")
            zuguidate = getattr(calculator, "zuguidate")
            value = QtCore.QDate.fromString(zuguiriqi1, "MM/dd/yyyy").toString("MM/dd")+'-'\
                         +QtCore.QDate.fromString(zuguiriqi2, "MM/dd/yyyy").toString("MM/dd")+'共'\
                         +zuguidate+'天'
            if zuguidate != '0':
                xlss.write(row + 11 + i + 1, 5, value,
                           style=self.set_style('Times New Roman', 220, align='center', bold=False, format_str=''))

            value = getattr(calculator, attrs[6])
            if value != '0':
                xlss.write(row + 11 + i + 1, 6, value,
                           style=self.set_style('Times New Roman', 220, align='center', bold=False, format_str=''))

            yuanchariqi1 = getattr(calculator, "yuanchadianriqi1")
            yuanchariqi2 = getattr(calculator, "yuanchadianriqi2")
            yuanchadate = getattr(calculator, "yuanchadiandate")
            value = QtCore.QDate.fromString(yuanchariqi1, "MM/dd/yyyy").toString("MM/dd") + '-' \
                    + QtCore.QDate.fromString(yuanchariqi2, "MM/dd/yyyy").toString("MM/dd") + '共' \
                    + yuanchadate + '天'
            if yuanchadate != '0':
                xlss.write(row + 11 + i, 7, value,
                           style=self.set_style('Times New Roman', 220, align='center', bold=False, format_str=''))

            value = getattr(calculator, "yuandaleng")
            if value != '0':
                xlss.write(row + 11 + i, 8, value,
                           style=self.set_style('Times New Roman', 220, align='center', bold=False, format_str=''))

            zuchariqi1 = getattr(calculator, "zuchadianriqi1")
            zuchariqi2 = getattr(calculator, "zuchadianriqi2")
            zuchadate = getattr(calculator, "zuchadiandate")
            value = QtCore.QDate.fromString(zuchariqi1, "MM/dd/yyyy").toString("MM/dd") + '-' \
                    + QtCore.QDate.fromString(zuchariqi2, "MM/dd/yyyy").toString("MM/dd") + '共' \
                    + zuchadate + '天'
            if zuchadate != '0':
                xlss.write(row + 11 + i+1, 7, value,
                           style=self.set_style('Times New Roman', 220, align='center', bold=False, format_str=''))
            value = getattr(calculator, "zudaleng")
            if value != '0':
                xlss.write(row + 11 + i+1, 8, value,
                           style=self.set_style('Times New Roman', 220, align='center', bold=False, format_str=''))

            for column in range(9, 16):
                value = getattr(calculator, attrs[column])
                if attrs[column] == "total":
                    total += int(value)
                if value != '0':
                    xlss.write(row + 11 + i+1, column, value,
                               style=self.set_style('Times New Roman', 220, align='center', bold=False, format_str=''))

            value = getattr(calculator, "chuanyunfei")
            if value != '0':
                xlss.write(row + 11 + i, 11, "出口船運費",
                           style=self.set_style('Times New Roman', 220, align='center', bold=False, format_str=''))
                xlss.write(row + 11 + i, 12, value,
                           style=self.set_style('Times New Roman', 220, align='center', bold=False, format_str=''))

            value = getattr(calculator, "weixiufei")
            if value != '0':
                xlss.write(row + 11 + i, 13, "維修費",
                           style=self.set_style('Times New Roman', 220, align='center', bold=False, format_str=''))
                xlss.write(row + 11 + i, 14, value,
                           style=self.set_style('Times New Roman', 220, align='center', bold=False, format_str=''))
            i += 1

        xlss.write(row + 11 + i+1, 13, "合計:",
                   style=self.set_style('Times New Roman', 220, align='center', bold=False, format_str=''))
        value = getattr(calculator, "unit")
        xlss.write(row + 11 + i+1, 14, value,
                   style=self.set_style('Times New Roman', 220, align='center', bold=False, format_str=''))
        xlss.write(row + 11 + i+1, 15, str(total),
                   style=self.set_style('Times New Roman', 220, align='center', bold=False, format_str=''))

        try:
            xls.save(path)
            return True
        except Exception as e:
            QMessageBox.critical(QtWidgets.QWidget(), "Error", "結算單保存失敗！", QMessageBox.Ok)
            return False

    def save(self, path=None):
        path = path or self.path
        f = None
        try:
            f = open(path, 'wb')
            pickle.dump(self.calculatorList, f)
            pickle.dump(self.calculatorIndex, f)
            result = True
        except:
            result = False
        finally:
            if f:
                f.close()
            return result

    def load(self, path=None):
        path = path or public.calculatorDataPath
        self.path = path
        f = None
        try:
            f = open(path, 'rb')
            calculatorList = pickle.load(f)
            calculatorIndex = pickle.load(f)
            result = True
        except:
            result = False
            calculatorList = []
            calculatorIndex = {}
        finally:
            if f:
                f.close()
            self.calculatorList = calculatorList
            self.calculatorIndex = calculatorIndex
        return result

    def calculatorlist(self):
        return self.calculatorList.copy()

    def calculatorlast(self):
        if self.calculatorList != []:
            calculator = self.calculatorList[-1]
        else:
            calculator = None
        return calculator

class Calculator(object):
    """結算类, 用于存储訂單結算信息"""

    def __init__(self, client="", date="", cnumber="", index="", cindex="", guihao="", baolaijianshu="",\
                    tiguiriqi="", zuguihao="", zuguiriqi1="", zuguiriqi2="", zuguidate="", danjia1="",  zuguifei="",\
                    danjia2="", jianmian="", yuanchadianriqi1="", yuanchadianriqi2="", yuanchadiandate="", yuandaleng="",\
                    zuchadianriqi1="", zuchadianriqi2="", zuchadiandate="", zudaleng="", zhuanguifei="", dabaofei="",\
                    zhafei="", diaofei="", guobangxiguifei="", chuanyunfei="", tuochefei="", weixiufei="", unit="", total=""):

        self.client = client
        self.date = date
        self.cnumber = cnumber
        self.index = index
        self.cindex = cindex
        self.guihao = guihao
        self.baolaijianshu = baolaijianshu
        self.tiguiriqi = tiguiriqi
        self.zuguihao = zuguihao
        self.zuguiriqi1 = zuguiriqi1
        self.zuguiriqi2 = zuguiriqi2
        self.zuguidate = zuguidate
        self.danjia1 = danjia1
        self.zuguifei = zuguifei
        self.danjia2 = danjia2
        self.jianmian = jianmian
        self.yuanchadianriqi1 = yuanchadianriqi1
        self.yuanchadianriqi2 = yuanchadianriqi2
        self.yuanchadiandate = yuanchadiandate
        self.yuandaleng = yuandaleng
        self.zuchadianriqi1 = zuchadianriqi1
        self.zuchadianriqi2 = zuchadianriqi2
        self.zuchadiandate = zuchadiandate
        self.zudaleng = zudaleng
        self.zhuanguifei = zhuanguifei
        self.dabaofei = dabaofei
        self.zhafei = zhafei
        self.diaofei = diaofei
        self.guobangxiguifei = guobangxiguifei
        self.chuanyunfei = chuanyunfei
        self.tuochefei = tuochefei
        self.weixiufei = weixiufei
        self.unit = unit
        self.total = total

    def copy(self):
        calculator = Calculator()
        self.copyTo(calculator)
        return calculator

    def copyTo(self, calculator):
        calculator.client = self.client
        calculator.date = self.date
        calculator.cnumber = self.cnumber
        calculator.index = self.index
        calculator.cindex = self.cindex
        calculator.guihao = self.guihao
        calculator.baolaijianshu = self.baolaijianshu
        calculator.tiguiriqi = self.tiguiriqi
        calculator.zuguihao = self.zuguihao
        calculator.zuguiriqi1 = self.zuguiriqi1
        calculator.zuguiriqi2 = self.zuguiriqi2
        calculator.zuguidate = self.zuguidate
        calculator.danjia1 = self.danjia1
        calculator.zuguifei = self.zuguifei
        calculator.danjia2 = self.danjia2
        calculator.jianmian = self.jianmian
        calculator.yuanchadianriqi1 = self.yuanchadianriqi1
        calculator.yuanchadianriqi2 = self.yuanchadianriqi2
        calculator.yuanchadiandate = self.yuanchadiandate
        calculator.yuandaleng = self.yuandaleng
        calculator.zuchadianriqi1 = self.zuchadianriqi1
        calculator.zuchadianriqi2 = self.zuchadianriqi2
        calculator.zuchadiandate = self.zuchadiandate
        calculator.zudaleng = self.zudaleng
        calculator.zhuanguifei = self.zhuanguifei
        calculator.dabaofei = self.dabaofei
        calculator.zhafei = self.zhafei
        calculator.diaofei = self.diaofei
        calculator.guobangxiguifei = self.guobangxiguifei
        calculator.chuanyunfei = self.chuanyunfei
        calculator.tuochefei = self.tuochefei
        calculator.weixiufei = self.weixiufei
        calculator.unit = self.unit
        calculator.total = self.total

    def checkInfo(self, new=False):
        '''检查自身信息是否完整合法'''
        # 空值检测
        '''for attr, text in attributeList:
            if not getattr(self, attr):
                return (False, "%s不能为空" % text)'''
        # 重复性检测
        #if new and self.cnumber in public.calculatorManager.calculatorIndex:
             #return (False, "賬單編號重复")

        return (True, "")
