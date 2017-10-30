from PyQt5 import QtWidgets
import sys

from PyQt5.QtWidgets import QMessageBox

from behinesazan.gas.station.software.model.gas.Gas import Gas
from behinesazan.gas.station.software.view.GasInformationInputForm.GasInformationInputForm import \
    GasInformationInputForm
from behinesazan.gas.station.software.view.GasStation.base import BaseGasStation
from behinesazan.gas.station.software.view.Heater.Heater import Heater
from behinesazan.gas.station.software.view.PipeLine.AfterHeaterLine.AfterHeaterLine import AfterHeaterLine
from behinesazan.gas.station.software.view.PipeLine.BeforeHeaterLine.BeforeHeaterLine import BeforeHeaterLine
from behinesazan.gas.station.software.view.Run.Run import Run


class GasStation(QtWidgets.QMainWindow, BaseGasStation.Ui_MainWindow):
    def __init__(self, parent=None):
        super(GasStation, self).__init__(parent)
        self.heater = Heater()
        self.beforeHeaterLine = BeforeHeaterLine()
        self.afterHeaterLine = AfterHeaterLine()
        self.run = Run()
        self.gasInformationInputForm = GasInformationInputForm()
        self.setupUi(self)
        self.initiateButtonIcon()
        self.buttonConnection()

    def buttonConnection(self):

        self.pushButton_21.clicked.connect(self.afterHeaterShow)
        self.pushButton_3.clicked.connect(self.beforeHeaterShow)
        self.pushButton_2.clicked.connect(self.heaterShow)
        self.pushButton_4.clicked.connect(self.runShow)
        self.pushButton_6.clicked.connect(self.runShow)
        self.pushButton_5.clicked.connect(self.runShow)
        self.pushButton_16.clicked.connect(self.runShow)
        self.pushButton_17.clicked.connect(self.runShow)
        self.pushButton.clicked.connect(self.runShow)
        self.pushButton_10.clicked.connect(self.runShow)
        self.pushButton_8.clicked.connect(self.runShow)
        self.pushButton_9.clicked.connect(self.runShow)
        self.pushButton_7.clicked.connect(self.runShow)
        self.pushButton_11.clicked.connect(self.runShow)
        self.pushButton_12.clicked.connect(self.runShow)
        self.pushButton_26.clicked.connect(self.runShow)
        self.pushButton_24.clicked.connect(self.runShow)
        self.pushButton_28.clicked.connect(self.runShow)
        self.pushButton_15.clicked.connect(self.gasInformationInputFormShow)


    def afterHeaterShow(self):
        self.afterHeaterLine.close()
        self.afterHeaterLine.show()
        return

    def beforeHeaterShow(self):
        self.beforeHeaterLine.close()
        self.beforeHeaterLine.show()
        return

    def heaterShow(self):
        self.heater.close()
        self.heater.show()
        return

    def runShow(self):
        self.run.close()
        self.run.show()
        return

    def gasInformationInputFormShow(self):
        self.gasInformationInputForm.close()
        self.gasInformationInputForm.show()
        return

        # self.pushButton_22.clicked.connect(self.inlineCal)

    def initiateButtonIcon(self):
        # self.pushButton_2.iconIn = ":/icon/heater05.svg"
        self.pushButton_2.iconIn = ":/icon/heaterred.svg"
        self.pushButton_2.iconOut = ":/icon/heater.svg"
        self.pushButton_2.iconPressed = ":/icon/heaterred.svg"
        self.pushButton_3.iconIn = ":/icon/pipeGageRed.svg"
        self.pushButton_3.iconOut = ":/icon/pipeGage.svg"
        self.pushButton_3.iconPressed = ":/icon/pipeGagePressed.svg"
        self.pushButton_21.iconIn = ":/icon/pipeGageRed.svg"
        self.pushButton_21.iconOut = ":/icon/pipeGage.svg"
        self.pushButton_21.iconPressed = ":/icon/pipeGagePressed.svg"
        self.pushButton_4.iconIn = ":/icon/4way/4way2red.svg"
        self.pushButton_4.iconOut = ":/icon/4way/4way2.svg"
        self.pushButton_4.iconPressed = ":/icon/4way/4way2red.svg"
        self.pushButton_11.iconIn = ":/icon/4way/4wayred.svg"
        self.pushButton_11.iconOut = ":/icon/4way/4way.svg"
        self.pushButton_11.iconPressed = ":/icon/4way/4wayred.svg"
        self.pushButton_5.iconIn = ":/icon/znway/newknee3red.svg"
        self.pushButton_5.iconOut = ":/icon/znway/newknee3.svg"
        self.pushButton_5.iconPressed = ":/icon/znway/newknee3red.svg"
        self.pushButton_6.iconIn = ":/icon/znway/newknee1red.svg"
        self.pushButton_6.iconOut = ":/icon/znway/newknee1.svg"
        self.pushButton_6.iconPressed = ":/icon/znway/newknee1red.svg"
        self.pushButton_7.iconIn = ":/icon/znway/newknee2red.svg"
        self.pushButton_7.iconOut = ":/icon/znway/newknee2.svg"
        self.pushButton_7.iconPressed = ":/icon/znway/newknee2red.svg"
        self.pushButton_12.iconIn = ":/icon/znway/newknee4red.svg"
        self.pushButton_12.iconOut = ":/icon/znway/newknee4.svg"
        self.pushButton_12.iconPressed = ":/icon/znway/newknee4red.svg"
        self.pushButton_14.iconIn = ":/icon/pipeGageRed.svg"
        self.pushButton_14.iconOut = ":/icon/pipeGage.svg"
        self.pushButton_14.iconPressed = ":/icon/pipeGagePressed.svg"
        self.pushButton_16.iconIn = ":/icon/pipeRed.svg"
        self.pushButton_16.iconOut = ":/icon/pipe.svg"
        self.pushButton_16.iconPressed = ":/icon/pipeRed.svg"
        # self.pushButton_18.iconIn = ":/icon/pipeRed.svg"
        # self.pushButton_18.iconOut = ":/icon/pipe.svg"
        # self.pushButton_18.iconPressed = ":/icon/pipeRed.svg"
        self.pushButton_17.iconIn = ":/icon/pipeRed.svg"
        self.pushButton_17.iconOut = ":/icon/pipe.svg"
        self.pushButton_17.iconPressed = ":/icon/pipeRed.svg"
        self.pushButton.iconIn = ":/icon/pipeRed.svg"
        self.pushButton.iconOut = ":/icon/pipe.svg"
        self.pushButton.iconPressed = ":/icon/pipeRed.svg"
        # self.pushButton_20.iconIn = ":/icon/pipeRed.svg"
        # self.pushButton_20.iconOut = ":/icon/pipe.svg"
        # self.pushButton_20.iconPressed = ":/icon/pipeRed.svg"
        # self.pushButton_19.iconIn = ":/icon/pipeRed.svg"
        # self.pushButton_19.iconOut = ":/icon/pipe.svg"
        # self.pushButton_19.iconPressed = ":/icon/pipeRed.svg"
        self.pushButton_10.iconIn = ":/icon/valveRed.svg"
        self.pushButton_10.iconOut = ":/icon/valve.svg"
        self.pushButton_10.iconPressed = ":/icon/valveRed.svg"
        self.pushButton_8.iconIn = ":/icon/valveRed.svg"
        self.pushButton_8.iconOut = ":/icon/valve.svg"
        self.pushButton_8.iconPressed = ":/icon/valveRed.svg"
        self.pushButton_9.iconIn = ":/icon/valveRed.svg"
        self.pushButton_9.iconOut = ":/icon/valve.svg"
        self.pushButton_9.iconPressed = ":/icon/valveRed.svg"
        self.pushButton_15.iconIn = ":/icon/GasinIcon2.svg"
        self.pushButton_15.iconOut = ":/icon/GasIcon2.svg"
        self.pushButton_15.iconPressed = ":/icon/GasinIcon2.svg"
        self.pushButton_22.iconIn = ":/icon/calculateinIcon.svg"
        self.pushButton_22.iconOut = ":/icon/calculateIcon.svg"
        self.pushButton_26.iconIn = ":/icon/regulator/05red.svg"
        self.pushButton_26.iconOut = ":/icon/regulator/05.svg"
        self.pushButton_24.iconIn = ":/icon/regulator/05red.svg"
        self.pushButton_24.iconOut = ":/icon/regulator/05.svg"
        self.pushButton_28.iconIn = ":/icon/regulator/05red.svg"
        self.pushButton_28.iconOut = ":/icon/regulator/05.svg"

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "برای خروج از نرم افزار اطمینان دارید؟", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.gasInformationInputForm.close()
            self.run.close()
            self.heater.close()
            self.afterHeaterLine.close()
            self.beforeHeaterLine.close()

            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = GasStation()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    g = Gas()
    ui.show()

    sys.exit(app.exec_())
