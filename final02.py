# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final01.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
# import numpy as np
# from scipy.optimize import fsolve
import math
# from PyQt5.QtWidgets import QPushButton
# from PyQt5.QtCore import pyqtSignal
# from PyQt5.QtGui import *
# from PyQt5.QtCore import pyqtSlot
# from numbers import Number
# from decimal import Decimal
# from GasLineCalTest import Reynolds
from QpipeLine import PipeLine
from QpipeLineEnd import PipeLineEnd
import inputlineWidget
import inputHeater
import OutputlineWidget
import Runs
import MainGasWindow
import OutputStation
import GasProperty
from AgaQt import Gas
from Regulator import Regulator
from Cumbustion import Combustion


class GasProp(QtWidgets.QWidget, GasProperty.Ui_Form):
    def __init__(self, parent=None):
        super(GasProp, self).__init__(parent)
        self.setupUi(self)

        self.label_34.setVisible(False)
        self.label_33.setVisible(False)
        self.label_37.setVisible(False)
        self.label_38.setVisible(False)
        self.label_39.setVisible(False)
        self.label_40.setVisible(False)
        self.label_23.setVisible(False)

        self.pushButton_2.clicked.connect(self.cancel)
        self.pushButton.clicked.connect(self.datagather)

    def datagather(self):
        ui.toutCheck = False
        ui.windCheck = False
        ui.humidityCheck = False
        ui.stationCapacityCheck = False
        try:

            # T standard

            if self.lineEdit_23.text() != "":
                try:
                    if float(self.lineEdit_23.text()) < -273.15:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "لطفاً اطلاعات دمای استاندارد صحیح وارد نمایید.")
                        self.label_34.setVisible(True)
                        self.label_23.setVisible(True)
                        return

                    else:
                        ui.tStandard = float(self.lineEdit_23.text()) + 273.15
                        self.label_34.setVisible(False)
                        self.label_23.setVisible(False)
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "اطلاعات دما به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                    self.label_34.setVisible(True)
                    self.label_23.setVisible(True)
                    return

            else:
                self.label_34.setVisible(True)
                self.label_23.setVisible(True)

            # P Standard
            if self.lineEdit_22.text() != "":
                try:

                    if float(self.lineEdit_22.text()) <= 0:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "فشار گاز مطلق وارد کنید. فشار استاندارد گاز  باید از صفر بیشتر باشد. لطفاً اطلاعات صحیح وارد نمایید.")
                        self.label_33.setVisible(True)
                        self.label_23.setVisible(True)
                        return

                    else:
                        ui.pStandard = float(self.lineEdit_22.text()) * 6.89476

                        self.label_33.setVisible(False)
                        self.label_23.setVisible(False)

                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "اطلاعات فشار استاندارد گاز ورودی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                    self.label_33.setVisible(True)
                    self.label_23.setVisible(True)
                    return


            else:
                self.label_33.setVisible(True)
                self.label_23.setVisible(True)


                # T in gas TEmperature

            if self.lineEdit_25.text() != "":
                try:
                    if float(self.lineEdit_25.text()) < -273.15:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "دمای گاز ورودی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                        self.label_37.setVisible(True)
                        self.label_23.setVisible(True)
                        return

                    else:
                        ui.Tin = float(self.lineEdit_25.text()) + 273.15
                        self.label_37.setVisible(False)
                        self.label_23.setVisible(False)
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "دمای گاز ورودی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                    self.label_37.setVisible(True)
                    self.label_23.setVisible(True)
                    return


            else:
                self.label_37.setVisible(True)
                self.label_23.setVisible(True)




                # P in gas pressure

            if self.lineEdit_24.text() != "":
                try:
                    if float(self.lineEdit_24.text()) * 6.89476 + ui.pStandard <= 0:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "فشار گاز ورودی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                        self.label_38.setVisible(True)
                        self.label_23.setVisible(True)
                        return

                    else:
                        ui.Pin = float(self.lineEdit_24.text()) * 6.89476

                        self.label_38.setVisible(False)
                        self.label_23.setVisible(False)
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "فشار گاز ورودی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                    self.label_38.setVisible(True)
                    self.label_23.setVisible(True)
                    return


            else:
                self.label_38.setVisible(True)
                self.label_23.setVisible(True)


            # T out gas TEmperature

            if self.lineEdit_26.text() != "":
                try:
                    if float(self.lineEdit_26.text()) < -273.15:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "دمای گاز خروجی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                        self.label_39.setVisible(True)
                        self.label_23.setVisible(True)
                        return

                    else:
                        ui.toutStation = float(self.lineEdit_26.text()) + 273.15
                        self.label_39.setVisible(False)
                        self.label_23.setVisible(False)

                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "دمای گاز خروجی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                    self.label_39.setVisible(True)
                    self.label_23.setVisible(True)
                    return


            else:
                self.label_39.setVisible(True)
                self.label_23.setVisible(True)

            # P out gas pressure

            if self.lineEdit_27.text() != "":
                try:
                    if float(self.lineEdit_27.text()) * 6.89476 + ui.pStandard <= 0:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "فشار گاز خروجی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                        self.label_40.setVisible(True)
                        self.label_23.setVisible(True)
                        return

                    else:
                        ui.poutStation = float(self.lineEdit_27.text()) * 6.89476

                        self.label_40.setVisible(False)
                        self.label_23.setVisible(False)
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "فشار گاز خروجی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                    self.label_40.setVisible(True)
                    self.label_23.setVisible(True)
                    return


            else:
                self.label_40.setVisible(True)
                self.label_23.setVisible(True)

            # جک کردن دمای محیط

            if self.lineEdit_28.text() != "":
                try:
                    if float(self.lineEdit_28.text()) < - 273.15:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "اطلاعات دمای محیط به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                    else:
                        ui.outTemperature = float(self.lineEdit_28.text()) + 273.15
                        ui.toutCheck = True
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "اطلاعات دمای محیط به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")

                # Humidity....

            # if self.lineEdit_29.text() != "":
            #     try:
            #         if float(self.lineEdit_29.text()) < 0 or float(self.lineEdit_29.text()) > 100:
            #             QMessageBox.about(self, "خطا در اطلاعات ورودی",
            #                               "رطوبت نسبی نمی تواند کمتر از صفر یا بزرگتر از 100 درصد باشد. لطفاً اطلاعات صحیح وارد نمایید.")
            #
            #         else:
            #             ui.humidity = float(self.lineEdit_29.text())
            #             ui.humidityCheck = True
            #     except:
            #         QMessageBox.about(self, "خطا در اطلاعات ورودی",
            #                           "اطلاعات رطوبت نسبی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")

            # Wind Velocity...

            if self.lineEdit_30.text() != "":
                try:
                    if float(self.lineEdit_30.text()) < 0:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "سرعت باد نمی تواند کوچکتر از صفر باشد. لطفاً اطلاعات صحیح وارد نمایید.")

                    else:
                        ui.windVelocity = float(self.lineEdit_30.text())
                        ui.windCheck = True
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "اطلاعاتی صحبحی برای سرعت باد وارد نشده است. لطفاً اطلاعات صحیح وارد فرمایید")

            # STation Capacity

            if self.lineEdit_31.text() != "":
                try:
                    if float(self.lineEdit_31.text()) <= 0:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "ظرفیت ایستگاه باید از صفر بزرگتر باشد. لطفاً اطلاعات صحیح وارد نمایید.")

                    else:
                        ui.stationCapacity = float(self.lineEdit_31.text())
                        ui.stationCapacityCheck = True
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "ظرفیت ایستگاه به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")

            g.component[0] = float(self.lineEdit.text())
            g.component[1] = float(self.lineEdit_2.text())
            g.component[2] = float(self.lineEdit_3.text())
            g.component[3] = float(self.lineEdit_4.text())
            g.component[4] = float(self.lineEdit_5.text())
            g.component[5] = float(self.lineEdit_6.text())
            g.component[6] = float(self.lineEdit_7.text())
            g.component[7] = float(self.lineEdit_8.text())
            g.component[8] = float(self.lineEdit_9.text())
            g.component[9] = float(self.lineEdit_10.text())
            g.component[10] = float(self.lineEdit_11.text())
            g.component[11] = float(self.lineEdit_12.text())
            g.component[12] = float(self.lineEdit_13.text())
            g.component[13] = float(self.lineEdit_14.text())
            g.component[14] = float(self.lineEdit_15.text())
            g.component[15] = float(self.lineEdit_16.text())
            g.component[16] = float(self.lineEdit_17.text())
            g.component[17] = float(self.lineEdit_18.text())
            g.component[18] = float(self.lineEdit_19.text())
            g.component[19] = float(self.lineEdit_20.text())
            g.component[20] = float(self.lineEdit_21.text())
            g.component = g.component / math.fsum(g.component)
            for comp in g.component:
                if comp < 0:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی", "لطفاً اطلاعات صحیح وارد فرمایید")
                    return


            if self.label_23.isVisible():
                return

            else:
                self.close()
                g.p_theta = ui.pStandard
                g.T_theta = ui.tStandard

                # print(ui.toutStation, ui.poutStation)



                ui.pushButton_15.iconOut = ":/icon/GasdefIcon2.svg"
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(ui.pushButton_15.iconOut), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                ui.pushButton_15.setIcon(icon)

                #
                # QMessageBox.about(self, " اطلاعات وارد شده",
                #                   "شما اینها را وارد کرده اید\n %s \n %s \n %s \n %s \n %s \n %s \n %s" % (
                #                   ui.runLength, ui.runWidth, ui.runOD, ui.runID, ui.Run1debi, ui.Run2debi, ui.Run3debi))


                ui.gasCheck = True

                # ui.gasProperty = None

                # print(self.label_23.isVisible())






        except:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            self.label_34.setVisible(True)
            self.label_33.setVisible(True)
            self.label_37.setVisible(True)
            self.label_38.setVisible(True)
            self.label_39.setVisible(True)
            self.label_40.setVisible(True)
            self.label_23.setVisible(True)

            ui.gasCheck = False
            QMessageBox.about(self, "خطا در اطلاعات ورودی", "لطفاً اطلاعات صحیح وارد فرمایید")

            return

    def cancel(self):
        self.label_34.setVisible(False)
        self.label_33.setVisible(False)
        self.label_37.setVisible(False)
        self.label_38.setVisible(False)
        self.label_39.setVisible(False)
        self.label_40.setVisible(False)
        self.label_23.setVisible(False)
        self.close()
        # ui.gasProperty = None


