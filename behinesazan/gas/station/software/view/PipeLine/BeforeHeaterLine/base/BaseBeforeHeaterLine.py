from PyQt5 import QtCore

from behinesazan.gas.station.software.view.PipeLine.PipeLine import PipeLine



class BaseBeforeHeaterLine(PipeLine):
    def __init__(self, parent=None):
        super(BaseBeforeHeaterLine, self).__init__(parent)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "اطلاعات خط لوله گاز ورودی به ایستگاه"))
        pass
    pass