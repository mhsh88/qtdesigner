# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final01.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from behinesazan.gas.station.software.view.base.HoverButton.HoverButton import HoverButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(997, 576)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/heater.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(26, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = HoverButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(533, 373, 151, 100))
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
        self.pushButton_3.setGeometry(QtCore.QRect(6, 234, 111, 81))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}\n"
"")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/pipeGage.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(150, 100))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = HoverButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(317, 225, 130, 131))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/4way/4way2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(350, 163))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoExclusive(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = HoverButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(359, 351, 85, 90))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/znway/newknee3.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(450, 320))
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoExclusive(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = HoverButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(351, 140, 100, 91))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/znway/newknee1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(450, 320))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = HoverButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(439, 210, 111, 100))
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
        self.pushButton_16.setGeometry(QtCore.QRect(531, 140, 151, 59))
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
        self.pushButton_17.setGeometry(QtCore.QRect(533, 264, 151, 60))
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
        self.pushButton_9.setGeometry(QtCore.QRect(439, 338, 111, 100))
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
        self.pushButton_10.setGeometry(QtCore.QRect(439, 86, 111, 100))
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
        self.pushButton_7 = HoverButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(757, 137, 88, 101))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_7.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/znway/newknee2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setIconSize(QtCore.QSize(450, 320))
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_11 = HoverButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(757, 227, 131, 130))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_11.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/4way/4way.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon8)
        self.pushButton_11.setIconSize(QtCore.QSize(360, 163))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setAutoExclusive(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = HoverButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(756, 351, 92, 91))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_12.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/znway/newpipe2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon9)
        self.pushButton_12.setIconSize(QtCore.QSize(450, 320))
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_14 = HoverButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(879, 237, 110, 81))
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
        self.pushButton_2.setGeometry(QtCore.QRect(115, 240, 101, 101))
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"\n"
"qproperty-icon:url(:/icon/heater.svg);\n"
"qproperty-iconSize: 120px 100px;\n"
"background-color:transparent;\n"
" \n"
"\n"
"}\n"
"QPushButton:hover#pushButton_2\n"
"{\n"
"   qproperty-icon:url(:/icon/heaterRED.svg);\n"
"   background-color:transparent;\n"
"}\n"
"\n"
"QPushButton::checked#pushButton_2{\n"
"\n"
" qproperty-icon:url(:/icon/heaterPressed.svg)\n"
"\n"
"}\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_15 = HoverButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(50, 50, 81, 81))
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}\n"
"")
        self.pushButton_15.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/GasIcon2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_15.setIcon(icon10)
        self.pushButton_15.setIconSize(QtCore.QSize(200, 100))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_22 = HoverButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(150, 51, 81, 81))
        self.pushButton_22.setStyleSheet("QPushButton{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}\n"
"")
        self.pushButton_22.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icon/calculateIcon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_22.setIcon(icon11)
        self.pushButton_22.setIconSize(QtCore.QSize(100, 75))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_24 = HoverButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(680, 250, 80, 70))
        self.pushButton_24.setStyleSheet("QPushButton#pushButton_24{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_24.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icon/regulator/05.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_24.setIcon(icon12)
        self.pushButton_24.setIconSize(QtCore.QSize(200, 100))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_26 = HoverButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(673, 129, 90, 60))
        self.pushButton_26.setStyleSheet("QPushButton#pushButton_26{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_26.setText("")
        self.pushButton_26.setIcon(icon12)
        self.pushButton_26.setIconSize(QtCore.QSize(200, 100))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_28 = HoverButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(680, 380, 80, 61))
        self.pushButton_28.setStyleSheet("QPushButton#pushButton_28{\n"
"\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_28.setText("")
        self.pushButton_28.setIcon(icon12)
        self.pushButton_28.setIconSize(QtCore.QSize(200, 100))
        self.pushButton_28.setObjectName("pushButton_28")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 350, 148, 75))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "نرم افزار محاسبه مصرف گاز ایستگاه تقلیل فشار گاز"))
        self.pushButton_15.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"right\">تعیین خصوصیات گاز طبیعی</p></body></html>"))
        self.pushButton_22.setToolTip(_translate("MainWindow", "<html><head/><body><p>محاسبه نتایج</p></body></html>"))

from behinesazan.gas.station.software.view.base.icon import svgfile_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

