from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import *



class HoverButton(QPushButton):
    iconIn = ""
    iconOut = ""
    iconPressed = ""

    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)
        self.setMouseTracking(True)
        self.setStyleSheet("QPushButton{\n"
                           "background-color:transparent;\n"
                           " \n"
                           "\n"
                           "}\n"
                           )
        # self.isCheckable()

    def enterEvent(self, event):
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(self.iconIn), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.setIcon(icon)

    def leaveEvent(self, event):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.iconOut), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setIcon(icon)


