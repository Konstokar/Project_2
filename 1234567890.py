import sys                                             #
import math                                            #
from PyQt5.QtWidgets import QApplication, QMainWindow  # импрот необходимых для работы модулей
from uk import Ui_Universal_calculator                 # (некоторые из них я придумал сам)
import Number                                          #


class MyWidget(QMainWindow, Ui_Universal_calculator):
    def __init__(self):  # инициализация кнопок
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run_1)
        self.pushButton_2.clicked.connect(self.run_2)
        self.pushButton_3.clicked.connect(self.run_3)
        self.pushButton_4.clicked.connect(self.run_4)
        self.pushButton_5.clicked.connect(self.run_5)
        self.pushButton_6.clicked.connect(self.run_6)
        self.pushButton_7.clicked.connect(self.run_7)
        self.pushButton_8.clicked.connect(self.run_8)
        self.pushButton_9.clicked.connect(self.run_9)
        self.pushButton_18.clicked.connect(self.run_10)
        self.pushButton_10.clicked.connect(self.run_11)
        self.pushButton_12.clicked.connect(self.run_12)
        self.pushButton_14.clicked.connect(self.run_13)
        self.pushButton_13.clicked.connect(self.run_14)
        self.pushButton_16.clicked.connect(self.run_15)
        self.pushButton_11.clicked.connect(self.run_16)
        self.pushButton_15.clicked.connect(self.run_17)
        self.pushButton_17.clicked.connect(self.run_18)
        self.pushButton_19.clicked.connect(self.run_19)
        self.pushButton_20.clicked.connect(self.run_20)
        self.pushButton_21.clicked.connect(self.run_21)
        self.pushButton_22.clicked.connect(self.run_22)
        self.pushButton_23.clicked.connect(self.run_23)
        self.pushButton_24.clicked.connect(self.run_24)
        self.pushButton_25.clicked.connect(self.run_25)
        self.pushButton_26.clicked.connect(self.run_26)
        self.pushButton_27.clicked.connect(self.run_27)
        self.pushButton_28.clicked.connect(self.run_28)
        self.pushButton_29.clicked.connect(self.run_29)
        self.pushButton_30.clicked.connect(self.run_30)
        self.pushButton_31.clicked.connect(self.run_31)
        self.pushButton_32.clicked.connect(self.run_32)
        self.pushButton_33.clicked.connect(self.run_33)
        self.pushButton_34.clicked.connect(self.run_34)
        self.pushButton_35.clicked.connect(self.run_35)
        self.pushButton_36.clicked.connect(self.run_36)
        self.pushButton_37.clicked.connect(self.run_37)
        self.pushButton_38.clicked.connect(self.run_38)
        self.pushButton_39.clicked.connect(self.run_39)
        self.pushButton_40.clicked.connect(self.run_40)
        self.pushButton_41.clicked.connect(self.run_41)
        self.pushButton_42.clicked.connect(self.run_42)
        self.pushButton_43.clicked.connect(self.run_43)
        self.pushButton_44.clicked.connect(self.run_44)
        self.pushButton_45.clicked.connect(self.run_45)
        # self.pushButton_46.clicked.connect(self.run_46)
        # self.pushButton_47.clicked.connect(self.run_47)
        # self.pushButton_48.clicked.connect(self.run_48)
        # self.pushButton_49.clicked.connect(self.run_49)
        # self.pushButton_50.clicked.connect(self.run_50)
        # self.pushButton_51.clicked.connect(self.run_51)
        # self.pushButton_52.clicked.connect(self.run_52)
        # self.pushButton_53.clicked.connect(self.run_53)
        # self.pushButton_54.clicked.connect(self.run_54)
        # self.pushButton_55.clicked.connect(self.run_55)
        # self.pushButton_56.clicked.connect(self.run_56)
        # self.pushButton_57.clicked.connect(self.run_57)
        # self.pushButton_58.clicked.connect(self.run_58)
        # self.pushButton_59.clicked.connect(self.run_62)
        # self.pushButton_60.clicked.connect(self.run_64)
        # self.pushButton_61.clicked.connect(self.run_66)
        # self.pushButton_62.clicked.connect(self.run_60)
        # self.pushButton_63.clicked.connect(self.run_63)
        # self.pushButton_64.clicked.connect(self.run_69)
        # self.pushButton_65.clicked.connect(self.run_59)
        # self.pushButton_66.clicked.connect(self.run_68)
        # self.pushButton_67.clicked.connect(self.run_67)
        # self.pushButton_68.clicked.connect(self.run_65)
        # self.pushButton_69.clicked.connect(self.run_61)
        # self.pushButton_70.clicked.connect(self.run_70)
        self.x = ''
        self.y = ''

    def run_1(self):  # сумма x и у
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(x + y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_2(self):  # разность x и у
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(x - y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_3(self):  # произведение x и у
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(x * y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_4(self):  # деление x и у
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(x / y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_5(self):  # возведение x в степень у
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(x ** y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_6(self):  # квадратный корень х
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.sqrt(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_7(self):  # квадратный корень у
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.sqrt(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_8(self):  # факториал x
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.factorial(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_9(self):  # факториал у
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.factorial(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_10(self):  # -х
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(-x)
        except Exception:
            self.lcdNumber.display('Error')

    def run_11(self):  # -у
        try:
            if '.' in self.lineEdit.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(-y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_12(self):  # перевод х из процентного значения
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(x / 100)
        except Exception:
            self.lcdNumber.display('Error')

    def run_13(self):  # перевод у из процентного значения
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(y / 100)
        except Exception:
            self.lcdNumber.display('Error')

    def run_14(self):  # возведение х в квадрат
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(x ** 2)
        except Exception:
            self.lcdNumber.display('Error')

    def run_15(self):  # возведение у в квадрат
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(y ** 2)
        except Exception:
            self.lcdNumber.display('Error')

    def run_16(self):  # возведение х в куб
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(x ** 3)
        except Exception:
            self.lcdNumber.display('Error')

    def run_17(self):  # возведение у в куб
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(y ** 3)
        except Exception:
            self.lcdNumber.display('Error')

    def run_18(self):  # вывод числа пи
        self.lcdNumber.display(math.pi)

    def run_19(self):  # деление 1 на х
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(1 / x)
        except Exception:
            self.lcdNumber.display('Error')

    def run_20(self):  # деление 1 на у
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(1 / y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_21(self):  # возведение 10 в степень х
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(10 ** x)
        except Exception:
            self.lcdNumber.display('Error')

    def run_22(self):   # возведение 10 в степень у
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(10 ** y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_23(self):  # модуль х
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.fabs(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_24(self):  # модуль у
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.fabs(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_25(self):  # округление х до ближайшего большего числа
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.ceil(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_26(self):  # округление у до ближайшего большего числа
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.ceil(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_27(self):  # основание натурального логарифма
        self.lcdNumber.display(math.e)

    def run_28(self):  # тангенс х
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.tan(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_29(self):  # округление х вниз
        try:
            if '.' in self.lineEdit_2.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.floor(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_30(self):  # округление у вниз
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.floor(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_31(self):  # целочисленное деление х на у
        try:
            if '.' in self.lineEdit_2.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(x // y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_32(self):  # остаток от деления х на у
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit_2.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.fmod(x, y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_33(self):  # целочисленное деление у на х (функция для лентяев)
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit_2.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(y // x)
        except Exception:
            self.lcdNumber.display('Error')

    def run_34(self):  # остаток от деления у на х (функция для лентяев)
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit_2.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.fmod(y, x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_35(self):  # разность у и х (функция для лентяев)
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(y - x)
        except Exception:
            self.lcdNumber.display('Error')

    def run_36(self):  # тангенс у
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.tan(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_37(self):  # усекает значение х до целого.
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.trunc(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_38(self):  # усекает значение у до целого.
        try:
            if '.' in self.lineEdit.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.trunc(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_39(self):  # синус х
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.sin(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_40(self):  # синус у
        try:
            if '.' in self.lineEdit.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.sin(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_41(self):  # косинус х
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.cos(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_42(self):  # косинус у
        try:
            if '.' in self.lineEdit.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.cos(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_43(self):  # проверка х на простоту
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(Number.IsPrime(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_44(self):  # проверка у на простоту
        try:
            if '.' in self.lineEdit.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(Number.IsPrime(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_45(self):  # вывод константы "золотое сечение"
        self.lcdNumber.display('1.61803398875')

    # def run_46(self):
        # self.x += '9'
        # self.lcdNumber_2.display(self.x)

    # def run_47(self):
        # self.x += '8'
        # self.lcdNumber_2.display(self.x)

    # def run_48(self):
        # self.x += '7'
        # self.lcdNumber_2.display(self.x)

    # def run_49(self):
        # self.x += '6'
        # self.lcdNumber_2.display(self.x)

    # def run_50(self):
        # self.x += '5'
        # self.lcdNumber_2.display(self.x)

    # def run_51(self):
        # self.x += '4'
        # self.lcdNumber_2.display(self.x)

    # def run_52(self):
        # self.x += '3'
        # self.lcdNumber_2.display(self.x)

    # def run_53(self):
        # self.x += '2'
        # self.lcdNumber_2.display(self.x)

    # def run_54(self):
        # self.x += '1'
        # self.lcdNumber_2.display(self.x)

    # def run_55(self):
        # self.x += '0'
        # self.lcdNumber_2.display(self.x)

    # def run_56(self):
        # self.x += '.'
        # self.lcdNumber_2.display(self.x)

    # def run_57(self):
        # self.x += '-'
        # self.lcdNumber_2.display(self.x)

    # def run_58(self):
        # self.y += '9'
        # self.lcdNumber_3.display(self.y)

    # def run_59(self):
        # self.y += '8'
        # self.lcdNumber_3.display(self.y)

    # def run_60(self):
        # self.y += '7'
        # self.lcdNumber_3.display(self.y)

    # def run_61(self):
        # self.y += '6'
        # self.lcdNumber_3.display(self.y)

    # def run_62(self):
        # self.y += '5'
        # self.lcdNumber_3.display(self.y)

    # def run_63(self):
        # self.y += '4'
        # self.lcdNumber_3.display(self.y)

    # def run_64(self):
        # self.y += '3'
        # self.lcdNumber_3.display(self.y)

    # def run_65(self):
        # self.y += '2'
        # self.lcdNumber_3.display(self.y)

    # def run_66(self):
        # self.y += '1'
        # self.lcdNumber_3.display(self.y)

    # def run_67(self):
        # self.y += '0'
        # self.lcdNumber_3.display(self.y)

    # def run_68(self):
        # self.y += '.'
        # self.lcdNumber_3.display(self.y)

    # def run_69(self):
        # self.y += '-'
        # self.lcdNumber_3.display(self.y)

    # def run_70(self):
        # self.y = ''
        # print(self.y)

    # def run_71(self):
        # self.x = ''


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