class OutStation(QtWidgets.QWidget, OutputStation.Ui_Form):
    def __init__(self, parent=None):
        super(OutStation, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.datagather)
        self.pushButton.clicked.connect(self.cancel)

    def datagather(self):
        try:

            #
            # QMessageBox.about(self, " اطلاعات وارد شده",
            #                   "شما اینها را وارد کرده اید\n %s \n %s \n %s \n %s \n %s \n %s \n %s" % (
            #                   ui.runLength, ui.runWidth, ui.runOD, ui.runID, ui.Run1debi, ui.Run2debi, ui.Run3debi))
            ui.outputCheck = True
            self.close()
        except:
            ui.outputCheck = False
            QMessageBox.about(self, "خطا در اطلاعات ورودی", "لطفاً اطلاعات صحیح وارد فرمایید")

            return

    def cancel(self):
        self.close()


class RunsWindow(QtWidgets.QWidget, Runs.Ui_Form):
    def __init__(self, parent=None):
        super(RunsWindow, self).__init__(parent)
        self.setupUi(self)

        self.label_9.setDisabled(True)
        self.label_11.setDisabled(True)

        self.lineEdit_9.setDisabled(True)

        self.pushButton_2.clicked.connect(self.cancel)
        self.pushButton.clicked.connect(self.datagather)

    def datagather(self):
        try:
            self.runLength = float(self.lineEdit_2.text())
            self.runWidth = float(self.lineEdit_4.text())
            self.runOD = float(self.lineEdit_3.text()) * 0.01
            self.runID = self.runOD - 2 * (float(self.lineEdit_5.text()) * 0.01)

            self.Run1debi = float(self.lineEdit.text())
            self.Run2debi = float(self.lineEdit_6.text())

            if self.radioButton_2.isChecked():
                self.Run3debi = float(self.lineEdit_9.text())
            else:
                self.Run3debi = 0

            if self.runOD <= self.runID:

                print("قطر داخلی نمی تواند کوچکتر از قطر خارجی لوله باشد! خواهشمند است اصلاح فرمایید.")
                return
            else:
                ui.runLength = self.runLength
                ui.runWidth = self.runWidth
                ui.runOD = self.runOD
                ui.runID = self.runID
                ui.Run1debi = self.Run1debi
                ui.Run2debi = self.Run2debi
                ui.Run3debi = self.Run3debi
                if ui.runCheck:
                    if ui.Run1debi + ui.Run2debi + ui.Run3debi > ui.stationCapacity:

                        reply = QMessageBox.question(self, 'اخطار',
                                                     "مجموع جریان عبوری از رانها بیش از ظرفیت تعیین شده برای ایستگاه است. آیا مایل به تصحیح ظرفیت ایستگاه هستید؟",
                                                     QMessageBox.Yes |
                                                     QMessageBox.No, QMessageBox.No)
                        if reply == QMessageBox.Yes:
                            ui.stationCapacity = ui.Run1debi + ui.Run2debi + ui.Run3debi
                        else:
                            return


                #
                # QMessageBox.about(self, " اطلاعات وارد شده",
                #                   "شما اینها را وارد کرده اید\n %s \n %s \n %s \n %s \n %s \n %s \n %s" % (
                #                   ui.runLength, ui.runWidth, ui.runOD, ui.runID, ui.Run1debi, ui.Run2debi, ui.Run3debi))

                ui.runCheck = True
                self.close()





        except:
            ui.runCheck = False
            print(sys.exc_info()[1])
            QMessageBox.about(self, "خطا در اطلاعات ورودی", "لطفاً اطلاعات صحیح وارد فرمایید")

            return

    def cancel(self):
        self.close()


