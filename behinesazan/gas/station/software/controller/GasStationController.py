# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final01.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

# import numpy as np
# from scipy.optimize import fsolve
import math

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import MainGasWindow
import OutputlineWidget
import Runs
import inputHeater
import inputlineWidget
from behinesazan.gas.station.software.model.gas.Gas import Gas
from Cumbustion import Combustion
from QpipeLine import PipeLine
from QpipeLineEnd import PipeLineEnd
from Regulator import Regulator
from behinesazan.gas.station.software.view.GasInformationInputForm.GasInformationInputForm import \
    GasInformationInputForm
from behinesazan.gas.station.software.view.GasStation.GasStation import GasStation
from behinesazan.gas.station.software.view.Heater.Heater import Heater
from behinesazan.gas.station.software.view.PipeLine.AfterHeaterLine.AfterHeaterLine import AfterHeaterLine
from behinesazan.gas.station.software.view.PipeLine.BeforeHeaterLine.BeforeHeaterLine import BeforeHeaterLine
from behinesazan.gas.station.software.view.Run.Run import Run


class MainStationWindow(QtWidgets.QMainWindow, MainGasWindow.Ui_MainWindow):


    def __init__(self, parent=None):
        super(MainStationWindow, self).__init__(parent)
        self.setupUi(self)

        self.afterHeaterCheck = False
        self.afterheater = AfterHeaterLine()
        self.pushButton_21.clicked.connect(self.afterheater.show)

        self.inputline = BeforeHeaterLine()
        # self.inputCheck = False
        self.pushButton_3.clicked.connect(self.inputline.show)

        self.heaterCheck = False
        # self.heaterproperty = inputHeaterWidget()
        self.heaterproperty = Heater()
        self.pushButton_2.clicked.connect(self.heaterproperty.show)

        self.runCheck = False
        self.run = Run()
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
        # self.out = OutStation()
        # self.pushButton_14.clicked.connect(self.out.show)

        self.gasCheck = False
        # self.gasProperty = GasProp()
        self.gasProperty = GasInformationInputForm()


        self.pushButton_15.clicked.connect(self.gasProperty.show)

        # self.pushButton_22.clicked.connect(self.calculation)
        self.pushButton_22.clicked.connect(self.inlineCal)



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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = GasStation()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    g = Gas()
    ui.show()

    sys.exit(app.exec_())