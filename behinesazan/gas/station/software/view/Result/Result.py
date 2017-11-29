import sys
import traceback
# from pdfrw import PdfWriter, PdfReader
import pandas as pd
import fpdf.fpdf as fpdf

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from behinesazan.gas.station.software.view.Result.base import BaseResult
import re


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
        filePath = self.fileDialog.getSaveFileName(self, 'Choose File Type', '', '*.xls\n*.xlsx')

        if filePath[1] == '*.xls' or filePath[1] == "*.xlsx":
            # Create a Pandas dataframe from the data.
            try:
                df = df2 = pd.DataFrame(self.inputs)
                # df.stats = df2.stats.str.strip("[]").str.split("\n")
                # df.stats = df2.stats.str.strip("[]").str.split("\n")

                # Create a Pandas Excel writer using XlsxWriter as the engine.
                writer = pd.ExcelWriter(filePath[0], engine='xlsxwriter')

                # Convert the dataframe to an XlsxWriter Excel object.
                df.to_excel(writer, sheet_name='Sheet1')

                # Close the Pandas Excel writer and output the Excel file.
                writer.save()
            except Exception as exception:
                print(traceback.format_exc())
                return
        # elif filePath[1] == '*.pdf':
        #     try:
        #         pdf = fpdf.FPDF(format='letter')
        #         # y = PdfWriter()
        #         # x = PdfReader('C:/Users/hossein.sharifi/Desktop/نرم افزار شبیه(1).pdf')
        #         # print(x)
        #         # y.addpage(x.pages[0])
        #         # y.write('result.pdf')
        #         pdf.add_page()
        #         pdf.set_font('Arial', 'B', 16)
        #         # os.path.join(request.folder, 'static', 'fonts/B Mitra.ttf')
        #         pdf.add_font('sysfont', '', r"c:\WINDOWS\Fonts\B Mitra.ttf", uni=True)
        #         txt = self.result_text.toPlainText()
        #         # utxt = str(txt, 'utf-8')
        #         # stxt = txt.encode('utf-8')  #
        #         # stxt = stxt.decode('utf-8')
        #         print(txt)
        #         pdf.cell(40, 10, txt)
        #         pdf.output(filePath[0], 'F')
        #     except Exception as exception:
        #         print(exception)
        #         print(traceback.format_exc())
        #         return
        #
        # print(type(filePath))
        # print(filePath)
        return

    def setOutput(self, information, heaterdata, result):
        tempstring = ''
        excel_output = []
        excel_output.append(['استان', information['province']])
        excel_output.append(['شهر', information['city']])
        excel_output.append(['منطقه', information['area']])
        excel_output.append(['آدرس', information['address']])
        excel_output.append(['ظرفیت نامی', information['nominal_capacity']])

        replacements = ('\n', '=')
        infos = 'استان:\n'
        infos += '%s\n' % information['province']
        infos += 'شهر:\n'
        infos += '%s\n' % information['city']
        infos += 'منطقه:\n'
        infos += '%s\n' % information['area']
        infos += 'آدرس:\n'
        infos += '%s\n' % information['address']
        infos += 'ظرفیت نامی:\n'
        infos += '%s\n' % information['nominal_capacity']

        try:
            for key in result:
                if key == 'user':
                    user_string = 'محاسبات با دمای خروجی وارد شده\n\n'
                    excel_output.append([user_string, ''])
                    string = self.string_creator(result[key])
                    tempstring = string
                    for r in replacements:
                        tempstring = tempstring.replace(r, ',')
                    tempstring = tempstring.split(',')
                    for i in range((len(tempstring) // 2) * 2):
                        excel_output.append([tempstring[i], tempstring[i + 1]])

                    user_string += string
                    pass
                elif key == 'T_hydrate':
                    t_hydrate_string = '\nمحاسبات بر اساس دمای هیدرات محاسبه شده\n\n'
                    excel_output.append([t_hydrate_string, ''])
                    string = self.string_creator(result[key])
                    tempstring = string
                    for r in replacements:
                        tempstring = tempstring.replace(r, ',')
                    tempstring = tempstring.split(',')
                    for i in range((len(tempstring) // 2) * 2):
                        excel_output.append([tempstring[i], tempstring[i + 1]])
                    t_hydrate_string += string
                    pass
                elif key == 'T_hydrate_plus_2':
                    t_hydrateplus2_string = '\nمحاسبات بر اساس دما دمای هیدرات محاسبه شده به علاوه ۲ درجه\n\n'
                    excel_output.append([t_hydrateplus2_string, ''])
                    string = self.string_creator(result[key])
                    tempstring = string
                    for r in replacements:
                        tempstring = tempstring.replace(r, ',')
                    tempstring = tempstring.split(',')
                    for i in range((len(tempstring) // 2) * 2):
                        excel_output.append([tempstring[i], tempstring[i + 1]])
                    t_hydrateplus2_string += string
                    pass

            self.outputs = infos + user_string + t_hydrate_string + t_hydrateplus2_string
            self.inputs = excel_output
            # print(user_string + t_hydrate_string + t_hydrateplus2_string)
            self.result_text.setPlainText(self.outputs)

        except Exception as exception:
            print(traceback.format_exc())
            self.result_text.setPlainText(traceback.format_exc())

    def string_creator(self, result):
        string = ''
        for key in sorted(result.keys()):

            if 'دمای هیدرات' == key:
                string += 'دمای هیدرات در فشار خروجی = %s سلسیوس\n' % result['دمای هیدرات']
            elif key == 'راندمان جذب حرارتی کویل گرمکن' and result['راندمان جذب حرارتی کویل گرمکن'] != "":
                string += result['راندمان جذب حرارتی کویل گرمکن']
            elif 'دمای گاز قبل از رگولاتور' == key:
                string += 'دمای گاز قبل از رگولاتور = %s سلسیوس\n' % round(result['دمای گاز قبل از رگولاتور'][0], 3)
            elif 'بار حرارتی' == key:
                if result['بار حرارتی'] > 0:
                    string += 'بار حرارتی مورد نیاز = %s متر مکعب بر ساعت\n' % round(result['بار حرارتی'][0], 3)
            elif 'بار حرارتی بدون تلفات لوله' == key:
                if result['بار حرارتی بدون تلفات لوله'] > 0:
                    string += "بار حرارتی بدون تلفات خط لوله = %s متر مکعب بر ساعت \n" % round(result['بار حرارتی '
                                                                                                      'بدون تلفات '
                                                                                                      'لوله'][0], 3)
            elif 'راندمان مشعل' == key:
                print(result[key])
                for burner in result['راندمان مشعل']:
                    print(burner[1])
                    print(burner[0])
                    string += 'راندمان %s = %s \n' % (burner[0], round(burner[1], 3))
                pass

            elif 'تلفات حرارتی ران' == key:
                for runloss in result['تلفات حرارتی ران']:
                    string += '%s = %s متر مکعب بر ساعت\n' % (runloss[0], round(runloss[1], 3))
                pass

                pass

            elif 'تلفات خط لوله قبل از گرم کن' == key:
                if result['تلفات خط لوله قبل از گرم کن']:
                    if result['تلفات خط لوله قبل از گرم کن'][0] > 0 or result['تلفات خط لوله قبل از گرم کن'][0] < 0:
                        if result['تلفات خط لوله قبل از گرم کن'][0] == result['تلفات خط لوله قبل از گرم کن'][1]:
                            string += 'تلفات خط لوله قبل از گرم کن  = %s متر مکعب بر ساعت\n' % round(result['تلفات خط '
                                                                                                            'لوله قبل '
                                                                                                            'از گرم '
                                                                                                            'کن'][0][
                                                                                                         0], 3)
                        else:
                            string += 'تلفات خط لوله قبل از گرم کن بدون عایق  = %s متر مکعب بر ساعت\n' % round(
                                result['تلفات خط لوله قبل از گرم کن'][0][0], 3)
                            string += 'تلفات خط لوله قبل از گرم کن با عایق  = %s متر مکعب بر ساعت\n' % \
                                      round(result['تلفات خط لوله قبل از گرم کن'][1][0], 3)
                pass
            elif 'تلفات خط لوله بعد از گرم کن' == key:
                if result['تلفات خط لوله بعد از گرم کن']:
                    if result['تلفات خط لوله بعد از گرم کن'][0] > 0 or result['تلفات خط لوله بعد از گرم کن'][0] < 0:
                        if result['تلفات خط لوله بعد از گرم کن'][0] == result['تلفات خط لوله بعد از گرم کن'][1]:
                            string += 'تلفات خط لوله بعد از گرم کن  = %s متر مکعب بر ساعت \n' % round(result['تلفات خط '
                                                                                                             'لوله بعد'
                                                                                                             ' از گرم '
                                                                                                             'کن'][0][
                                                                                                          0], 3)
                        else:
                            string += 'تلفات خط لوله بعد از گرم کن بدون عایق  = %s متر مکعب بر ساعت\n' % round(
                                result['تلفات خط لوله بعد از گرم کن'][0][0], 3)
                            string += 'تلفات خط لوله قبل از گرم کن با عایق  = %s متر مکعب بر ساعت\n' % \
                                      round(result['تلفات خط لوله بعد از گرم کن'][1][0], 3)
                pass
            elif 'مصرف با راندمان محاسبه شده' == key:
                print(result['مصرف با راندمان محاسبه شده'])
                strng = ''
                if bool(result['مصرف با راندمان محاسبه شده']):
                    for heater in sorted(result['مصرف با راندمان محاسبه شده'].keys()):
                        for burner in sorted(result['مصرف با راندمان محاسبه شده'][heater].keys()):
                            if result['مصرف با راندمان محاسبه شده'][heater][burner] > 0:
                                strng += 'مصرف گاز مشعل %s از گرم کن %s = %s متر مکعب بر ساعت \n' % (
                                burner, heater, round(result['مصرف با راندمان محاسبه شده'][heater][burner][0], 3))

                string += strng
                pass
            elif 'درصد صرفه جویی عایق' == key:
                if result['درصد صرفه جویی عایق'] > 0.0 or result['درصد صرفه جویی عایق'] < 0.0:
                    string += 'درصد صرفه جویی عایق = %s\n' % (round(result['درصد صرفه جویی عایق'][0], 3))
                pass
            elif 'مصرف هیتر با راندمان ۸۰ درصد' == key:
                if result['مصرف هیتر با راندمان ۸۰ درصد'] > 0.0 or result['مصرف هیتر با راندمان ۸۰ درصد'] < 0.0:
                    string += 'مصرف گاز با راندمان ۸۰ درصد = %s متر مکعب بر ساعت\n' % round(result['مصرف هیتر با '
                                                                                                   'راندمان ۸۰ '
                                                                                                   'درصد'][0], 3)
                pass

        return string


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        ui = Result()
        ui.show()

        sys.exit(app.exec_())
    except Exception as e:
        print(e)
        print(traceback.format_exc())
