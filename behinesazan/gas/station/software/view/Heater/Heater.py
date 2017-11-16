from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QListView
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
        self.clearButton.clicked.connect(self.data.clear)

        self.burner_oxygen_percent_spinbox.valueChanged.connect(self.burner_spinbox_changed)
        self.burner_fluegas_spinbox.valueChanged.connect(self.burner_spinbox_changed)

        # combo_font = QFont("Arial", 12, -1, True)
        # vw = QListView()
        # vw.setFont(combo_font)
        # self.burner_oxygen_percent_spinbox.setView(vw)
        # self.burner_fluegas_spinbox.setView(vw)

    def burner_spinbox_changed(self):
        if self.heater_number_input.text() == "":
            QMessageBox.about(self, "خطا در اطلاعات ورودی", "ابتدا باید تعداد گرمکن را مشخص نمایید!")
            return
        else:
            if self.burner_oxygen_percent_spinbox.text() == "":
                self.burner_oxygen_percent_spinbox.setValue(0)

            if self.burner_fluegas_spinbox.text() == "":
                self.burner_fluegas_spinbox.setValue(0)

            self.data.setdefault(self.heater_number_comboBox.currentText(), {})
            self.data[self.heater_number_comboBox.currentText()].setdefault(self.burner_number_comboBox.currentText(),
                                                                            {})
            self.data[self.heater_number_comboBox.currentText()][self.burner_number_comboBox.currentText()].setdefault(
                "oxygen", [])
            self.data[self.heater_number_comboBox.currentText()][self.burner_number_comboBox.currentText()]["oxygen"] = \
                float(self.enToArNumb(self.burner_oxygen_percent_spinbox.text()))
            self.data.setdefault(self.heater_number_comboBox.currentText(), {})
            self.data[self.heater_number_comboBox.currentText()].setdefault(self.burner_number_comboBox.currentText(),
                                                                            {})
            self.data[self.heater_number_comboBox.currentText()][self.burner_number_comboBox.currentText()].setdefault(
                "fluegas", [])
            self.data[self.heater_number_comboBox.currentText()][self.burner_number_comboBox.currentText()]["fluegas"] = \
                float(self.enToArNumb(self.burner_fluegas_spinbox.text()))
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
                float(self.enToArNumb(self.burner_fluegas_spinbox.text()))
            self.data.setdefault(self.heater_number_comboBox.currentText(), {})
            self.data[self.heater_number_comboBox.currentText()].setdefault(self.burner_number_comboBox.currentText(),
                                                                            {})
            self.data[self.heater_number_comboBox.currentText()][self.burner_number_comboBox.currentText()].setdefault(
                "oxygen", [])
            self.data[self.heater_number_comboBox.currentText()][self.burner_number_comboBox.currentText()]["oxygen"] = \
                float(self.enToArNumb(self.burner_oxygen_percent_spinbox.text()))

        print(self.data)
        self.close()
        pass

    def cancelbutton(self):
        self.close()
        pass

    def enToArNumb(self, number):
        print(number)
        dic = {
            ',': '.',
            '۱': '1',
            '۲': '2',
            '۰': '0',
            '١': '1',
            '٢': '2',
            '۳': '3',
            '۴': '4',
            '۵': '5',
            '۶': '6',
            '۷': '7',
            '۸': '8',
            '۹': '9',
            '٫': '.',
            '0': '0',
            '1': '1',
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            '8': '8',
            '9': '9',
            '.': '.',
        }
        temp = [dic.get(num) for num in number]
        print(temp)
        return ''.join(temp)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Heater()
    ui.show()
    sys.exit(app.exec_())
