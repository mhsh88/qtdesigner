import sys

import math
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

from behinesazan.gas.station.software.view.GasInformationInputForm.base import BaseGasInformationInputForm
from behinesazan.gas.station.software.model.gas.Gas import Gas


# from behinesazan.gas.station.software.model.gas.Gas import Gas
# from AgaQt import Gas

class GasInformationInputForm(QtWidgets.QWidget, BaseGasInformationInputForm.Ui_Form):
    data = {}

    g = Gas()

    def __init__(self, parent=None):
        super(GasInformationInputForm, self).__init__(parent)
        self.setupUi(self)

        self.label_37.setVisible(False)
        self.label_38.setVisible(False)
        self.label_39.setVisible(False)
        self.label_40.setVisible(False)
        self.label_23.setVisible(False)
        self.address_input
        # TODO create clear button
        self.pushButton_2.clicked.connect(self.cancel)
        self.pushButton.clicked.connect(self.datagather)
        self.clear_button.clicked.connect(self.data.clear)

    # def clear_btn_clicked(self):
    #     self.data.clear()
        # self.address_input.clear()
        # self.province_input.clear()
        # self.city_input.clear()
        # self.area_input.clear()
        # self.station_nominal_capacity.clear()
        # self.lineEdit_25.clear()
        # self.lineEdit_24.clear()
        # self.lineEdit_26.clear()
        # self.lineEdit_27.clear()
        # self.lineEdit_28.clear()
        # self.lineEdit_30.clear()
        # self.lineEdit_31.clear()
        #
        # self.lineEdit.clear()
        # self.lineEdit_2.clear()
        # self.lineEdit_3.clear()
        # self.lineEdit_4.clear()
        # self.lineEdit_5.clear()
        # self.lineEdit_6.clear()
        # self.lineEdit_7.clear()
        # self.lineEdit_8.clear()
        # self.lineEdit_9.clear()
        # self.lineEdit_10.clear()
        # self.lineEdit_11.clear()
        # self.lineEdit_12.clear()
        # self.lineEdit_13.clear()
        # self.lineEdit_14.clear()
        # self.lineEdit_15.clear()
        # self.lineEdit_16.clear()
        # self.lineEdit_17.clear()
        # self.lineEdit_18.clear()
        # self.lineEdit_19.clear()
        # self.lineEdit_20.clear()
        # self.lineEdit_21.clear()

    def datagather(self):
        self.toutCheck = False
        self.windCheck = False
        self.humidityCheck = False
        self.stationCapacityCheck = False
        self.tStandard = 273.15
        self.data["T_Standard"] = 273.15 + 15
        self.pStandard = 101.325
        self.data["P_Standard"] = 101.325
        self.data["address"] = self.address_input.toPlainText()
        print(self.data['address'])
        self.data["province"] = self.province_input.text()
        self.data["city"] = self.city_input.text()
        self.data["nominal_capacity"] = self.station_nominal_capacity.text()

        try:
                # T in gas TEmperature

            if self.lineEdit_25.text() != "":
                try:
                    if float(self.lineEdit_25.text()) < -273.15:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "دمای گاز ورودی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                        self.label_37.setVisible(True)
                        self.label_23.setVisible(True)
                        return

                    else:
                        self.Tin = float(self.lineEdit_25.text()) + 273.15
                        self.data["T_input"] = self.Tin
                        self.label_37.setVisible(False)
                        self.label_23.setVisible(False)
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "دمای گاز ورودی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                    self.label_37.setVisible(True)
                    self.label_23.setVisible(True)
                    return


            else:
                self.label_37.setVisible(True)
                self.label_23.setVisible(True)




                # P in gas pressure

            if self.lineEdit_24.text() != "":
                try:
                    if float(self.lineEdit_24.text()) * 6.89476 + self.pStandard <= 0:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "فشار گاز ورودی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                        self.label_38.setVisible(True)
                        self.label_23.setVisible(True)
                        return

                    else:
                        self.Pin = float(self.lineEdit_24.text()) * 6.89476
                        self.data["P_input"] = self.Pin

                        self.label_38.setVisible(False)
                        self.label_23.setVisible(False)
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "فشار گاز ورودی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                    self.label_38.setVisible(True)
                    self.label_23.setVisible(True)
                    return


            else:
                self.label_38.setVisible(True)
                self.label_23.setVisible(True)

            # T out gas TEmperature

            if self.lineEdit_26.text() != "":
                try:
                    if float(self.lineEdit_26.text()) < -273.15:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "دمای گاز خروجی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                        self.label_39.setVisible(True)
                        self.label_23.setVisible(True)
                        return

                    else:
                        self.toutStation = float(self.lineEdit_26.text()) + 273.15

                        self.data["T_station_out"] = self.toutStation
                        self.label_39.setVisible(False)
                        self.label_23.setVisible(False)

                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "دمای گاز خروجی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                    self.label_39.setVisible(True)
                    self.label_23.setVisible(True)
                    return


            else:
                self.label_39.setVisible(True)
                self.label_23.setVisible(True)

            # P out gas pressure

            if self.lineEdit_27.text() != "":
                try:
                    if float(self.lineEdit_27.text()) * 6.89476 + self.pStandard <= 0:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "فشار گاز خروجی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                        self.label_40.setVisible(True)
                        self.label_23.setVisible(True)
                        return

                    else:
                        self.poutStation = float(self.lineEdit_27.text()) * 6.89476

                        self.data["P_station_out"] = self.poutStation

                        self.label_40.setVisible(False)
                        self.label_23.setVisible(False)
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "فشار گاز خروجی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                    self.label_40.setVisible(True)
                    self.label_23.setVisible(True)
                    return


            else:
                self.label_40.setVisible(True)
                self.label_23.setVisible(True)

            # جک کردن دمای محیط

            if self.lineEdit_28.text() != "":
                try:
                    if float(self.lineEdit_28.text()) < - 273.15:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "اطلاعات دمای محیط به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                        return
                    else:
                        self.outTemperature = float(self.lineEdit_28.text()) + 273.15
                        self.data["T_environment"] = self.outTemperature
                        self.toutCheck = True
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "اطلاعات دمای محیط به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                    return

                    # Humidity....

            # if self.lineEdit_29.text() != "": try: if float(self.lineEdit_29.text()) < 0 or float(
            # self.lineEdit_29.text()) > 100: QMessageBox.about(self, "خطا در اطلاعات ورودی", "رطوبت نسبی نمی تواند
            # کمتر از صفر یا بزرگتر از 100 درصد باشد. لطفاً اطلاعات صحیح وارد نمایید.")
            #
            #         else:
            #             self.humidity = float(self.lineEdit_29.text())
            #             self.humidityCheck = True
            #     except:
            #         QMessageBox.about(self, "خطا در اطلاعات ورودی",
            #                           "اطلاعات رطوبت نسبی به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")

            # Wind Velocity...

            if self.lineEdit_30.text() != "":
                try:
                    if float(self.lineEdit_30.text()) < 0:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "سرعت باد نمی تواند کوچکتر از صفر باشد. لطفاً اطلاعات صحیح وارد نمایید.")
                        return

                    else:
                        self.windVelocity = float(self.lineEdit_30.text())
                        if self.windVelocity < 0.5:
                            self.windVelocity = 0.5
                        self.data["Wind_velocity"] = self.windVelocity
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "اطلاعاتی صحبحی برای سرعت باد وارد نشده است. لطفاً اطلاعات صحیح وارد فرمایید")
                    return
            else:
                self.data["Wind_velocity"] = 0.5  # set wind velocity to 0.5 if nothing is entered

            # STation Capacity

            if self.lineEdit_31.text() != "":
                try:
                    if float(self.lineEdit_31.text()) <= 0:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "ظرفیت ایستگاه باید از صفر بزرگتر باشد. لطفاً اطلاعات صحیح وارد نمایید.")
                        return

                    else:
                        self.stationCapacity = float(self.lineEdit_31.text())
                        self.data["Station_Capacity"] = self.stationCapacity
                        self.stationCapacityCheck = True
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "ظرفیت ایستگاه به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                    return
            else:
                self.stationCapacity = 0
                self.data["Station_Capacity"] = self.stationCapacity


            if self.comboBox.currentText() == "درصد جرمی":
                print("جطوری؟") # TODO it must be modified
                pass

            self.g.component[0] = self.input_var_check(self.lineEdit.text())
            self.g.component[1] = self.input_var_check(self.lineEdit_2.text())
            self.g.component[2] = self.input_var_check(self.lineEdit_3.text())
            self.g.component[3] = self.input_var_check(self.lineEdit_4.text())
            self.g.component[4] = self.input_var_check(self.lineEdit_5.text())
            self.g.component[5] = self.input_var_check(self.lineEdit_6.text())
            self.g.component[6] = self.input_var_check(self.lineEdit_7.text())
            self.g.component[7] = self.input_var_check(self.lineEdit_8.text())
            self.g.component[8] = self.input_var_check(self.lineEdit_9.text())
            self.g.component[9] = self.input_var_check(self.lineEdit_10.text())
            self.g.component[10] = self.input_var_check(self.lineEdit_11.text())
            self.g.component[11] = self.input_var_check(self.lineEdit_12.text())
            self.g.component[12] = self.input_var_check(self.lineEdit_13.text())
            self.g.component[13] = self.input_var_check(self.lineEdit_14.text())
            self.g.component[14] = self.input_var_check(self.lineEdit_15.text())
            self.g.component[15] = self.input_var_check(self.lineEdit_16.text())
            self.g.component[16] = self.input_var_check(self.lineEdit_17.text())
            self.g.component[17] = self.input_var_check(self.lineEdit_18.text())
            self.g.component[18] = self.input_var_check(self.lineEdit_19.text())
            self.g.component[19] = self.input_var_check(self.lineEdit_20.text())
            self.g.component[20] = self.input_var_check(self.lineEdit_21.text())
            self.g.component = self.g.component / math.fsum(self.g.component)
            for comp in self.g.component:
                if comp < 0:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی", "لطفاً اطلاعات صحیح وارد فرمایید")
                    return
            self.data["gas"] = self.g

            if self.label_23.isVisible():
                return

            else:
                self.close()
                self.g.p_theta = self.pStandard
                self.g.T_theta = self.tStandard

                # print(self.toutStation, self.poutStation)



                # ui.pushButton_15.iconOut = ":/icon/GasdefIcon2.svg"
                # icon = QtGui.QIcon()
                # icon.addPixmap(QtGui.QPixmap(ui.pushButton_15.iconOut), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                # ui.pushButton_15.setIcon(icon)



                self.gasCheck = True
                # if 'Wind_velocity' in self.data.keys():
                #     print(self.data['Wind_velocity'])
                # else:
                #     print("it has not key")
                # try:
                #     print(self.data["Wind_velocity"])
                #
                # except KeyError:
                #     print(sys.exc_info()[0])
                #     print(sys.exc_info()[1])
                # except Exception:
                #     print("salam")


                print(self.data)






        except:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            self.label_37.setVisible(True)
            self.label_38.setVisible(True)
            self.label_39.setVisible(True)
            self.label_40.setVisible(True)
            self.label_23.setVisible(True)

            self.gasCheck = False
            QMessageBox.about(self, "خطا در اطلاعات ورودی", "لطفاً اطلاعات صحیح وارد فرمایید")

            return
    def input_var_check(self, text):
        if text =="":
            return 0
        return float(text)

    def cancel(self):
        self.label_37.setVisible(False)
        self.label_38.setVisible(False)
        self.label_39.setVisible(False)
        self.label_40.setVisible(False)
        self.label_23.setVisible(False)
        self.close()
        # self.gasProperty = None


        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = GasInformationInputForm()
    ui.show()
    sys.exit(app.exec_())
