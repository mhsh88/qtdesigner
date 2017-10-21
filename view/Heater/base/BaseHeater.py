# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hossein.sharifi\PycharmProjects\pyqtdesigner\view\Heater\ui\heater.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(317, 283)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/heater.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.heater_number_input = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.heater_number_input.setFont(font)
        self.heater_number_input.setObjectName("heater_number_input")
        self.horizontalLayout_3.addWidget(self.heater_number_input)
        self.heater_number_label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.heater_number_label.setFont(font)
        self.heater_number_label.setObjectName("heater_number_label")
        self.horizontalLayout_3.addWidget(self.heater_number_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.heater_number_comboBox = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.heater_number_comboBox.setFont(font)
        self.heater_number_comboBox.setObjectName("heater_number_comboBox")
        self.horizontalLayout_4.addWidget(self.heater_number_comboBox)
        self.heater_base_specification_label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.heater_base_specification_label.setFont(font)
        self.heater_base_specification_label.setObjectName("heater_base_specification_label")
        self.horizontalLayout_4.addWidget(self.heater_base_specification_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.burner_fluegas_label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.burner_fluegas_label.setFont(font)
        self.burner_fluegas_label.setObjectName("burner_fluegas_label")
        self.verticalLayout_2.addWidget(self.burner_fluegas_label)
        self.burner_fluegas_spinbox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.burner_fluegas_spinbox.setMaximum(999.99)
        self.burner_fluegas_spinbox.setObjectName("burner_fluegas_spinbox")
        self.verticalLayout_2.addWidget(self.burner_fluegas_spinbox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.burner_oxygen_percent_label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.burner_oxygen_percent_label.setFont(font)
        self.burner_oxygen_percent_label.setObjectName("burner_oxygen_percent_label")
        self.verticalLayout_3.addWidget(self.burner_oxygen_percent_label)
        self.burner_oxygen_percent_spinbox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.burner_oxygen_percent_spinbox.setMaximum(21.0)
        self.burner_oxygen_percent_spinbox.setObjectName("burner_oxygen_percent_spinbox")
        self.verticalLayout_3.addWidget(self.burner_oxygen_percent_spinbox)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.burner_number_label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.burner_number_label.setFont(font)
        self.burner_number_label.setObjectName("burner_number_label")
        self.verticalLayout.addWidget(self.burner_number_label)
        self.burner_number_comboBox = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.burner_number_comboBox.setFont(font)
        self.burner_number_comboBox.setObjectName("burner_number_comboBox")
        self.burner_number_comboBox.addItem("")
        self.burner_number_comboBox.addItem("")
        self.verticalLayout.addWidget(self.burner_number_comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancelButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(9)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.okButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(9)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_2.addWidget(self.okButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.okButton, self.cancelButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "اطلاعات گرم کن ایستگاه تقلیل فشار گاز"))
        self.groupBox.setTitle(_translate("Form", "گرم کن"))
        self.heater_number_input.setToolTip(_translate("Form", "<html><head/><body><p>تعداد گرم کن ها موجود در ایستگاه</p></body></html>"))
        self.heater_number_label.setText(_translate("Form", "تعداد گرم کن:"))
        self.heater_base_specification_label.setText(_translate("Form", "گرم کن:"))
        self.groupBox_2.setTitle(_translate("Form", "مشعل"))
        self.burner_fluegas_label.setText(_translate("Form", "دمای دودکش (C°)"))
        self.burner_oxygen_percent_label.setText(_translate("Form", "درصد اکسیژن(%)"))
        self.burner_number_label.setText(_translate("Form", "مشعل "))
        self.burner_number_comboBox.setItemText(0, _translate("Form", "1"))
        self.burner_number_comboBox.setItemText(1, _translate("Form", "2"))
        self.cancelButton.setText(_translate("Form", "Cancel"))
        self.okButton.setText(_translate("Form", "Ok"))

import svgfile_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

