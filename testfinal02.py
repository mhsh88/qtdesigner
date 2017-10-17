from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
# import numpy as np
# from scipy.optimize import fsolve
import math
# from PyQt5.QtWidgets import QPushButton
# from PyQt5.QtCore import pyqtSignal
# from PyQt5.QtGui import *
# from PyQt5.QtCore import pyqtSlot
# from numbers import Number
# from decimal import Decimal
# from GasLineCalTest import Reynolds
from QpipeLine import PipeLine
from QpipeLineEnd import PipeLineEnd
import inputlineWidget
import inputHeater
import OutputlineWidget
import Runs
import MainGasWindow
import OutputStation
import GasProperty
from AgaQt import Gas
from Regulator import Regulator
from Cumbustion import Combustion
from final03 import MainStationWindow


class Main(MainStationWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)


import svgfile_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = MainStationWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    g = Gas()
    ui.show()

    sys.exit(app.exec_())
