from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMessageBox

from behinesazan.gas.station.software.view.Heater.base import BaseHeater


class Heater(QtWidgets.QWidget, BaseHeater.Ui_Form):
    data = {}

    def __init__(self, parent=None):
        super(Heater, self).__init__(parent)
        self.setupUi(self)

        self.heater_number_input.setValidator(QIntValidator(1, 20, self.heater_number_input))

        self.heater_number_input.textChanged[str].connect(self.heaterNumber)
        self.okButton.clicked.connect(self.okbutton)
        self.cancelButton.clicked.connect(self.cancelbutton)

        self.burner_oxygen_percent_spinbox.valueChanged.connect(self.burner_oxygen_percent_spinbox_changed)
        self.burner_fluegas_spinbox.valueChanged.connect(self.burner_fluegas_spinbox_changed)

    def burner_fluegas_spinbox_changed(self):
        if self.heater_number_input.text() == "":
            QMessageBox.about(self, "خطا در اطلاعات ورودی", "ابتدا باید تعداد گرمکن را مشخص نمایید!")
            return
        else:
            self.data.setdefault(self.heater_number_comboBox.currentText(), {})
            self.data[self.heater_number_comboBox.currentText()].setdefault(self.burner_number_comboBox.currentText(),
                                                                            {})
            self.data[self.heater_number_comboBox.currentText()][self.burner_number_comboBox.currentText()].setdefault(
                "fluegas", [])
            self.data[self.heater_number_comboBox.currentText()][self.burner_number_comboBox.currentText()]["fluegas"] = \
                float(self.burner_fluegas_spinbox.text())
            # print(self.data)
        return

    def burner_oxygen_percent_spinbox_changed(self):
        if self.heater_number_input.text() == "":
            QMessageBox.about(self, "خطا در اطلاعات ورودی", "ابتدا باید تعداد گرمکن را مشخص نمایید!")
            return
        else:
            self.data.setdefault(self.heater_number_comboBox.currentText(), {})
            self.data[self.heater_number_comboBox.currentText()].setdefault(self.burner_number_comboBox.currentText(),
                                                                            {})
            self.data[self.heater_number_comboBox.currentText()][self.burner_number_comboBox.currentText()].setdefault(
                "oxygen", [])
            self.data[self.heater_number_comboBox.currentText()][self.burner_number_comboBox.currentText()]["oxygen"] = \
                float(self.burner_oxygen_percent_spinbox.text())
            # print(self.data)
        return

    def heaterNumber(self):
        self.heater_number_comboBox.clear()
        if self.heater_number_input.text() == "":
            return
        number = int(self.heater_number_input.text())
        item = []
        for i in range(1, number + 1):
            item.append(str(i))

        self.heater_number_comboBox.addItems(item)
        return

    def okbutton(self):
        if self.heater_number_input.text() == "":
            QMessageBox.about(self, "خطا در اطلاعات ورودی", "تعداد گرم کن مشخص نشده است")
            return
        elif self.burner_fluegas_spinbox.text() == "":
            QMessageBox.about(self, "خطا در اطلاعات ورودی", "دمای دودکش مشخص نشده است")
            return
        elif self.burner_oxygen_percent_spinbox.text() == "":
            QMessageBox.about(self, "خطا در اطلاعات ورودی", "درصد اکسیژن وارد نشده است")
            return
        else:
            self.data.setdefault(self.heater_number_comboBox.currentText(), {})
            self.data[self.heater_number_comboBox.currentText()].setdefault(self.burner_number_comboBox.currentText(),
                                                                            {})
            self.data[self.heater_number_comboBox.currentText()][self.burner_number_comboBox.currentText()].setdefault(
                "fluegas", [])
            self.data[self.heater_number_comboBox.currentText()][self.burner_number_comboBox.currentText()]["fluegas"] = \
                float(self.burner_fluegas_spinbox.text())
            self.data.setdefault(self.heater_number_comboBox.currentText(), {})
            self.data[self.heater_number_comboBox.currentText()].setdefault(self.burner_number_comboBox.currentText(),
                                                                            {})
            self.data[self.heater_number_comboBox.currentText()][self.burner_number_comboBox.currentText()].setdefault(
                "oxygen", [])
            self.data[self.heater_number_comboBox.currentText()][self.burner_number_comboBox.currentText()]["oxygen"] = \
                float(self.burner_oxygen_percent_spinbox.text())

        print(self.data)
        self.close()
        pass

    def cancelbutton(self):
        self.close()
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Heater()
    ui.show()
    sys.exit(app.exec_())
