# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final01.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
# from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import *
# from PyQt5.QtCore import pyqtSlot
# from numbers import Number
# from decimal import Decimal
import GasLineCalTest
import inputlineWidget
import inputHeater
import OutputlineWidget
import Runs


class RunsWindow(QtWidgets.QWidget, Runs.Ui_Form):
    def __init__(self, parent=None):
        super(RunsWindow, self).__init__(parent)
        self.setupUi(self)

        self.label_9.setDisabled(True)
        self.label_10.setDisabled(True)
        self.label_11.setDisabled(True)
        self.label_12.setDisabled(True)

        self.lineEdit_8.setDisabled(True)
        self.lineEdit_7.setDisabled(True)
        self.lineEdit_9.setDisabled(True)


class inputlineWindow(QtWidgets.QWidget, inputlineWidget.Ui_Form, GasLineCalTest.Reynolds):
    inlineLength = ""
    inlineOuterDiameter = ""
    inlineInnerDiameter = ""
    R = GasLineCalTest.Reynolds(6000, 6)


    def __init__(self, parent=None):
        super(inputlineWindow, self).__init__(parent)

        self.setupUi(self)
        self.lineEdit.setPlaceholderText("ex: 20")
        self.lineEdit_2.setPlaceholderText("ex: 40")
        self.lineEdit_3.setPlaceholderText("ex: 35")


        self.pushButton_2.clicked.connect(self.datagather)
        self.pushButton.clicked.connect(self.cancel)


    def datagather(self):

            try:
                self.inlineLength = float(self.lineEdit.text())
                self.inlineOuterDiameter = float(self.lineEdit_2.text())
                self.inlineInnerDiameter = float(self.lineEdit_3.text())


                if self.inlineOuterDiameter <= self.inlineInnerDiameter:

                    print("قطر داخلی نمی تواند کوچکتر از قطر خارجی لوله باشد! خواهشمند است اصلاح فرمایید.")
                    return
                else:


                    self.pipeLength = self.inlineLength
                    print('ta inja kar mikonad')
                    self.ID = self.inlineInnerDiameter
                    self.OD = self.inlineOuterDiameter
                    self.R.calcul(self.inlineLength, self.inlineInnerDiameter, self.inlineOuterDiameter)
                    self.Tin = self.R.Tin
                    self.Tout = self.R.Tout

                    self.close()





            except:
                print("please enter a real number")
                return

    def cancel(self):
        self.close()


class inputHeaterWidget(QtWidgets.QWidget, inputHeater.Ui_Form):


    def __init__(self, parent = None):
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

        try:
            self.outTemperature = float(self.lineEdit_21.text())
            self.TflueGas1 = float(self.lineEdit_19.text())
            self.O2Mashal1 = float(self.lineEdit_22.text())
            print('تا اینجا که کار میکند')
            if self.radioButton_2.isChecked():
                self.TflueGas2 = float(self.lineEdit_20.text())
                self.O2Mashal2 = float(self.lineEdit_23.text())
                print('تا به اینجا هم کار میکند')
                if self.radioButton_5.isChecked():
                    self.TflueGas3 = float(self.lineEdit_24.text())
                    self.O2Mashal3 = float(self.lineEdit_28.text())
                    print('ببین تا به اینجا هم کار میکند')
                    if self.radioButton_4.isChecked():
                        self.TflueGas3 = float(self.lineEdit_27.text())
                        self.O2Mashal3 = float(self.lineEdit_25.text())
                        print('اوه چه خفن تا اینجا کار کرده تا به اینجا هم کار میکند')



            self.close()
        except:
            print("please enter a real number")
            return


    def cancel(self):
        self.close()