class inputlineWindow(QtWidgets.QWidget, inputlineWidget.Ui_Form):
    inlineLength = ""
    inlineOuterDiameter = ""
    inlineInnerDiameter = ""

    # R = Reynolds(6000, 6)


    def __init__(self, parent=None):
        super(inputlineWindow, self).__init__(parent)

        self.setupUi(self)
        self.lineEdit.setPlaceholderText("ex: 20")
        self.lineEdit_2.setPlaceholderText("ex: 30")
        self.lineEdit_3.setPlaceholderText("ex: 2")

        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)

        self.pushButton_2.clicked.connect(self.datagather)
        self.pushButton.clicked.connect(self.cancel)

    def datagather(self):
        ui.inputCheck = False

        try:
            if float(self.lineEdit.text()) <= 0 or float(self.lineEdit_2.text()) * 0.01 <= 0 or float(
                    self.lineEdit_3.text()) * 0.01 <= 0 or float(self.lineEdit_3.text()) * 0.01 >= float(
                    self.lineEdit_2.text()) * 0.01 / 2:
                self.label_4.setVisible(True)
                self.label_5.setVisible(True)
                self.label_6.setVisible(True)
                QMessageBox.about(self, "خطا در اطلاعات ورودی", "لطفاً اطلاعات صحیح وارد فرمایید")
                return

            else:
                ui.inputlineLength = float(self.lineEdit.text())
                ui.inputlineOD = float(self.lineEdit_2.text()) * 0.01
                ui.inputlineID = ui.inputlineOD - 2 * (float(self.lineEdit_3.text()) * 0.01)
                self.label_4.setVisible(False)
                self.label_5.setVisible(False)
                self.label_6.setVisible(False)
                # QMessageBox.about(self, " اطلاعات وارد شده", "شما اینها را وارد کرده اید\n %s \n %s \n %s \n %s \n %s" %(ui.a, ui.b, ui.c, ui.d, ui.f))
                ui.inputCheck = True
                self.close()





        except:
            ui.inputCheck = False
            self.label_4.setVisible(True)
            self.label_5.setVisible(True)
            self.label_6.setVisible(True)
            QMessageBox.about(self, "خطا در اطلاعات ورودی", "لطفاً اطلاعات صحیح وارد فرمایید")

            return

    def cancel(self):
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)
        self.close()


