import sys
import traceback
# from pdfrw import PdfWriter, PdfReader
import pandas as pd
import fpdf.fpdf as fpdf

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from behinesazan.gas.station.software.view.Result.base import BaseResult


class Result(QtWidgets.QWidget, BaseResult.Ui_Form):
    def __init__(self, parent=None):
        super(Result, self).__init__(parent)
        self.setupUi(self)

        self.inputs = ""
        self.outputs = ""
        self.fileDialog = QFileDialog(self)

        self.export_button.clicked.connect(self.export_button_clicked)
        self.close_button.clicked.connect(self.close)

    def export_button_clicked(self):
        # self.fileDialog.getOpenFileNames(self, 'Multiple File',
        #                                  "Desktop",
        #                                  '*.xls')
        filePath = self.fileDialog.getSaveFileName(self, 'Choose File Type', '', '*.xls\n*.xlsx\n*.pdf')

        if filePath[1] == '*.xls' or filePath[1] == "*.xlsx":
            # Create a Pandas dataframe from the data.
            df = pd.DataFrame([self.inputs, self.outputs])

            # Create a Pandas Excel writer using XlsxWriter as the engine.
            writer = pd.ExcelWriter(filePath[0], engine='xlsxwriter')

            # Convert the dataframe to an XlsxWriter Excel object.
            df.to_excel(writer, sheet_name='Sheet1')

            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
        elif filePath[1] == '*.pdf':
            try:
                pdf = fpdf.FPDF(format='letter')
                # y = PdfWriter()
                # x = PdfReader('C:/Users/hossein.sharifi/Desktop/نرم افزار شبیه(1).pdf')
                # print(x)
                # y.addpage(x.pages[0])
                # y.write('result.pdf')
                pdf.add_page()
                pdf.set_font('Arial', 'B', 16)
                # os.path.join(request.folder, 'static', 'fonts/B Mitra.ttf')
                pdf.add_font('sysfont', '', r"c:\WINDOWS\Fonts\B Mitra.ttf", uni=True)
                txt = self.result_text.toPlainText()
                # utxt = str(txt, 'utf-8')
                # stxt = txt.encode('utf-8')  #
                # stxt = stxt.decode('utf-8')
                print(txt)
                pdf.cell(40, 10, txt)
                pdf.output(filePath[0], 'F')
            except Exception as exception:
                print(exception)
                print(traceback.format_exc())

        print(type(filePath))
        print(filePath)
        return


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        ui = Result()
        ui.show()

        sys.exit(app.exec_())
    except Exception as e:
        print(e)
        print(traceback.format_exc())