class OutputLineWidget(QtWidgets.QWidget, OutputlineWidget.Ui_Form):
    def __init__(self, parent = None):
        super(OutputLineWidget, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit.setPlaceholderText("ex: 20")
        self.lineEdit_2.setPlaceholderText("ex: 40")
        self.lineEdit_3.setPlaceholderText("ex: 35")


class HoverButton(QPushButton, inputlineWindow, inputHeaterWidget, OutputLineWidget, RunsWindow):
    iconIn = ""
    iconOut = ""
    iconPressed = ""

    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)
        self.setMouseTracking(True)
        self.setStyleSheet("QPushButton{\n"
                           "background-color:transparent;\n"
                           " \n"
                           "\n"
                           "}\n"
                           )
        # self.isCheckable()

    def enterEvent(self, event):
            # if self.isChecked():
            #     self.setIcon(QIcon(self.iconPressed))
               #  self.setStyleSheet("QPushButton#pushButton_2{\n"
               # "\n"
               # "qproperty-icon:url(:/icon/heaterPressed.svg);\n"
               # "qproperty-iconSize: 120px 100px;\n"
               # "background-color:transparent;\n"
               # " \n"
               # "\n"
               # "}\n"
               # )
            # else:
            # if self.objectName() == "pushButton_2":

                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(self.iconIn), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.setIcon(icon)
                if self.objectName() == 'pushButton_6':
                    self.setIconSize(QtCore.QSize(110, 200))
                    self.setAutoFillBackground(True)

            # else:
            #     self.setIcon(QIcon(self.iconIn))
                # self.setStyleSheet("QPushButton#pushButton_2{\n"
                # "\n"
                # "qproperty-icon:url(:/icon/heaterRED.svg);\n"
                # "qproperty-iconSize: 120px 100px;\n"
                # "background-color:transparent;\n"
                # " \n"
                # "\n"
                # "}\n"
                # )

    def leaveEvent(self, event):
            # if self.isChecked():
            #     self.setIcon(QIcon(self.iconPressed))
            # else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.iconOut), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setIcon(icon)
            if self.objectName() == 'pushButton_6':
                self.setIconSize(QtCore.QSize(50, 50))

               #  self.setStyleSheet("QPushButton#pushButton_2{\n"
               # "\n"
               # "qproperty-icon:url(:/icon/heater.svg);\n"
               # "qproperty-iconSize: 120px 100px;\n"
               # "background-color:transparent;\n"
               # " \n"
               # "\n"
               # "}\n"
               # )


    def pushButtonClick(self):
        # self.setIcon(QIcon(self.iconPressed))
        # self.setCheckable(False)
        if self.objectName() == "pushButton_3":
                self.inWindow = inputlineWindow()
                self.inWindow.show()
                self.inWindow.pushButton.clicked.connect(self.cancelButton)
                self.inWindow.pushButton_2.clicked.connect(self.okbutton)
        elif self.objectName() == "pushButton_2":
                self.inWindow = inputHeaterWidget()
                self.inWindow.show()
                self.inWindow.pushButton.clicked.connect(self.cancelButton)
                self.inWindow.pushButton_2.clicked.connect(self.okbutton)
        elif self.objectName() == "pushButton_21":
                self.inWindow = OutputLineWidget()
                self.inWindow.show()
                self.inWindow.pushButton.clicked.connect(self.cancelButton)
                self.inWindow.pushButton_2.clicked.connect(self.okbutton)
        else:
            print('آیا اجرا می شود؟')
            self.runWindow = RunsWindow()
            self.runWindow.show()
            # self.runWindow.pushButton.clicked.connect(self.okbutton)
            # self.runWindow.pushButton_2.clicked.connect(self.cancelButton)


    def cancelButton(self):
        self.setIcon(QIcon(self.iconOut))
        # print(str(self.isDown()))
        # # self.setCheckable(False)
        # # self.setCheckable(True)
        #
        # # self.setEnabled(False)
        # # self.toggled(False)
        # print(str(self.toggle()))
        # self.setChecked(True)
        # print(str(self.isChecked()))
        self.setChecked(False)
        # self.inWindow.close()


    def okbutton(self):
            # self.isChecked(False)
            self.setIcon(QIcon(self.iconOut))
            # self.inWindow.lineLength = float(self.inWindow.lineEdit.text())
            # self.inWindow.inner
            # print(self.inWindow.lineLength)
            # self.inWindow.close()


    def thisIsCalledWhenMouseIsClicked(self):
            print("salam")


        # print("button is pressed!")



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 726)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/heaterdefined.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(26, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = HoverButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(489, 419, 151, 100))
        self.pushButton.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/pipe.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("icon/222467.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("icon/222467.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("icon/222467.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(200, 200))
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = HoverButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 234, 111, 81))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}\n"
"\n"
)
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/pipeGage.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(150, 100))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = HoverButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 190, 201, 200))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/pipes4WayBlack.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(350, 320))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoExclusive(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = HoverButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(389, 383, 111, 110))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/zanuee.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(110, 200))
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoExclusive(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = HoverButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(386, 83, 111, 110))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/zanue02.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = HoverButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(620, 210, 111, 100))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_8.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/valve01.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon6)
        self.pushButton_8.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setAutoExclusive(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_16 = HoverButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(480, 82, 151, 60))
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_16.setText("")
        self.pushButton_16.setIcon(icon1)
        self.pushButton_16.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setAutoExclusive(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = HoverButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(481, 263, 151, 60))
        self.pushButton_17.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_17.setText("")
        self.pushButton_17.setIcon(icon1)
        self.pushButton_17.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setAutoExclusive(True)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_9 = HoverButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(630, 385, 111, 100))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_9.setText("")
        self.pushButton_9.setIcon(icon6)
        self.pushButton_9.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoExclusive(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = HoverButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(620, 28, 111, 100))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_10.setText("")
        self.pushButton_10.setIcon(icon6)
        self.pushButton_10.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoExclusive(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_18 = HoverButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(713, 81, 151, 60))
        self.pushButton_18.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_18.setText("")
        self.pushButton_18.setIcon(icon1)
        self.pushButton_18.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setAutoExclusive(True)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = HoverButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(710, 263, 151, 60))
        self.pushButton_19.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_19.setText("")
        self.pushButton_19.setIcon(icon1)
        self.pushButton_19.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setAutoExclusive(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = HoverButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(720, 438, 151, 60))
        self.pushButton_20.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_20.setText("")
        self.pushButton_20.setIcon(icon1)
        self.pushButton_20.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_20.setCheckable(True)
        self.pushButton_20.setAutoExclusive(True)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_7 = HoverButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(854, 80, 111, 110))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_7.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/zanue03.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QtCore.QSize(110, 200))
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_11 = HoverButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(846, 190, 201, 200))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_11.setText("")
        self.pushButton_11.setIcon(icon3)
        self.pushButton_11.setIconSize(QtCore.QSize(350, 320))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setAutoExclusive(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = HoverButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(859, 379, 111, 110))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_12.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/zanue04.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon9)
        self.pushButton_12.setIconSize(QtCore.QSize(110, 200))
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_14 = HoverButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(1030, 233, 111, 80))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_14.setText("")
        self.pushButton_14.setIcon(icon2)
        self.pushButton_14.setIconSize(QtCore.QSize(150, 100))
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setAutoExclusive(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_21 = HoverButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(210, 234, 111, 81))
        self.pushButton_21.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_21.setText("")
        self.pushButton_21.setIcon(icon2)
        self.pushButton_21.setIconSize(QtCore.QSize(150, 100))
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setAutoExclusive(True)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_2 = HoverButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(119, 240, 101, 101))
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"\n"
"qproperty-icon:url(:/icon/heater.svg);\n"
"qproperty-iconSize: 120px 100px;\n"
 "background-color:transparent;\n"
