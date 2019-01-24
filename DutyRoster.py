"""
    项目：人员值班表
    开发：唐昭
    版本：V2.7
    日期：2019.1.18
    功能描述：程序基本调试完毕，人员排班顺序调整完毕
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DutyRoster(object):
    def setupUi(self, DutyRoster):
        DutyRoster.setObjectName("DutyRoster")
        DutyRoster.resize(800, 600)
        DutyRoster.setMinimumSize(QtCore.QSize(800, 600))
        DutyRoster.setMaximumSize(QtCore.QSize(800, 600))
        self.calendarWidget = QtWidgets.QCalendarWidget(DutyRoster)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.calendarWidget.setMinimumSize(QtCore.QSize(400, 600))
        self.calendarWidget.setMaximumSize(QtCore.QSize(400, 600))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setMinimumDate(QtCore.QDate(2013, 1, 1))
        self.calendarWidget.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.calendarWidget.setObjectName("calendarWidget")
        self.label1 = QtWidgets.QLabel(DutyRoster)
        self.label1.setGeometry(QtCore.QRect(400, 0, 100, 40))
        self.label1.setMinimumSize(QtCore.QSize(100, 40))
        self.label1.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(DutyRoster)
        self.label2.setGeometry(QtCore.QRect(500, 0, 100, 40))
        self.label2.setMinimumSize(QtCore.QSize(100, 40))
        self.label2.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(DutyRoster)
        self.label3.setGeometry(QtCore.QRect(600, 0, 100, 40))
        self.label3.setMinimumSize(QtCore.QSize(100, 40))
        self.label3.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(DutyRoster)
        self.label4.setGeometry(QtCore.QRect(700, 0, 100, 40))
        self.label4.setMinimumSize(QtCore.QSize(100, 40))
        self.label4.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label4.setFont(font)
        self.label4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setObjectName("label4")
        self.label1_0 = QtWidgets.QLabel(DutyRoster)
        self.label1_0.setGeometry(QtCore.QRect(400, 40, 100, 560))
        self.label1_0.setMinimumSize(QtCore.QSize(100, 560))
        self.label1_0.setMaximumSize(QtCore.QSize(100, 560))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.label1_0.setFont(font)
        self.label1_0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label1_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_0.setObjectName("label1_0")
        self.label1_0.setWordWrap(True)
        self.label2_0 = QtWidgets.QLabel(DutyRoster)
        self.label2_0.setGeometry(QtCore.QRect(500, 40, 100, 560))
        self.label2_0.setMinimumSize(QtCore.QSize(100, 560))
        self.label2_0.setMaximumSize(QtCore.QSize(100, 560))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.label2_0.setFont(font)
        self.label2_0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label2_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_0.setObjectName("label2_0")
        self.label2_0.setWordWrap(True)
        self.label3_0 = QtWidgets.QLabel(DutyRoster)
        self.label3_0.setGeometry(QtCore.QRect(600, 40, 100, 560))
        self.label3_0.setMinimumSize(QtCore.QSize(100, 560))
        self.label3_0.setMaximumSize(QtCore.QSize(100, 560))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.label3_0.setFont(font)
        self.label3_0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label3_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_0.setObjectName("label3_0")
        self.label3_0.setWordWrap(True)
        self.label4_0 = QtWidgets.QLabel(DutyRoster)
        self.label4_0.setGeometry(QtCore.QRect(700, 40, 100, 560))
        self.label4_0.setMinimumSize(QtCore.QSize(100, 560))
        self.label4_0.setMaximumSize(QtCore.QSize(100, 560))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.label4_0.setFont(font)
        self.label4_0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label4_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_0.setObjectName("label4_0")
        self.label4_0.setWordWrap(True)

        self.retranslateUi(DutyRoster)

        QtCore.QMetaObject.connectSlotsByName(DutyRoster)

    def retranslateUi(self, DutyRoster):
        _translate = QtCore.QCoreApplication.translate
        DutyRoster.setWindowTitle(_translate("DutyRoster", "FG03排班表V3.0 By FG033 唐昭"))
        self.label1.setText(_translate("DutyRoster", "当日白班"))
        self.label2.setText(_translate("DutyRoster", "当日夜班"))
        self.label3.setText(_translate("DutyRoster", "当日一休"))
        self.label4.setText(_translate("DutyRoster", "当日二休"))
        self.label1_0.setText(_translate("DutyRoster", "当日白班"))
        self.label2_0.setText(_translate("DutyRoster", "当日上夜班"))
        self.label3_0.setText(_translate("DutyRoster", "当日下夜班"))
        self.label4_0.setText(_translate("DutyRoster", "当日休息"))



#主函数
class Duty(QWidget, Ui_DutyRoster):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calendarWidget.clicked[QtCore.QDate].connect(self.plan_duty)
        sel_date = self.calendarWidget.selectedDate()





    def plan_duty(self, sel_date):
        #获取年月日字符串
        year_month_day_str = sel_date.toString("yyyy/MM/dd")
        year = int(year_month_day_str[0:4])
        month = int(year_month_day_str[5:7])
        day = int(year_month_day_str[8:])
        days = 0
        leap_year = 0
        not_leap_yar = 0

        days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        total_years = year - 2012   #之前有几年

        #计算之前有几个闰年
        for year_num in range(2012, year):
            if (year_num % 400) == 0 or ((year_num % 4 ==0) and (year_num % 100 != 0)):
                leap_year += 1
            not_leap_yar = total_years - leap_year

        #计算总天数
        if (year % 400) == 0 or ((year % 4 ==0) and (year % 100 != 0)):
            if month > 2:
                days = leap_year * 366 + not_leap_yar * 365 + sum(days_in_month_list[:month-1]) + 1 + day
            else:
                days = leap_year * 366 + not_leap_yar * 365 + sum(days_in_month_list[:month-1]) + day
        else:
            days = leap_year * 366 + not_leap_yar * 365 + sum(days_in_month_list[:month-1]) + day

        #days_str = str(days)


        #定义排班组合并转化为字符串
        team2_str = str("FG031\n@刘  飞\nFG032\n杨  军\n李京男\n@空  缺\nFG033\n吴海军\n赵  贺\n茅  宁\n胡金祥\n刘振东\n姜国昌\nFG034\n@姚  辉\n@穆春生\n孙  伟\nFG036\n@彭建华\n@吴硕琳\n肖在仁")
        team1_str = str("FG031\n陈  宇\nFG032\n@李宝山\n李广生\n宋承岳\nFG033\n@刘志军\n李海彬\n@谢光琦\n高建成\n胡思楚\n王珏依强\nFG034\n@王  欢\n冯志刚\n惠俊彦\nFG036\n李  远\n聂  飞\n冯宝山")
        team4_str = str("FG031\n刘冬旭\nFG032\n周东兴\n毛文勇\n空  缺\nFG033\n@吴建平\n曹东海\n冯太伟\n崔加云\n马永仓\n王尽宇\nFG034\n张  宇\n韩  磊\n邢进彪\nFG036\n@赵俊忠\n李永生\n宋乃熙")
        team3_str = str("FG031\n@尹奎亮\nFG032\n@李  颖\n高永攀\n毛伍保\nFG033\n卞  克\n韩晨婕\n付  薇\n孙向阳\n仇建国\n空  缺\nFG034\n@朱文斌\n徐秋华\n张宝纪\nFG036\n@李德山\n郭建国\n王书祥")

        if days % 4 == 3:
            self.label1_0.setText(team1_str)
            self.label2_0.setText(team2_str)
            self.label3_0.setText(team3_str)
            self.label4_0.setText(team4_str)
        elif days % 4 == 2:
            self.label1_0.setText(team2_str)
            self.label2_0.setText(team3_str)
            self.label3_0.setText(team4_str)
            self.label4_0.setText(team1_str)
        elif days % 4 == 1:
            self.label1_0.setText(team3_str)
            self.label2_0.setText(team4_str)
            self.label3_0.setText(team1_str)
            self.label4_0.setText(team2_str)
        else:
            self.label1_0.setText(team4_str)
            self.label2_0.setText(team1_str)
            self.label3_0.setText(team2_str)
            self.label4_0.setText(team3_str)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    Mainwindow = Duty()
    Mainwindow.show()
    sys.exit(app.exec_())