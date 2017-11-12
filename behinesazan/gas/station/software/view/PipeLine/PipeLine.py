from PyQt5 import QtWidgets
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QMessageBox

from behinesazan.gas.station.software.view.PipeLine.base import BasePipeLine


class PipeLine(QtWidgets.QWidget, BasePipeLine.Ui_Form):
    data = {}

    lineinchDimension = {'1 1/4"': {'1.66': ['0.065', '0.109', '0.14', '0.191', '0.25', '0.382']}, '12"': {
        '12.75': ['0.156', '0.18', '0.25', '0.33', '0.375', '0.406', '0.5', '0.562', '0.688', '0.844', '1.0', '1.125',
                  '1.312']}, '18"': {
        '18.0': ['0.188', '0.25', '0.312', '0.375', '0.438', '0.5', '0.562', '0.75', '0.938', '1.156', '1.375', '1.562',
                 '1.781']}, '36"': {'36.0': ['0.312', '0.375', '0.5']},
                         '3 1/2"': {'4.0': ['0.083', '0.12', '0.226', '0.318', '0.636']},
                         '2"': {'2.375': ['0.065', '0.109', '0.154', '0.218', '0.344', '0.436']},
                         '3/8"': {'0.675': ['0.065', '0.091', '0.126']}, '1/4"': {'0.54': ['0.065', '0.088', '0.119']},
                         '2 1/2"': {'2.875': ['0.083', '0.12', '0.203', '0.276', '0.375', '0.552']},
                         '5"': {'5.563': ['0.109'], '5.63': ['0.134', '0.258', '0.375', '0.5', '0.625', '0.75']},
                         '3"': {'3.5': ['0.083', '0.12', '0.216', '0.3', '0.438', '0.6']}, '10"': {
            '10.75': ['0.134', '0.165', '0.25', '0.307', '0.365', '0.5', '0.594', '0.719', '0.844', '1.0', '1.25']},
                         '4"': {'4.5': ['0.083', '0.12', '0.237', '0.337', '0.438', '0.531', '0.374']},
                         '6"': {'6.625': ['0.109', '0.134', '0.28', '0.432', '0.562', '0.719', '0.864']},
                         '1 1/2"': {'1.9': ['0.065', '0.109', '0.145', '0.2', '0.281', '0.4']}, '8"': {
            '8.625': ['0.109', '0.148', '0.25', '0.277', '0.322', '0.406', '0.5', '0.594', '0.719', '0.812', '0.875',
                      '0.906']}, '1/2"': {'0.84': ['0.065', '0.083', '0.109', '0.147', '0.188', '0.294']}, '24"': {
            '24.0': ['0.25', '0.375', '0.5', '0.562', '0.688', '0.969', '1.219', '1.531', '1.812', '2.062', '2.344']},
                         '1"': {'1.315': ['0.065', '0.011', '0.133', '0.179', '0.25', '0.358']}, '14"': {
            '14.0': ['0.188', '0.25', '0.312', '0.375', '0.438', '0.5', '0.594', '0.75', '0.938', '1.094', '1.25',
                     '1.406']}, '30"': {'30.0': ['0.361', '0.375', '0.5', '0.625']}, '16"': {
            '16.0': ['0.188', '0.25', '0.312', '0.375', '0.5', '0.656', '0.844', '1.031', '1.219', '1.438', '1.594']},
                         '1/8"': {'0.405': ['0.049', '0.068', '0.095']}, '20"': {
            '20.0': ['0.218', '0.25', '0.375', '0.5', '0.594', '0.812', '1.031', '1.281', '1.5', '1.75', '1.969']},
                         '3/4"': {'1.05': ['0.065', '0.083', '0.113', '0.154', '0.219', '0.308']}}
    linemmDimension = {'40.0': {'48.26': ['1.65', '2.77', '3.68', '5.08', '7.14', '10.16']}, '500.0': {
        '508.0': ['5.54', '6.35', '9.53', '12.7', '15.09', '20.62', '26.19', '32.54', '38.1', '44.45', '50.01']},
                       '350.0': {'355.6': ['4.78', '6.35', '7.92', '9.53', '11.13', '12.7', '15.09', '19.05', '23.83',
                                           '27.79', '31.75', '35.71']},
                       '750.0': {'762.0': ['7.92', '9.53', '12.7', '15.88']}, '400.0': {
            '406.4': ['4.78', '6.35', '7.92', '9.53', '12.7', '16.66', '21.44', '26.2', '30.96', '36.53', '40.49']},
                       '900.0': {'914.4': ['7.92', '9.53', '12.7']},
                       '10.0': {'17.15': ['1.65', '3.2'], '21.34': ['1.65']}, '300.0': {
            '323.85': ['3.96', '4.57', '6.35', '8.38', '9.53', '10.31', '12.7', '14.27', '17.48', '21.44', '25.4',
                       '28.58', '33.32']},
                       '125.0': {'143.0': ['3.4', '6.55', '9.53', '12.7', '15.88', '19.05'], '141.3': ['2.77']},
                       '600.0': {'609.6': ['6.35', '9.53', '12.7', '14.27', '17.48', '24.61', '30.96', '38.89', '46.02',
                                           '52.37', '59.54']},
                       '90.0': {'101.6': ['2.11', '3.05', '5.74', '8.08', '16.15']}, '200.0': {
            '219.08': ['2.77', '3.76', '6.35', '7.04', '8.18', '10.31', '12.7', '15.09', '18.26', '20.62', '22.23',
                       '23.01']}, '80.0': {'88.9': ['2.11', '3.05', '5.49', '7.62', '11.13', '15.24']},
                       '20.0': {'26.67': ['1.65', '2.11', '2.87', '3.91', '5.56', '7.82']},
                       '15.0': {'21.34': ['2.11', '2.77', '3.73', '4.78', '7.47']},
                       '32.0': {'42.16': ['1.65', '2.77', '3.56', '4.85', '6.35', '9.7']},
                       '8.0': {'13.72': ['2.24', '3.02'], '17.15': ['2.31']},
                       '6.0': {'13.72': ['1.65'], '10.29': ['1.24', '1.73', '2.41']},
                       '50.0': {'60.33': ['1.65', '2.77', '3.91', '5.54', '8.74', '11.07']},
                       '100.0': {'114.3': ['2.11', '3.05', '6.02', '8.56', '11.13', '13.49', '17.12']}, '250.0': {
            '273.05': ['3.4', '4.19', '6.35', '7.8', '9.27', '12.7', '15.09', '18.26', '21.44', '25.4', '28.58']},
                       '25.0': {'33.4': ['1.65', '2.77', '3.38', '4.55', '6.35', '9.09']},
                       '65.0': {'73.03': ['2.11', '3.05', '5.16', '7.01', '9.53', '14.02']},
                       '150.0': {'168.28': ['2.77', '3.4', '7.11', '10.97', '14.27', '18.26', '21.95']}, '450.0': {
            '457.2': ['4.78', '6.35', '7.92', '9.53', '11.13', '12.7', '14.27', '19.05', '23.83', '29.36', '34.93',
                      '39.67', '45.24']}}

    def __init__(self, parent=None):
        super(PipeLine, self).__init__(parent)
        self.setupUi(self)

        self.data = {}
        self.lineEdit.setPlaceholderText("ex: 20")

        # self.thermal_conductivity_label.setFixedSize(self.thermal_conductivity_label.width(),
        #                                              self.thermal_conductivity_label.height())
        # self.setFixedSize(self.width(), self.height())

        validator = QDoubleValidator(0, 999, 2, self.lineEdit)
        validator.setNotation(QDoubleValidator.StandardNotation)
        self.lineEdit.setValidator(validator)

        insulation_validator = QDoubleValidator(0, 99, 2, self.insulation_input)
        insulation_validator.setNotation(QDoubleValidator.StandardNotation)
        self.insulation_input.setValidator(insulation_validator)

        thermal_conductivity_validator = QDoubleValidator(0, 9999, 2, self.thermal_conductivity_input)
        thermal_conductivity_validator.setNotation(QDoubleValidator.StandardNotation)
        self.thermal_conductivity_input.setValidator(thermal_conductivity_validator)

        self.label_4.setVisible(False)

        self.pushButton_2.clicked.connect(self.datagather)
        self.pushButton.clicked.connect(self.cancel)
        self.clearButton.clicked.connect(self.data.clear)
        self.clearButton.clicked.connect(self.insolation_radioButton.setChecked)

        self.radioButton.toggled.connect(self.radiomm)
        self.radioButton_2.toggled.connect(self.radioinch)
        self.insolation_radioButton.toggled.connect(self.insolation_activation)
        if self.insolation_radioButton.isChecked():
            self.insolation_label.setEnabled(True)
            self.insulation_input.setEnabled(True)
            self.thermal_conductivity_label(True)
            self.thermal_conductivity_input(True)
        else:
            self.insolation_label.setEnabled(False)
            self.insulation_input.setEnabled(False)
            self.thermal_conductivity_label.setEnabled(False)
            self.thermal_conductivity_input.setEnabled(False)

        self.comboBox.activated[str].connect(self.changecombobox2)
        self.comboBox_2.activated[str].connect(self.changecombobox3)

        if self.radioButton.isChecked():
            self.comboBox.clear()
            self.comboBox.addItems(sorted(self.linemmDimension.keys()))

        elif self.radioButton_2.isChecked():
            self.comboBox.clear()
            self.comboBox.addItems(sorted(self.lineinchDimension.keys()))

            #     QMessageBox.about(self, "radiobutton", "radio button is checked")
            #     pass
            # elif self.radioButton_2.isChecked():
            #     QMessageBox.about(self, "radiobutton2", "radio button2 is checked")
            #     pass

    def insolation_activation(self):
        if self.insolation_radioButton.isChecked():
            self.insolation_label.setEnabled(True)
            self.insulation_input.setEnabled(True)
            self.thermal_conductivity_label.setEnabled(True)
            self.thermal_conductivity_input.setEnabled(True)
            self.thermal_conductivity_input.clear()
            self.insulation_input.clear()
        else:
            self.insolation_label.setEnabled(False)
            self.insulation_input.setEnabled(False)
            self.thermal_conductivity_label.setEnabled(False)
            self.thermal_conductivity_input.setEnabled(False)
            self.thermal_conductivity_input.clear()
            self.insulation_input.clear()

    def changecombobox2(self):
        self.comboBox_3.clear()
        if self.radioButton.isChecked():
            self.comboBox_2.clear()
            self.comboBox_2.addItems(sorted(self.linemmDimension[self.comboBox.currentText()].keys()))
        elif self.radioButton_2.isChecked():
            self.comboBox_2.clear()
            self.comboBox_2.addItems(sorted(self.lineinchDimension[self.comboBox.currentText()].keys()))
        return

    def changecombobox3(self):
        if self.radioButton.isChecked():
            self.comboBox_3.clear()
            self.comboBox_3.addItems(
                sorted(self.linemmDimension[self.comboBox.currentText()][self.comboBox_2.currentText()]))
        elif self.radioButton_2.isChecked():
            self.comboBox_3.clear()
            self.comboBox_3.addItems(
                sorted(self.lineinchDimension[self.comboBox.currentText()][self.comboBox_2.currentText()]))

        return

    def radiomm(self):
        try:
            self.comboBox.clear()
            self.comboBox_2.clear()
            self.comboBox_3.clear()
            self.comboBox.addItems(sorted(self.linemmDimension.keys()))
        except:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(sys.exc_info()[2])
            return

        return

    def radioinch(self):
        try:
            # print(self.linemmDimension.keys())
            self.comboBox.clear()
            self.comboBox_2.clear()
            self.comboBox_3.clear()
            self.comboBox.addItems(sorted(self.lineinchDimension.keys()))
        except:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(sys.exc_info()[2])
            return
        return

    def datagather(self):
        self.inputCheck = False

        # if not self.insolation_radioButton.isChecked():
        #     if ""
        #     pass


        try:
            if float(self.lineEdit.text()) <= 0 or self.lineEdit.text() == "" or \
                    (self.insolation_radioButton.isChecked() and (self.thermal_conductivity_input.text() == "" or
                             self.insulation_input.text() == "")):

                # float(self.lineEdit.text()) <= 0 or float(self.lineEdit_2.text()) * 0.01 <= 0 or float(
                # self.lineEdit_3.text()) * 0.01 <= 0 or float(self.lineEdit_3.text()) * 0.01 >= float(
                # self.lineEdit_2.text()) * 0.01 / 2:
                self.label_4.setVisible(True)
                # self.label_5.setVisible(True)
                # self.label_6.setVisible(True)
                QMessageBox.about(self, "خطا در اطلاعات ورودی", "لطفاً اطلاعات صحیح وارد فرمایید")
                return

            else:
                self.data.clear()

                self.inputlineLength = float(self.lineEdit.text())
                if self.radioButton.isChecked():
                    self.inputlineOD = float(self.comboBox_2.currentText()) * 0.001
                    self.inputlineID = self.inputlineOD - 2 * (float(self.comboBox_3.currentText()) * 0.001)

                elif self.radioButton_2.isChecked():
                    self.inputlineOD = float(self.comboBox_2.currentText()) * 25.4 * 0.001
                    self.inputlineID = self.inputlineOD - 2 * (float(self.comboBox_3.currentText()) * 25.4 * 0.001)

                if self.insolation_radioButton.isChecked():
                    self.data["thermal_conductivity"] = round(float(self.thermal_conductivity_input.text()), 3)
                    self.data["insulation_thickness"] = round(float(self.insulation_input.text()), 3)/100 # to cm
                else:
                    self.data["thermal_conductivity"] = 0
                    self.data["insulation_thickness"] = 0

                # self.inputlineOD = float(self.lineEdit_2.text()) * 0.01
                # self.inputlineID = self.inputlineOD - 2 * (float(self.lineEdit_3.text()) * 0.01)
                self.label_4.setVisible(False)
                # self.label_5.setVisible(False)
                # self.label_6.setVisible(False)
                # QMessageBox.about(self, " اطلاعات وارد شده", "شما اینها را وارد کرده اید\n %s \n %s \n %s \n %s \n %s" %(self.a, self.b, self.c, self.d, self.f))
                self.inputCheck = True
                self.close()

                self.data["length"] = self.inputlineLength
                self.data["ID"] = round(self.inputlineID, 6)
                self.data["OD"] = round(self.inputlineOD, 6)

                print(self.data)

                return





        except Exception as e:

            print(e)
            self.label_4.setVisible(True)
            # self.label_5.setVisible(True)
            # self.label_6.setVisible(True)
            QMessageBox.about(self, "خطا در اطلاعات ورودی", "لطفاً اطلاعات صحیح وارد فرمایید")
            return

    def cancel(self):
        self.data.clear()
        self.label_4.setVisible(False)
        # self.label_5.setVisible(False)
        # self.label_6.setVisible(False)
        self.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = PipeLine()
    ui.show()
    sys.exit(app.exec_())
