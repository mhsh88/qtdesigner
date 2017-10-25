import sys, os
import numpy
from behinesazan.gas.station.software.model.Combustion.Combustion import Combustion
from behinesazan.gas.station.software.model.HeatLoss.PipeLineHeatLoss import PipeLineHeatLoss
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
        regulator = Regulator(gasInformationFormInputData["P_input"], gasInformationFormInputData["T_station_out"],
                              gasInformationFormInputData["P_station_out"], gasInformationFormInputData["gas"])
        tBeforeRegulator = regulator.Tin
        gasInformationFormInputData["gas"].calculate(gasInformationFormInputData["P_input"],
                                                     gasInformationFormInputData["T_input"])
        H1 = gasInformationFormInputData["gas"].H
        gasInformationFormInputData["gas"].calculate(gasInformationFormInputData["P_input"], tBeforeRegulator)
        H2 = gasInformationFormInputData["gas"].H

        Calculation.result["T_before_regulator"] = tBeforeRegulator

        # check if Station Capacity is entered to calculation amount of energy needed

        if "Station_Capacity" in gasInformationFormInputData.keys():
            Calculation.result["Q_Heater"] = Calculation.__capacityCal(gasInformationFormInputData, H1, H2, HHV)

        # check if heater data form is defined and air temperature is defined in Gas information form input data

        if bool(heaterData) and "T_environment" in gasInformationFormInputData.keys():
            Calculation.__combustionCal(heaterData, gasInformationFormInputData)
            # Combustion(g, , ui.outTemperature, ui.TflueGas1)
            pass

        if bool(runData) and bool(
                afterHeaterLineData) and 'Wind_velocity' in gasInformationFormInputData.keys() and "T_environment" in gasInformationFormInputData.keys():
            Calculation.__heatTransferLossCal(runData, afterHeaterLineData, gasInformationFormInputData)
            pass
        # if ui.runCheck and ui.afterHeaterCheck and ui.windCheck and ui.toutCheck:

        # ui.heaterCheck and ui.toutCheck:
        # # print('Check')
        # mashal1 = Combustion(g, ui.O2Mashal1, ui.outTemperature, ui.TflueGas1)



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

    @classmethod
    def __combustionCal(cls, heaterData, gasInformationFormInputData):
        Calculation.result.setdefault('heater', {})

        for keys in heaterData:
            Calculation.result["heater"].setdefault(keys, {})
            for key in heaterData[keys]:
                Calculation.result["heater"][keys].setdefault(key, None)
                Calculation.result["heater"][keys][key] = Combustion(gasInformationFormInputData["gas"],
                                                                     heaterData[keys][key]["oxygen"],
                                                                     gasInformationFormInputData["T_environment"],
                                                                     heaterData[keys][key]["fluegas"])
                print("efficiency: ", "heater ", keys, " burner ", key, Calculation.result["heater"][keys][key].eff)
                # print("efficiency: ", Calculation.result["heater"][keys][key].eff)
                # print(heaterData[keys][key])

        # print(heaterData)
        #

        # Combustion(gasInformationFormInputData["gas"], ui.O2Mashal1, ui.outTemperature, ui.TflueGas1)

        pass

    @classmethod
    def __heatTransferLossCal(cls, runData, afterHeaterLineData, gasInformationFormInputData):
        print(runData['run_debi'])
        for key in runData["run_debi"].keys():
            Calculation.result["run_heat_loss"][key] = PipeLineHeatLoss(gasInformationFormInputData["T_environment"],
                                                                        gasInformationFormInputData["Wind_velocity"],
                                                                        Calculation.result["T_before_regulator"],
                                                                        gasInformationFormInputData["T_input"],
                                                                        gasInformationFormInputData["P_input"],
                                                                        gasInformationFormInputData["gas"],
                                                                        runData["OD"],
                                                                        runData["length"],
                                                                        runData["run_debi"][key])
            print(Calculation.result["run_heat_loss"][key].Tout)
            pass
        print(Calculation.result)

        print(runData, afterHeaterLineData, gasInformationFormInputData)
        # heatloss = PipeLineHeatLoss(gasInformationFormInputData["T_environment"], gasInformationFormInputData["Wind_velocity"],
        #                             Calculation.result["T_before_regulator"], gasInformationFormInputData["P_input"],
        #                             gasInformationFormInputData["gas"], runData[])
        # PipeLineEnd(ui.outTemperature, ui.windVelocity, self.tBeforeRegulator, ui.Pin, g,
        #             ui.runOD, ui.runID,
        #             ui.runWidth / 2 + ui.runLength, ui.Run1debi)
        pass


if __name__ == "__main__":
    pass
