from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainterPath, QGradient

import inputlineWidget

class inputWindow(QtWidgets.QWidget, inputlineWidget.Ui_Form):
    def __init__(self, parent = None):
        super(inputWindow, self).__init__(parent)
        self.setupUi(self)





app = QApplication(sys.argv)

form = inputWindow()
form.show()
app.exec_()