class inputHeaterWidget(QtWidgets.QWidget, inputHeater.Ui_Form):
    def __init__(self, parent=None):
        super(inputHeaterWidget, self).__init__(parent)
        self.setupUi(self)

        self.radioButton_4.setDisabled(True)
        self.radioButton_5.setDisabled(True)

        self.lineEdit_20.setDisabled(True)
        self.lineEdit_23.setDisabled(True)
        self.lineEdit_24.setDisabled(True)
        self.lineEdit_25.setDisabled(True)
        self.lineEdit_27.setDisabled(True)
        self.lineEdit_28.setDisabled(True)

        self.label_20.setDisabled(True)
        self.label_24.setDisabled(True)
        self.label_25.setDisabled(True)
        self.label_26.setDisabled(True)
        self.label_27.setDisabled(True)
        self.label_28.setDisabled(True)
        self.label_32.setDisabled(True)

        self.radioButton_2.toggled['bool'].connect(self.radioButton2Toggled)
        self.radioButton_2.toggled['bool'].connect(self.label_20.setEnabled)
        self.radioButton_2.toggled['bool'].connect(self.label_24.setEnabled)
        self.radioButton_2.toggled['bool'].connect(self.lineEdit_20.setEnabled)
        self.radioButton_2.toggled['bool'].connect(self.lineEdit_23.setEnabled)
        self.radioButton_2.toggled['bool'].connect(self.radioButton_5.setEnabled)

        self.radioButton_5.toggled['bool'].connect(self.radioButton5Toggled)
        self.radioButton_5.toggled['bool'].connect(self.label_26.setEnabled)
        self.radioButton_5.toggled['bool'].connect(self.label_28.setEnabled)
        self.radioButton_5.toggled['bool'].connect(self.label_32.setEnabled)
        self.radioButton_5.toggled['bool'].connect(self.lineEdit_24.setEnabled)
        self.radioButton_5.toggled['bool'].connect(self.lineEdit_28.setEnabled)
        self.radioButton_5.toggled['bool'].connect(self.radioButton_4.setEnabled)

        #
        self.radioButton_4.toggled['bool'].connect(self.label_25.setEnabled)
        self.radioButton_4.toggled['bool'].connect(self.label_27.setEnabled)
        self.radioButton_4.toggled['bool'].connect(self.lineEdit_27.setEnabled)
        self.radioButton_4.toggled['bool'].connect(self.lineEdit_25.setEnabled)

        self.pushButton_2.clicked.connect(self.dataGather)
        self.pushButton.clicked.connect(self.cancel)

    def radioButton2Toggled(self):

        if self.radioButton_5.isChecked():
            self.radioButton_5.setChecked(False)

    def radioButton5Toggled(self):

        if self.radioButton_4.isChecked():
            self.radioButton_4.setChecked(False)

    def dataGather(self):
        ui.mashal2 = False
        ui.mashal3 = False
        ui.mashal4 = False

        try:

            ui.TflueGas1 = float(self.lineEdit_19.text()) + 273.15
            ui.O2Mashal1 = float(self.lineEdit_22.text())

            if self.radioButton_2.isChecked():
                ui.mashal2 = True
                ui.TflueGas2 = float(self.lineEdit_20.text()) + 273.15
                ui.O2Mashal2 = float(self.lineEdit_23.text())

                if self.radioButton_5.isChecked():
                    ui.mashal3 = True
                    ui.TflueGas3 = float(self.lineEdit_24.text()) + 273.15
                    ui.O2Mashal3 = float(self.lineEdit_28.text())

                    if self.radioButton_4.isChecked():
                        ui.mashal4 = True
                        ui.TflueGas4 = float(self.lineEdit_27.text()) + 273.15
                        ui.O2Mashal4 = float(self.lineEdit_25.text())

                    else:
                        ui.mashal4 = False
                else:
                    ui.mashal3 = False
            else:
                ui.mashal2 = False

            ui.heaterCheck = True
            self.close()
        except:
            ui.heaterCheck = False
            QMessageBox.about(self, "خطا در اطلاعات ورودی", "لطفاً اطلاعات صحیح وارد فرمایید")
            return

    def cancel(self):
        self.close()


