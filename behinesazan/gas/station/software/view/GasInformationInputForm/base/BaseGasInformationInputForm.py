# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GasInformationInputForm.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(583, 607)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/heater.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.comboBox = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox)
        self.label_24 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_7.addWidget(self.label_24)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_2.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_2.addWidget(self.label_21)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout.addWidget(self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout.addWidget(self.lineEdit_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(Form)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout.addWidget(self.lineEdit_11)
        self.lineEdit_12 = QtWidgets.QLineEdit(Form)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout.addWidget(self.lineEdit_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(Form)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout.addWidget(self.lineEdit_13)
        self.lineEdit_14 = QtWidgets.QLineEdit(Form)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.verticalLayout.addWidget(self.lineEdit_14)
        self.lineEdit_15 = QtWidgets.QLineEdit(Form)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.verticalLayout.addWidget(self.lineEdit_15)
        self.lineEdit_16 = QtWidgets.QLineEdit(Form)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.verticalLayout.addWidget(self.lineEdit_16)
        self.lineEdit_17 = QtWidgets.QLineEdit(Form)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.verticalLayout.addWidget(self.lineEdit_17)
        self.lineEdit_18 = QtWidgets.QLineEdit(Form)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.verticalLayout.addWidget(self.lineEdit_18)
        self.lineEdit_19 = QtWidgets.QLineEdit(Form)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.verticalLayout.addWidget(self.lineEdit_19)
        self.lineEdit_20 = QtWidgets.QLineEdit(Form)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.verticalLayout.addWidget(self.lineEdit_20)
        self.lineEdit_21 = QtWidgets.QLineEdit(Form)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.verticalLayout.addWidget(self.lineEdit_21)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_8.addWidget(self.line)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_23 = QtWidgets.QLineEdit(Form)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.verticalLayout_4.addWidget(self.lineEdit_23)
        self.lineEdit_22 = QtWidgets.QLineEdit(Form)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.verticalLayout_4.addWidget(self.lineEdit_22)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 2, 1)
        self.label_34 = QtWidgets.QLabel(Form)
        self.label_34.setStyleSheet("QLabel#label_34{ \n"
"\n"
"color : red;\n"
"\n"
" }")
        self.label_34.setObjectName("label_34")
        self.gridLayout_2.addWidget(self.label_34, 0, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(Form)
        self.label_33.setStyleSheet("QLabel#label_33{ \n"
"\n"
"color : red;\n"
"\n"
" }")
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_25 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_5.addWidget(self.label_25)
        self.label_22 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_5.addWidget(self.label_22)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_13.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_13.addWidget(self.line_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEdit_25 = QtWidgets.QLineEdit(Form)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.verticalLayout_8.addWidget(self.lineEdit_25)
        self.lineEdit_24 = QtWidgets.QLineEdit(Form)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.verticalLayout_8.addWidget(self.lineEdit_24)
        self.gridLayout_3.addLayout(self.verticalLayout_8, 0, 0, 2, 1)
        self.label_37 = QtWidgets.QLabel(Form)
        self.label_37.setStyleSheet("QLabel#label_37{ \n"
"\n"
"color : red;\n"
"\n"
" }")
        self.label_37.setObjectName("label_37")
        self.gridLayout_3.addWidget(self.label_37, 0, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(Form)
        self.label_38.setStyleSheet("QLabel#label_38{ \n"
"\n"
"color : red;\n"
"\n"
" }")
        self.label_38.setObjectName("label_38")
        self.gridLayout_3.addWidget(self.label_38, 1, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_26 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_6.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_6.addWidget(self.label_27)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_13.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lineEdit_26 = QtWidgets.QLineEdit(Form)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.verticalLayout_9.addWidget(self.lineEdit_26)
        self.lineEdit_27 = QtWidgets.QLineEdit(Form)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.verticalLayout_9.addWidget(self.lineEdit_27)
        self.gridLayout_4.addLayout(self.verticalLayout_9, 0, 0, 2, 1)
        self.label_39 = QtWidgets.QLabel(Form)
        self.label_39.setStyleSheet("QLabel#label_39{ \n"
"\n"
"color : red;\n"
"\n"
" }")
        self.label_39.setObjectName("label_39")
        self.gridLayout_4.addWidget(self.label_39, 0, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(Form)
        self.label_40.setStyleSheet("QLabel#label_40{ \n"
"\n"
"color : red;\n"
"\n"
" }")
        self.label_40.setObjectName("label_40")
        self.gridLayout_4.addWidget(self.label_40, 1, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_4)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_28 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_10.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_10.addWidget(self.label_29)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.verticalLayout_13.addLayout(self.horizontalLayout_4)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_13.addWidget(self.line_3)
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_13.addWidget(self.line_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lineEdit_28 = QtWidgets.QLineEdit(Form)
        self.lineEdit_28.setText("")
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.verticalLayout_11.addWidget(self.lineEdit_28)
        self.lineEdit_30 = QtWidgets.QLineEdit(Form)
        self.lineEdit_30.setText("")
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.verticalLayout_11.addWidget(self.lineEdit_30)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_30 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_12.addWidget(self.label_30)
        self.label_32 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_12.addWidget(self.label_32)
        self.horizontalLayout_5.addLayout(self.verticalLayout_12)
        self.verticalLayout_13.addLayout(self.horizontalLayout_5)
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_13.addWidget(self.line_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_31 = QtWidgets.QLineEdit(Form)
        self.lineEdit_31.setText("")
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.horizontalLayout_6.addWidget(self.lineEdit_31)
        self.label_35 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_6.addWidget(self.label_35)
        self.verticalLayout_13.addLayout(self.horizontalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem1)
        self.label_23 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("QLabel#label_23{ \n"
"\n"
"color : red;\n"
"\n"
" }")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_13.addWidget(self.label_23)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_13.addLayout(self.horizontalLayout)
        self.horizontalLayout_8.addLayout(self.verticalLayout_13)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "اطلاعات ورودی ایستگاه تقلیل فشار گاز"))
        self.comboBox.setItemText(0, _translate("Form", "درصد جرمی"))
        self.comboBox.setItemText(1, _translate("Form", "درصد حجمی"))
        self.comboBox.setItemText(2, _translate("Form", "درصد مولی"))
        self.label_24.setText(_translate("Form", "ترکیب گاز:"))
        self.label.setText(_translate("Form", "Nitrogen"))
        self.label_2.setText(_translate("Form", "Carbon Dioxide"))
        self.label_3.setText(_translate("Form", "Methane"))
        self.label_4.setText(_translate("Form", "Ethane"))
        self.label_5.setText(_translate("Form", "Propane"))
        self.label_6.setText(_translate("Form", "n-Butane"))
        self.label_7.setText(_translate("Form", "iso-Butane"))
        self.label_8.setText(_translate("Form", "n-Pentane"))
        self.label_9.setText(_translate("Form", "iso-Pentane"))
        self.label_10.setText(_translate("Form", "Hexane"))
        self.label_11.setText(_translate("Form", "Heptane"))
        self.label_12.setText(_translate("Form", "Octane"))
        self.label_13.setText(_translate("Form", "Nonane"))
        self.label_14.setText(_translate("Form", "Decane"))
        self.label_15.setText(_translate("Form", "Hydrogen"))
        self.label_16.setText(_translate("Form", "Oxygen"))
        self.label_17.setText(_translate("Form", "Crbon Monoxide"))
        self.label_18.setText(_translate("Form", "Water"))
        self.label_19.setText(_translate("Form", "Hydrogen Sulfide"))
        self.label_20.setText(_translate("Form", "Helium"))
        self.label_21.setText(_translate("Form", "Argon"))
        self.lineEdit.setText(_translate("Form", "0"))
        self.lineEdit_2.setText(_translate("Form", "0"))
        self.lineEdit_3.setText(_translate("Form", "100"))
        self.lineEdit_4.setText(_translate("Form", "0"))
        self.lineEdit_5.setText(_translate("Form", "0"))
        self.lineEdit_6.setText(_translate("Form", "0"))
        self.lineEdit_7.setText(_translate("Form", "0"))
        self.lineEdit_8.setText(_translate("Form", "0"))
        self.lineEdit_9.setText(_translate("Form", "0"))
        self.lineEdit_10.setText(_translate("Form", "0"))
        self.lineEdit_11.setText(_translate("Form", "0"))
        self.lineEdit_12.setText(_translate("Form", "0"))
        self.lineEdit_13.setText(_translate("Form", "0"))
        self.lineEdit_14.setText(_translate("Form", "0"))
        self.lineEdit_15.setText(_translate("Form", "0"))
        self.lineEdit_16.setText(_translate("Form", "0"))
        self.lineEdit_17.setText(_translate("Form", "0"))
        self.lineEdit_18.setText(_translate("Form", "0"))
        self.lineEdit_19.setText(_translate("Form", "0"))
        self.lineEdit_20.setText(_translate("Form", "0"))
        self.lineEdit_21.setText(_translate("Form", "0"))
        self.lineEdit_23.setText(_translate("Form", "15"))
        self.lineEdit_23.setPlaceholderText(_translate("Form", "15°C"))
        self.lineEdit_22.setText(_translate("Form", "101.325"))
        self.lineEdit_22.setPlaceholderText(_translate("Form", "101325 kPa"))
        self.label_34.setText(_translate("Form", "*"))
        self.label_33.setText(_translate("Form", "*"))
        self.label_25.setText(_translate("Form", "دمای گاز استاندارد (C°) :"))
        self.label_22.setText(_translate("Form", "فشار گاز استاندارد (kPa) :"))
        self.lineEdit_25.setText(_translate("Form", "7"))
        self.lineEdit_25.setPlaceholderText(_translate("Form", "7°C"))
        self.lineEdit_24.setText(_translate("Form", "600"))
        self.lineEdit_24.setPlaceholderText(_translate("Form", "650 Psi"))
        self.label_37.setText(_translate("Form", "*"))
        self.label_38.setText(_translate("Form", "*"))
        self.label_26.setText(_translate("Form", "دمای گاز ورودی به ایستگاه (C°) :"))
        self.label_27.setText(_translate("Form", "فشار گاز ورودی به ایستگاه (Psi) :"))
        self.lineEdit_26.setText(_translate("Form", "8"))
        self.lineEdit_26.setPlaceholderText(_translate("Form", "8°C"))
        self.lineEdit_27.setText(_translate("Form", "250"))
        self.lineEdit_27.setPlaceholderText(_translate("Form", "250 Psi"))
        self.label_39.setText(_translate("Form", "*"))
        self.label_40.setText(_translate("Form", "*"))
        self.label_28.setText(_translate("Form", "دمای گاز خروجی از ایستگاه (C°) :"))
        self.label_29.setText(_translate("Form", "فشار گاز خروجی از ایستگاه (Psi) :"))
        self.lineEdit_28.setPlaceholderText(_translate("Form", "15°C"))
        self.lineEdit_30.setPlaceholderText(_translate("Form", "10 m/s"))
        self.label_30.setText(_translate("Form", "دمای محیط (C°) :"))
        self.label_32.setText(_translate("Form", "سرعت باد (m/s):"))
        self.lineEdit_31.setPlaceholderText(_translate("Form", "30000 (m3/hr)"))
        self.label_35.setText(_translate("Form", "دبی گاز عبوری از ایستگاه (متر مکعب بر ساعت) :"))
        self.label_23.setText(_translate("Form", "* الزامی"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        self.pushButton.setText(_translate("Form", "Ok"))

import svgfile_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

