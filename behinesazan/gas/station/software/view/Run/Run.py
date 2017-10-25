from PyQt5 import QtWidgets
import sys

from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QMessageBox

from behinesazan.gas.station.software.view.Run.base import BaseRun


class Run(QtWidgets.QWidget, BaseRun.Ui_Form):
    data = {}
    debi_dict = {}

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
        super(Run, self).__init__(parent)
        self.setupUi(self)
        self.initialization()

    def initialization(self):

        self.run_length_input.setPlaceholderText("ex: 20")
        self.debi_input.setPlaceholderText("20000 m3/hr")
        self.run_width_input.setPlaceholderText("ex: 5")



        self.debi_input.textChanged.connect(self.debi_input_textChange)


        # set validator input for run length and debi and width input

        validator = QDoubleValidator(0, 999, 2, self.run_length_input)
        validator.setNotation(QDoubleValidator.StandardNotation)
        self.run_length_input.setValidator(validator)


        run_width_validator = QDoubleValidator(0, 999, 2, self.run_width_input)
        run_width_validator.setNotation(QDoubleValidator.StandardNotation)
        self.run_width_input.setValidator(run_width_validator)

        debi_input_validator = QDoubleValidator(0, 9999999, 2, self.debi_input)
        debi_input_validator.setNotation(QDoubleValidator.StandardNotation)
        self.debi_input.setValidator(debi_input_validator)


        self.label_4.setVisible(False)

        self.okButton.clicked.connect(self.datagather)
        self.cancelButton.clicked.connect(self.cancel)

        self.mm_radioButton.toggled.connect(self.radiomm)
        self.inch_radioButton.toggled.connect(self.radioinch)

        self.nominal_diameter_comboBox.activated[str].connect(self.changecombobox2)
        self.outer_diameter_comboBox.activated[str].connect(self.changecombobox3)

        if self.mm_radioButton.isChecked():
            self.nominal_diameter_comboBox.clear()
            self.nominal_diameter_comboBox.addItems(sorted(self.linemmDimension.keys()))

        elif self.inch_radioButton.isChecked():
            self.nominal_diameter_comboBox.clear()
            self.nominal_diameter_comboBox.addItems(sorted(self.lineinchDimension.keys()))

            #     QMessageBox.about(self, "radiobutton", "radio button is checked")
            #     pass
            # elif self.radioButton_2.isChecked():
            #     QMessageBox.about(self, "radiobutton2", "radio button2 is checked")
            #     pass

    def debi_input_textChange(self):
        self.debi_dict[self.run_number_comboBox.currentText()] = self.debi_input.text()

    def changecombobox2(self):
        self.thickness_comboBox.clear()
        if self.mm_radioButton.isChecked():
            self.outer_diameter_comboBox.clear()
            self.outer_diameter_comboBox.addItems(sorted(self.linemmDimension[self.nominal_diameter_comboBox.currentText()].keys()))
        elif self.inch_radioButton.isChecked():
            self.outer_diameter_comboBox.clear()
            self.outer_diameter_comboBox.addItems(sorted(self.lineinchDimension[self.nominal_diameter_comboBox.currentText()].keys()))
        return

    def changecombobox3(self):
        if self.mm_radioButton.isChecked():
            self.thickness_comboBox.clear()
            self.thickness_comboBox.addItems(
                sorted(self.linemmDimension[self.nominal_diameter_comboBox.currentText()][self.outer_diameter_comboBox.currentText()]))
        elif self.inch_radioButton.isChecked():
            self.thickness_comboBox.clear()
            self.thickness_comboBox.addItems(
                sorted(self.lineinchDimension[self.nominal_diameter_comboBox.currentText()][self.outer_diameter_comboBox.currentText()]))

        return

    def radiomm(self):
        try:
            self.nominal_diameter_comboBox.clear()
            self.outer_diameter_comboBox.clear()
            self.thickness_comboBox.clear()
            self.nominal_diameter_comboBox.addItems(sorted(self.linemmDimension.keys()))
        except:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(sys.exc_info()[2])
            return

        return

    def radioinch(self):
        try:
            # print(self.linemmDimension.keys())
            self.nominal_diameter_comboBox.clear()
            self.outer_diameter_comboBox.clear()
            self.thickness_comboBox.clear()
            self.nominal_diameter_comboBox.addItems(sorted(self.lineinchDimension.keys()))
        except:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(sys.exc_info()[2])
            return
        return

    def datagather(self):
        self.inputCheck = False

        try:
            if float(self.run_length_input.text()) <= 0 or self.run_length_input.text() == "" or self.run_width_input.text() == "" or self.debi_input.text() == "":

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
                self.run_number = int(self.run_number_comboBox.currentText())
                self.run_width = float(self.run_width_input.text())
                self.inputlineLength = float(self.run_length_input.text())


                if self.mm_radioButton.isChecked():
                    self.inputlineOD = float(self.outer_diameter_comboBox.currentText()) * 0.001
                    self.inputlineID = self.inputlineOD - 2 * (float(self.thickness_comboBox.currentText()) * 0.001)

                elif self.inch_radioButton.isChecked():
                    self.inputlineOD = float(self.outer_diameter_comboBox.currentText()) * 25.4 * 0.001
                    self.inputlineID = self.inputlineOD - 2 * (float(self.outer_diameter_comboBox.currentText()) * 25.4 * 0.001)

                self.label_4.setVisible(False)
                self.inputCheck = True


                self.data["length"] = self.inputlineLength
                self.data["ID"] = self.inputlineID
                self.data["OD"] = self.inputlineOD
                self.data["number"] = self.run_number
                self.data["width"] = self.run_width
                print(self.debi_dict)
                self.data['run_debi'] = {}

                # self.data.setdefault("run_debi", {})
                self.data['run_debi'] = self.debi_dict
                # self.data["run_debi"] = self.debi_dict
                print(self.data['run_debi'])
                # self.data = {**self.data, **self.debi_dict}
                # self.debi_dict.clear()
                print(self.data)
                self.close()






        except Exception:
            print(Exception)
            # print(sys.exc_info()[0] + " " + sys.exc_info()[1] + " " + sys.exc_info()[2])
            print(sys.exc_info()[0])
            print(sys.exc_info()[2])
            print(sys.exc_info()[2])
            self.inputCheck = False
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
    app = QtWidgets.QApplication(sys.argv)
    ui = Run()
    ui.show()
    sys.exit(app.exec_())
