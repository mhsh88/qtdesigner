from PyQt5 import QtWidgets

from view.PipeLine.AfterHeaterLine.base.BaseAfterHeaterLine import BaseAfterHeaterLine


class AfterHeaterLine(BaseAfterHeaterLine):

    # def __init__(self, parent=None):
    #     super(AfterHeaterLine, self).__init__(parent)
    pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = AfterHeaterLine()
    ui.show()
    sys.exit(app.exec_())