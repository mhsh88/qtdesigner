from PyQt5 import QtWidgets

from behinesazan.gas.station.software.view.PipeLine.BeforeHeaterLine.base.BaseBeforeHeaterLine import BaseBeforeHeaterLine



class BeforeHeaterLine(BaseBeforeHeaterLine):

    pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = BeforeHeaterLine()
    ui.show()
    sys.exit(app.exec_())
