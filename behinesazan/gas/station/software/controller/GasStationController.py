import sys
import traceback

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from behinesazan.gas.station.software.model.Logic.calculation.Calculation import Calculation
from behinesazan.gas.station.software.view.GasStation.GasStation import GasStation


class Calculate:  # (GasStation):
    # def __init__(self, parent=None):
    #     super(AfterHeaterLine, self).__init__(parent)

    # def __init__(self, parent=None):
    #     super(Calculate, self).__init__(parent)
    def __init__(self):
        # self.calculate = Calculation()
        self.station = GasStation()
        self.station.show()
        try:
            self.station.pushButton_22.clicked.connect(self.cal)
        except Exception as exception:
            print(exception)
            return
        pass

    def cal(self):
        if bool(self.station.gasInformationInputForm.data):
            try:
                result = Calculation.calculate(self.station.gasInformationInputForm.data, self.station.beforeHeaterLine.data,
                                     self.station.heater.data, self.station.afterHeaterLine.data, self.station.run.data)
                self.station.result.result_text.clear()
                # self.station.result.result_text.setPlainText("".join(result))
                self.station.result.setOutput(self.station.gasInformationInputForm.data , result)
                self.station.result.show()

            except Exception as e:
                print("saalm")
                print(e)
                print(traceback.format_exc())
                return
            print(self.station.gasInformationInputForm.data)
        else:
            try:
                QMessageBox.about(self.station, "خطا در اطلاعات ورودی", "لطفا اطلاعات گاز را کامل فرمایید.")
            except Exception as e:
                print(e)


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        ui = Calculate()
        # ui.show()
        # g = Gas()

        sys.exit(app.exec_())
    except Exception as e:
        print(e)
        sys.exit(app.exec_())