class OutHeaterWidget(QtWidgets.QWidget, OutputlineWidget.Ui_Form):
    def __init__(self, parent=None):
        super(OutHeaterWidget, self).__init__(parent)
        self.setupUi(self)

        self.lineEdit.setPlaceholderText("ex: 20")
        self.lineEdit_2.setPlaceholderText("ex: 40")
        self.lineEdit_3.setPlaceholderText("ex: 2")

        self.pushButton_2.clicked.connect(self.dataGather)
        self.pushButton.clicked.connect(self.cancel)

    def dataGather(self):

        try:
            print(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text())
            ui.afterHeaterLength = float(self.lineEdit.text())

            ui.afterHeaterOD = float(self.lineEdit_2.text()) * 0.01

            ui.afterHeaterID = ui.afterHeaterOD - 2 * (float(self.lineEdit_3.text()) * 0.01)
            # print(ui.afterHeaterLength,ui.afterHeaterID, ui.afterHeaterOD)
            if ui.afterHeaterOD <= ui.afterHeaterID:

                print("قطر داخلی نمی تواند کوچکتر از قطر خارجی لوله باشد! خواهشمند است اصلاح فرمایید.")
                return
            else:
                ui.afterHeaterCheck = True
                self.close()
        except:
            ui.afterHeaterCheck = False
            QMessageBox.about(self, "خطا در اطلاعات ورودی", "لطفاً اطلاعات صحیح وارد فرمایید")
            return

    def cancel(self):
        self.close()


