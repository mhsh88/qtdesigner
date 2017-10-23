import sys, os
import numpy
from behinesazan.gas.station.software.model.Combustion.Combustion import Combustion
from behinesazan.gas.station.software.model.Regulator.Regulator import Regulator


class Calculation:
    result = {}
    def __init__(self):
        return
    @staticmethod
    def calculate(gasInformationFormInputData, beforeHeaterLineData, heaterData, afterHeaterLineData, runData):
        # try:
        tempHHV = Combustion(gasInformationFormInputData["gas"], 2, 15, 200)
        HHV = tempHHV.HHVd
        regulator = Regulator(gasInformationFormInputData["P_input"], gasInformationFormInputData["T_station_out"], gasInformationFormInputData["P_station_out"], gasInformationFormInputData["gas"])
        tBeforeRegulator = regulator.Tin
        gasInformationFormInputData["gas"].calculate(gasInformationFormInputData["P_input"], gasInformationFormInputData["T_input"])
        H1 = gasInformationFormInputData["gas"].H
        gasInformationFormInputData["gas"].calculate(gasInformationFormInputData["P_input"], tBeforeRegulator)
        H2 = gasInformationFormInputData["gas"].H
        if "Station_Capacity" in gasInformationFormInputData.keys():
            Calculation.result["Q_Heater"] = Calculation.__capacityCal(gasInformationFormInputData, H1, H2, HHV)
            if "Q_Heater" in Calculation.result.keys():
                print(Calculation.result["Q_Heater"])
            # print(gasInformationFormInputData["Station_Capacity"])
        # print("this is calculate method in Calculation")
        # print(gasInformationFormInputData)
        # print(H1 - H2)
        # print(tBeforeRegulator - 273.15)
        Calculation.result["T_before_regulator"] = tBeforeRegulator

        return

    @staticmethod
    def __capacityCal(data, H1, H2, HHV):
        g = data["gas"]
        g.calculate(g.p_theta, g.T_theta)
        P2 = g.P
        Z2 = g.Z
        T2 = g.T
        Dstd = g.D
        g.calculate(data["P_input"], data["T_input"])
        P1 = g.P
        Z1 = g.Z
        T1 = g.T

        Qdot = (data["Station_Capacity"] / 3600) * (P2 * Z1 * T1) / (P1 * Z2 * T2)
        # Q1Heater = Qdot * g.D * (H2 - H1) / HHV * 3600
        Q1Heater = Qdot * g.D * (H2 - H1) / HHV * 3600
        Q1Heater = Q1Heater / Dstd
        return Q1Heater


if __name__ == "__main__":
    pass
