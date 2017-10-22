from PyQt5 import QtWidgets
import sys

from behinesazan.gas.station.software.model.gas.Gas import Gas
from behinesazan.gas.station.software.view.GasStation.base import BaseGasStation


class GasStation(QtWidgets.QMainWindow, BaseGasStation.Ui_MainWindow):
    def __init__(self, parent=None):
        super(GasStation, self).__init__(parent)
        self.setupUi(self)
        self.initiateButtonIcon()
        
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

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = GasStation()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    g = Gas()
    ui.show()

    sys.exit(app.exec_())