class MainStationWindow(QtWidgets.QMainWindow, MainGasWindow.Ui_MainWindow):


    def __init__(self, parent=None):
        super(MainStationWindow, self).__init__(parent)
        self.setupUi(self)

        # self.settingVars(self)





        # self.pushButton_2.iconIn = ":/icon/heater05.svg"
        self.pushButton_2.iconIn = ":/icon/heaterred.svg"
        self.pushButton_2.iconOut = ":/icon/heater.svg"
        self.pushButton_2.iconPressed = ":/icon/heaterred.svg"
        self.pushButton_3.iconIn = ":/icon/pipeGageRed.svg"
        self.pushButton_3.iconOut = ":/icon/pipeGage.svg"
        self.pushButton_3.iconPressed = ":/icon/pipeGagePressed.svg"
        self.pushButton_21.iconIn = ":/icon/pipeGageRed.svg"
        self.pushButton_21.iconOut = ":/icon/pipeGage.svg"
        self.pushButton_21.iconPressed = ":/icon/pipeGagePressed.svg"
        self.pushButton_4.iconIn = ":/icon/4way/4way2red.svg"
        self.pushButton_4.iconOut = ":/icon/4way/4way2.svg"
        self.pushButton_4.iconPressed = ":/icon/4way/4way2red.svg"
        self.pushButton_11.iconIn = ":/icon/4way/4wayred.svg"
        self.pushButton_11.iconOut = ":/icon/4way/4way.svg"
        self.pushButton_11.iconPressed = ":/icon/4way/4wayred.svg"
        self.pushButton_5.iconIn = ":/icon/znway/newknee3red.svg"
        self.pushButton_5.iconOut = ":/icon/znway/newknee3.svg"
        self.pushButton_5.iconPressed = ":/icon/znway/newknee3red.svg"
        self.pushButton_6.iconIn = ":/icon/znway/newknee1red.svg"
        self.pushButton_6.iconOut = ":/icon/znway/newknee1.svg"
        self.pushButton_6.iconPressed = ":/icon/znway/newknee1red.svg"
        self.pushButton_7.iconIn = ":/icon/znway/newknee2red.svg"
        self.pushButton_7.iconOut = ":/icon/znway/newknee2.svg"
        self.pushButton_7.iconPressed = ":/icon/znway/newknee2red.svg"
        self.pushButton_12.iconIn = ":/icon/znway/newknee4red.svg"
        self.pushButton_12.iconOut = ":/icon/znway/newknee4.svg"
        self.pushButton_12.iconPressed = ":/icon/znway/newknee4red.svg"
        self.pushButton_14.iconIn = ":/icon/pipeGageRed.svg"
        self.pushButton_14.iconOut = ":/icon/pipeGage.svg"
        self.pushButton_14.iconPressed = ":/icon/pipeGagePressed.svg"
        self.pushButton_16.iconIn = ":/icon/pipeRed.svg"
        self.pushButton_16.iconOut = ":/icon/pipe.svg"
        self.pushButton_16.iconPressed = ":/icon/pipeRed.svg"
        # self.pushButton_18.iconIn = ":/icon/pipeRed.svg"
        # self.pushButton_18.iconOut = ":/icon/pipe.svg"
        # self.pushButton_18.iconPressed = ":/icon/pipeRed.svg"
        self.pushButton_17.iconIn = ":/icon/pipeRed.svg"
        self.pushButton_17.iconOut = ":/icon/pipe.svg"
        self.pushButton_17.iconPressed = ":/icon/pipeRed.svg"
        self.pushButton.iconIn = ":/icon/pipeRed.svg"
        self.pushButton.iconOut = ":/icon/pipe.svg"
        self.pushButton.iconPressed = ":/icon/pipeRed.svg"
        # self.pushButton_20.iconIn = ":/icon/pipeRed.svg"
        # self.pushButton_20.iconOut = ":/icon/pipe.svg"
        # self.pushButton_20.iconPressed = ":/icon/pipeRed.svg"
        # self.pushButton_19.iconIn = ":/icon/pipeRed.svg"
        # self.pushButton_19.iconOut = ":/icon/pipe.svg"
        # self.pushButton_19.iconPressed = ":/icon/pipeRed.svg"
        self.pushButton_10.iconIn = ":/icon/valveRed.svg"
        self.pushButton_10.iconOut = ":/icon/valve.svg"
        self.pushButton_10.iconPressed = ":/icon/valveRed.svg"
        self.pushButton_8.iconIn = ":/icon/valveRed.svg"
        self.pushButton_8.iconOut = ":/icon/valve.svg"
        self.pushButton_8.iconPressed = ":/icon/valveRed.svg"
        self.pushButton_9.iconIn = ":/icon/valveRed.svg"
        self.pushButton_9.iconOut = ":/icon/valve.svg"
        self.pushButton_9.iconPressed = ":/icon/valveRed.svg"
        self.pushButton_15.iconIn = ":/icon/GasinIcon2.svg"
        self.pushButton_15.iconOut = ":/icon/GasIcon2.svg"
        self.pushButton_15.iconPressed = ":/icon/GasinIcon2.svg"
        self.pushButton_22.iconIn = ":/icon/calculateinIcon.svg"
        self.pushButton_22.iconOut = ":/icon/calculateIcon.svg"
        self.pushButton_26.iconIn = ":/icon/regulator/05red.svg"
        self.pushButton_26.iconOut = ":/icon/regulator/05.svg"
        self.pushButton_24.iconIn = ":/icon/regulator/05red.svg"
        self.pushButton_24.iconOut = ":/icon/regulator/05.svg"
        self.pushButton_28.iconIn = ":/icon/regulator/05red.svg"
        self.pushButton_28.iconOut = ":/icon/regulator/05.svg"

        self.afterHeaterCheck = False
        self.afterheater = OutHeaterWidget()
        self.pushButton_21.clicked.connect(self.afterheater.show)

        self.inputline = inputlineWindow()
        # self.inputCheck = False
        self.pushButton_3.clicked.connect(self.inputline.show)

        self.heaterCheck = False
        self.heaterproperty = inputHeaterWidget()
        self.pushButton_2.clicked.connect(self.heaterproperty.show)

        self.runCheck = False
        self.run = RunsWindow()
        self.pushButton_4.clicked.connect(self.run.show)
        self.pushButton_6.clicked.connect(self.run.show)
        self.pushButton_5.clicked.connect(self.run.show)
        self.pushButton_16.clicked.connect(self.run.show)
        self.pushButton_17.clicked.connect(self.run.show)
        self.pushButton.clicked.connect(self.run.show)
        self.pushButton_10.clicked.connect(self.run.show)
        self.pushButton_8.clicked.connect(self.run.show)
        self.pushButton_9.clicked.connect(self.run.show)
        # self.pushButton_19.clicked.connect(self.run.show)
        # self.pushButton_18.clicked.connect(self.run.show)
        # self.pushButton_20.clicked.connect(self.run.show)
        self.pushButton_7.clicked.connect(self.run.show)
        self.pushButton_11.clicked.connect(self.run.show)
        self.pushButton_12.clicked.connect(self.run.show)
        self.pushButton_26.clicked.connect(self.run.show)
        self.pushButton_24.clicked.connect(self.run.show)
        self.pushButton_28.clicked.connect(self.run.show)

        self.outputCheck = False
        self.out = OutStation()
        self.pushButton_14.clicked.connect(self.out.show)

        self.gasCheck = False
        self.gasProperty = GasProp()

        self.pushButton_15.clicked.connect(self.gasProperty.show)

        # self.pushButton_22.clicked.connect(self.calculation)
        self.pushButton_22.clicked.connect(self.inlineCal)

    def gasPropertyFunction(self):
        self.gasProperty = GasProp()
        self.gasProperty.show()



    def inlineCal(self):

        
        try:
            if self.gasCheck:
                tempHHV = Combustion(g, 2, 15, 200)
                HHV = tempHHV.HHVd
                regulator = Regulator(ui.Pin, ui.toutStation, ui.poutStation, g)
                self.tBeforeRegulator = regulator.Tin
                g.calculate(ui.Pin, ui.Tin)
                H1 = g.H
                g.calculate(ui.Pin, self.tBeforeRegulator)
                H2 = g.H
                # self.label_2.setText('T = ' + str(round(math.fsum(self.tBeforeRegulator) - 273.15, 2)) + ' °C')

                self.pushButton_24.setToolTip("T in = %s  °C" %round(math.fsum(self.tBeforeRegulator-273.15),2))
                self.pushButton_26.setToolTip("T in = %s  °C" %round(math.fsum(self.tBeforeRegulator-273.15),2))
                self.pushButton_28.setToolTip("T in = %s  °C" %round(math.fsum(self.tBeforeRegulator-273.15),2))
                if ui.stationCapacityCheck:
                    g.calculate(g.p_theta, g.T_theta)
                    P2 = g.P
                    Z2 = g.Z
                    T2 = g.T
                    Dstd = g.D
                    g.calculate(ui.Pin, ui.Tin)
                    P1 = g.P
                    Z1 = g.Z
                    T1 = g.T

                    Qdot = (ui.stationCapacity / 3600) * (P2 * Z1 * T1) / (P1 * Z2 * T2)
                    # Q1Heater = Qdot * g.D * (H2 - H1) / HHV * 3600
                    Q1Heater = Qdot * g.D * (H2 - H1) / HHV * 3600
                    Q1Heater = Q1Heater / Dstd

                    # self.label.setText(str(round(math.fsum(Q1Heater), 3)) + ' m3/hr')
                    result = (
                    "Q Heater = %s m3/hr" % (round(math.fsum(Q1Heater),3)))

                if ui.heaterCheck and ui.toutCheck:
                    # print('Check')
                    mashal1 = Combustion(g, ui.O2Mashal1, ui.outTemperature, ui.TflueGas1)
                    if ui.mashal2:
                        mashal2 = Combustion(g, ui.O2Mashal2, ui.outTemperature, ui.TflueGas2)
                        if ui.mashal3:
                            mashal3 = Combustion(g, ui.O2Mashal3, ui.outTemperature, ui.TflueGas3)
                            if ui.mashal4:
                                mashal4 = Combustion(g, ui.O2Mashal4, ui.outTemperature, ui.TflueGas4)
                if ui.runCheck and ui.afterHeaterCheck and ui.windCheck and ui.toutCheck:

                    pipelineRun1 = PipeLineEnd(ui.outTemperature, ui.windVelocity, self.tBeforeRegulator, ui.Pin, g,
                                               ui.runOD, ui.runID,
                                               ui.runWidth / 2 + ui.runLength, ui.Run1debi)
                    C_plineRun1 = pipelineRun1.g.C_p

                    pipelineRun3 = PipeLineEnd(ui.outTemperature, ui.windVelocity, self.tBeforeRegulator, ui.Pin, g,
                                               ui.runOD, ui.runID,
                                               ui.runLength, ui.Run2debi)
                    C_plineRun3 = pipelineRun3.g.C_p

                    pipelineRun2 = PipeLineEnd(ui.outTemperature, ui.windVelocity, self.tBeforeRegulator, ui.Pin, g,
                                               ui.runOD, ui.runID,
                                               ui.runWidth / 2 + ui.runLength, ui.Run3debi)
                    C_plineRun2 = pipelineRun2.g.C_p

                    tbeforerun = max(pipelineRun1.Tout, pipelineRun2.Tout, pipelineRun3.Tout)


                    pipeline1 = PipeLine(ui.outTemperature, ui.windVelocity, ui.Tin, ui.Pin, g, ui.inputlineOD,
                                         ui.inputlineID,
                                         ui.inputlineLength, ui.Run1debi + ui.Run2debi + ui.Run3debi)

                    C_pline1 = pipeline1.g.C_p
                    H_pipeline1 = pipeline1.g.H

                    pipeline2 = PipeLineEnd(ui.outTemperature, ui.windVelocity, tbeforerun, ui.Pin, g,
                                            ui.afterHeaterOD, ui.afterHeaterID,
                                            ui.afterHeaterLength, ui.Run1debi + ui.Run2debi + ui.Run3debi)
                    C_pline2 = pipeline2.g.C_p
                    H_pipeline2 = pipeline2.g.H

                    H_Heater = H_pipeline2 - H_pipeline1

                    C_p = (C_pline1 + C_pline2) / 2

                    QHeaterDeltaT = pipeline2.mdot * C_p * (pipeline2.Tout - pipeline1.Tout)
                    QHeaterEntalpy = pipeline2.mdot * H_Heater
                     # print('T beforheater = %s, T after Heater = %s' % (pipeline1.Tout - 273.15, pipeline2.Tout - 273.15))
                    # print("C_p = %s" %C_pline1)
                    Qdot = pipeline2.Qdot + pipelineRun1.Qdot + pipelineRun2.Qdot + pipelineRun3.Qdot
                    Q_Total = QHeaterEntalpy - Qdot


                    g.calculate(g.p_theta, g.T_theta)
                    P2 = g.P
                    Z2 = g.Z
                    T2 = g.T
                    D = g.D
                    g.calculate(ui.Pin, ui.Tin)
                    P1 = g.P
                    Z1 = g.Z
                    T1 = g.T

                    mdot = (ui.stationCapacity / 3600) * (P2 * Z1 * T1) / (P1 * Z2 * T2)
                    Q1Heater = Q_Total / HHV / D * 3600
                    # Q1Heater = mdot * (H2 - H1) / HHV * 3600
                    #
                    # Q1Heater = Qdot * (H2 - H1) / HHV * 3600
                    # Q1Heater = Q_Total

                    result = ("Q Heater = %s m3/hr\n" %round(math.fsum(Q1Heater),3))

                    # self.label.setText(str(round(math.fsum(Q_Total) / 1000, 3)) + ' m3/hr')
                    # self.label_2.setText(str(round(math.fsum(pipeline2.Tout - 273.15), 3)) + ' °C')





                if ui.stationCapacityCheck:
                    if ui.heaterCheck:
                        Qburner1 = Q1Heater / mashal1.eff
                        QT = Qburner1
                        print(QT)
                        result = ("Q Heater = %s m3/hr\n Q burner = %s m3/hr" %(round(math.fsum(QT),3), round(math.fsum(Qburner1),3)))
                        # self.pushButton_2.setToolTip(result) #+ str(round(math.fsum(QT),3)))
                        if ui.mashal2:
                            Qburner1 = Q1Heater / 2 / mashal1.eff
                            Qburner2 = Q1Heater / 2 / mashal2.eff
                            QT = Qburner1 + Qburner2
                            result = ("Q Heater = %s m3/hr\nQ burner 1 = %s m3/hr\nQ burner 2 = %s m3/hr" %(round(math.fsum(QT),3), round(math.fsum(Qburner1),3), round(math.fsum(Qburner2),3)))
                            if ui.mashal3:
                                Qburner1 = Q1Heater/2/2/mashal1.eff
                                Qburner2 = Q1Heater/2/2/mashal2.eff
                                Qburner3 = Q1Heater/2/mashal3.eff
                                QT = Qburner1 + Qburner2 + Qburner3
                                result = ("Q Heater 1 = %s m3/hr\nQ burner 1 = %s m3/hr\nQ burner 2 = %s m3/hr\nQ Heater 2 = %s m3/hr\nQ burner 3 = %s m3/hr" %(round(math.fsum(Qburner1+Qburner2),3), round(math.fsum(Qburner1),3), round(math.fsum(Qburner2),3), round(math.fsum(Qburner3),3), round(math.fsum(Qburner3),3)))
                                if ui.mashal4:
                                    Qburner1 = Q1Heater/2/2/mashal1.eff
                                    Qburner2 = Q1Heater/2/2/mashal2.eff
                                    Qburner3 = Q1Heater/2/2/mashal3.eff
                                    Qburner4 = Q1Heater/2/2/mashal3.eff
                                    QT = Qburner1 + Qburner2 + Qburner3 + Qburner4
                                    result = ("Q Heater 1 = %s m3/hr\nQ burner 1 = %s m3/hr\nQ burner 2 = %s m3/hr\nQ Heater 2 = %s m3/hr\nQ burner 3 = %s m3/hr\nQ burner 4 = %s m3/hr"
                                              %(round(math.fsum(Qburner1+Qburner2),3), round(math.fsum(Qburner1),3), round(math.fsum(Qburner2),3), round(math.fsum(Qburner3+ Qburner4),3), round(math.fsum(Qburner3),3), round(math.fsum(Qburner4),3)))
                                    #self.pushButton_2.setToolTip("MainWindow", "<html><head/><body><p>Q Heater = " + str(QT)+"</p></body></html>")
                                    # print(QT)

                    self.pushButton_2.setToolTip(result) #+ str(round(math.fsum(QT),3)))
            else:
                QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                  "اطلاعات گاز ورودی کامل نشده است. خواهشمند است اطلاعات را به صورت کامل وارد نمایید.")
                return
        except:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(sys.exc_info()[2])



    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "برای خروج از نرم افزار اطمینان دارید؟", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.out.close()
            self.gasProperty.close()

            self.run.close()
            self.heaterproperty.close()
            self.afterheater.close()
            self.inputline.close()
            event.accept()
        else:
            event.ignore()


    def settingVar(self):
        self.pStandard = ''
        self.tStandard = ''
        self.Tin = ''
        self.Pin = ''
        self.toutStation = ''
        self.poutStation = ''
        self.outTemperature = ''
        self.windVelocity = ''





import svgfile_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = MainStationWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    g = Gas()
    ui.show()

    sys.exit(app.exec_())
