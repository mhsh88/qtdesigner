from behinesazan.gas.station.software.model.Combustion.Combustion import Combustion
from behinesazan.gas.station.software.model.Regulator.Regulator import Regulator


class Calculation:

    def __init__(self):

        return

    def calculate(self, data):
        try:
            tempHHV = Combustion(data["gas"], 2, 15, 200)
            HHV = tempHHV.HHVd
            regulator = Regulator(data["P_input"], data["T_station_out"], data["P_station_out"], data["gas"])
            tBeforeRegulator = regulator.Tin
            data["gas"].calculate(data["P_input"], data["T_input"])
            H1 = data["gas"].H
            data["gas"].calculate(data["P_input"], tBeforeRegulator)
            H2 = data["gas"].H
            print("this is calculate method in Calculation")
            print(data)
            print(H1 - H2)
            print(tBeforeRegulator)
        except Exception as e:
            print(e)

        return