" \n"
"\n"
"}\n"
)
        self.pushButton_2.setText("")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setToolTip("Click to Configure Heater Properties!\n برای تعیین خصوصیات هیتر کلیک کنید!");
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1240, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.pushButton_2.iconIn = ":/icon/heater05.svg"
        self.pushButton_2.iconIn = ":/icon/heater05.svg"
        self.pushButton_2.iconOut = ":/icon/heater.svg"
        self.pushButton_2.iconPressed = ":/icon/heaterPressed.svg"
        self.pushButton_3.iconIn = ":/icon/pipeGageRed.svg"
        self.pushButton_3.iconOut = ":/icon/pipeGage.svg"
        self.pushButton_3.iconPressed = ":/icon/pipeGagePressed.svg"
        self.pushButton_21.iconIn = ":/icon/pipeGageRed.svg"
        self.pushButton_21.iconOut = ":/icon/pipeGage.svg"
        self.pushButton_21.iconPressed = ":/icon/pipeGagePressed.svg"
        self.pushButton_4.iconIn = ":/icon/pipes4WayRed.svg"
        self.pushButton_4.iconOut = ":/icon/pipes4WayBlack.svg"
        self.pushButton_4.iconPressed = ":/icon/pipes4WayGreen.svg"
        self.pushButton_11.iconIn = ":/icon/pipes4WayRed.svg"
        self.pushButton_11.iconOut = ":/icon/pipes4WayBlack.svg"
        self.pushButton_11.iconPressed = ":/icon/pipes4WayGreen.svg"
        self.pushButton_5.iconIn = ":/icon/zanueeRed.svg"
        self.pushButton_5.iconOut = ":/icon/zanuee.svg"
        self.pushButton_5.iconPressed = ":/icon/zanueeRed.svg"
        self.pushButton_6.iconIn = ":/icon/zanue02Red.svg"
        self.pushButton_6.iconOut = ":/icon/zanue02.svg"
        self.pushButton_6.iconPressed = ":/icon/zanue02Red.svg"
        self.pushButton_7.iconIn = ":/icon/zanue03Red.svg"
        self.pushButton_7.iconOut = ":/icon/zanue03.svg"
        self.pushButton_7.iconPressed = ":/icon/zanue03Red.svg"
        self.pushButton_12.iconIn = ":/icon/zanue04Red.svg"
        self.pushButton_12.iconOut = ":/icon/zanue04.svg"
        self.pushButton_12.iconPressed = ":/icon/zanue04Red.svg"
        self.pushButton_14.iconIn = ":/icon/pipeGageRed.svg"
        self.pushButton_14.iconOut = ":/icon/pipeGage.svg"
        self.pushButton_14.iconPressed = ":/icon/pipeGagePressed.svg"
        self.pushButton_16.iconIn = ":/icon/pipeRed.svg"
        self.pushButton_16.iconOut = ":/icon/pipe.svg"
        self.pushButton_16.iconPressed = ":/icon/pipeRed.svg"
        self.pushButton_18.iconIn = ":/icon/pipeRed.svg"
        self.pushButton_18.iconOut = ":/icon/pipe.svg"
        self.pushButton_18.iconPressed = ":/icon/pipeRed.svg"
        self.pushButton_17.iconIn = ":/icon/pipeRed.svg"
        self.pushButton_17.iconOut = ":/icon/pipe.svg"
        self.pushButton_17.iconPressed = ":/icon/pipeRed.svg"
        self.pushButton.iconIn = ":/icon/pipeRed.svg"
        self.pushButton.iconOut = ":/icon/pipe.svg"
        self.pushButton.iconPressed = ":/icon/pipeRed.svg"
        self.pushButton_20.iconIn = ":/icon/pipeRed.svg"
        self.pushButton_20.iconOut = ":/icon/pipe.svg"
        self.pushButton_20.iconPressed = ":/icon/pipeRed.svg"
        self.pushButton_19.iconIn = ":/icon/pipeRed.svg"
        self.pushButton_19.iconOut = ":/icon/pipe.svg"
        self.pushButton_19.iconPressed = ":/icon/pipeRed.svg"
        self.pushButton_10.iconIn = ":/icon/valveRed.svg"
        self.pushButton_10.iconOut = ":/icon/valve.svg"
        self.pushButton_10.iconPressed = ":/icon/valveRed.svg"
        self.pushButton_8.iconIn = ":/icon/valveRed.svg"
        self.pushButton_8.iconOut = ":/icon/valve.svg"
        self.pushButton_8.iconPressed = ":/icon/valveRed.svg"
        self.pushButton_9.iconIn = ":/icon/valveRed.svg"
        self.pushButton_9.iconOut = ":/icon/valve.svg"
        self.pushButton_9.iconPressed = ":/icon/valveRed.svg"


        self.pushButton_2.clicked.connect(self.pushButton_2.pushButtonClick)
        self.pushButton_3.clicked.connect(self.pushButton_3.pushButtonClick)
        self.pushButton_21.clicked.connect(self.pushButton_21.pushButtonClick)
        self.pushButton_4.clicked.connect(self.pushButton_4.pushButtonClick)
        self.pushButton_6.clicked.connect(self.pushButton_6.pushButtonClick)
        self.pushButton_5.clicked.connect(self.pushButton_5.pushButtonClick)


    def hoverinEvent(self):

            # icon = QtGui.QIcon()
            # icon.addPixmap(QtGui.QPixmap(":/icon/heater05.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            # self.pushButton_2.setIcon(icon)
            icon = QIcon(":/icon/pipe.svg")
            self.pushButton_2.setIcon(icon)
            print("salam")
        # self.mbutton.setIconSize(QSize(200, 200))
    def hoveroutEvent(self):

            # icon = QtGui.QIcon()
            # icon.addPixmap(QtGui.QPixmap(":/icon/heater.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            # self.pushButton_2.setIcon(icon)
            icon = QIcon(":/icon/heater05.svg")

            self.pushButton_2.setIcon(icon)
            print("Bye!!")
         # self.mbutton.setIconSize(QSize(200, 200))






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

import svgfile_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


