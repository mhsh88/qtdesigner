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

        self.label_34.setVisible(False)
        self.label_33.setVisible(False)
        self.label_37.setVisible(False)
        self.label_38.setVisible(False)
        self.label_39.setVisible(False)
        self.label_40.setVisible(False)
        self.label_23.setVisible(False)
        # TODO create clear button
        self.pushButton_2.clicked.connect(self.cancel)
        self.pushButton.clicked.connect(self.datagather)

    def datagather(self):
        self.toutCheck = False
        self.windCheck = False
        self.humidityCheck = False
        self.stationCapacityCheck = False
        try:

            # T standard

            if self.lineEdit_23.text() != "":
                try:
                    if float(self.lineEdit_23.text()) < -273.15:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "لطفاً اطلاعات دمای استاندارد صحیح وارد نمایید.")
                        self.label_34.setVisible(True)
                        self.label_23.setVisible(True)
                        return

                    else:
                        self.tStandard = float(self.lineEdit_23.text()) + 273.15
                        self.data["T_Standard"] = self.tStandard
                        self.label_34.setVisible(False)
                        self.label_23.setVisible(False)
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "اطلاعات دما به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")
                    self.label_34.setVisible(True)
                    self.label_23.setVisible(True)
                    return

            else:
                self.label_34.setVisible(True)
                self.label_23.setVisible(True)

            # P Standard
            if self.lineEdit_22.text() != "":
                try:

                    if float(self.lineEdit_22.text()) <= 0:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "فشار گاز مطلق وارد کنید. فشار استاندارد گاز  باید از صفر بیشتر باشد. لطفاً "
                                          "اطلاعات صحیح وارد نمایید.")
                        self.label_33.setVisible(True)
                        self.label_23.setVisible(True)
                        return

                    else:
                        self.pStandard = float(self.lineEdit_22.text()) * 6.89476
                        self.data["P_Standard"] = self.pStandard

                        self.label_33.setVisible(False)
                        self.label_23.setVisible(False)

                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "اطلاعات فشار استاندارد گاز ورودی به درستی وارد نشده است. لطفاً اطلاعات صحیح "
                                      "وارد نمایید.")
                    self.label_33.setVisible(True)
                    self.label_23.setVisible(True)
                    return


            else:
                self.label_33.setVisible(True)
                self.label_23.setVisible(True)


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
                    else:
                        self.outTemperature = float(self.lineEdit_28.text()) + 273.15
                        self.data["T_environment"] = self.outTemperature
                        self.toutCheck = True
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "اطلاعات دمای محیط به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")

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

                    else:
                        self.windVelocity = float(self.lineEdit_30.text())
                        if self.windVelocity < 0.5:
                            self.windVelocity = 0.5
                        self.data["Wind_velocity"] = self.windVelocity
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "اطلاعاتی صحبحی برای سرعت باد وارد نشده است. لطفاً اطلاعات صحیح وارد فرمایید")
            else:
                self.data["Wind_velocity"] = 0.5  # set wind velocity to 0.5 if nothing is entered

            # STation Capacity

            if self.lineEdit_31.text() != "":
                try:
                    if float(self.lineEdit_31.text()) <= 0:
                        QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                          "ظرفیت ایستگاه باید از صفر بزرگتر باشد. لطفاً اطلاعات صحیح وارد نمایید.")

                    else:
                        self.stationCapacity = float(self.lineEdit_31.text())
                        self.data["Station_Capacity"] = self.stationCapacity
                        self.stationCapacityCheck = True
                except:
                    QMessageBox.about(self, "خطا در اطلاعات ورودی",
                                      "ظرفیت ایستگاه به درستی وارد نشده است. لطفاً اطلاعات صحیح وارد نمایید.")

            self.g.component[0] = float(self.lineEdit.text())
            self.g.component[1] = float(self.lineEdit_2.text())
            self.g.component[2] = float(self.lineEdit_3.text())
            self.g.component[3] = float(self.lineEdit_4.text())
            self.g.component[4] = float(self.lineEdit_5.text())
            self.g.component[5] = float(self.lineEdit_6.text())
            self.g.component[6] = float(self.lineEdit_7.text())
            self.g.component[7] = float(self.lineEdit_8.text())
            self.g.component[8] = float(self.lineEdit_9.text())
            self.g.component[9] = float(self.lineEdit_10.text())
            self.g.component[10] = float(self.lineEdit_11.text())
            self.g.component[11] = float(self.lineEdit_12.text())
            self.g.component[12] = float(self.lineEdit_13.text())
            self.g.component[13] = float(self.lineEdit_14.text())
            self.g.component[14] = float(self.lineEdit_15.text())
            self.g.component[15] = float(self.lineEdit_16.text())
            self.g.component[16] = float(self.lineEdit_17.text())
            self.g.component[17] = float(self.lineEdit_18.text())
            self.g.component[18] = float(self.lineEdit_19.text())
            self.g.component[19] = float(self.lineEdit_20.text())
            self.g.component[20] = float(self.lineEdit_21.text())
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
            self.label_34.setVisible(True)
            self.label_33.setVisible(True)
            self.label_37.setVisible(True)
            self.label_38.setVisible(True)
            self.label_39.setVisible(True)
            self.label_40.setVisible(True)
            self.label_23.setVisible(True)

            self.gasCheck = False
            QMessageBox.about(self, "خطا در اطلاعات ورودی", "لطفاً اطلاعات صحیح وارد فرمایید")

            return

    def cancel(self):
        self.label_34.setVisible(False)
        self.label_33.setVisible(False)
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
