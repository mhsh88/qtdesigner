from PyQt5 import QtCore

from behinesazan.gas.station.software.view.PipeLine.PipeLine import PipeLine


class BaseAfterHeaterLine(PipeLine):
    def __init__(self, parent=None):
        super(BaseAfterHeaterLine, self).__init__(parent)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "اطلاعات خط لوله گاز خروجی از گرم کن"))
        pass


    pass



