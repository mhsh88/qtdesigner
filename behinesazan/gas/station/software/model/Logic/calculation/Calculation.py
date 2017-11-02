from behinesazan.gas.station.software.model.Combustion.Combustion import Combustion
from behinesazan.gas.station.software.model.HeatLoss.PipeLineEndDefined.PipeLineEndDefinedHeatLoss import PipeLineEnd
from behinesazan.gas.station.software.model.HeatLoss.PipeLineHeadDefined.PipeLineHeadDefinedHeatLoss import PipeLineHead
from behinesazan.gas.station.software.model.Regulator.Regulator import Regulator


class Calculation:
    result = {}
    result.setdefault("heat_loss", {})

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

        # for temporary calculation
        gasInformationFormInputData["gas"].calculate(gasInformationFormInputData["P_station_out"],
                                                     gasInformationFormInputData["T_station_out"])
        print("this is print in calculate method of Calculation class T hydrate is ",
              gasInformationFormInputData["gas"].T_h, " at ", gasInformationFormInputData["gas"].P / 6.89476, "psi")

        # check if Station Capacity is entered to calculation amount of energy needed

        if "Station_Capacity" in gasInformationFormInputData.keys():
            Calculation.result["Q_Heater"] = Calculation.__capacityCal(gasInformationFormInputData, H1, H2, HHV)

        # check if heater data form is defined and air temperature is defined in Gas information form input data

        if bool(heaterData) and "T_environment" in gasInformationFormInputData.keys():
            Calculation.__combustionCal(heaterData, gasInformationFormInputData)
            # Combustion(g, , ui.outTemperature, ui.TflueGas1)
            pass

        if bool(runData) and bool(
                afterHeaterLineData) and 'Wind_velocity' in gasInformationFormInputData.keys() and \
                        "T_environment" in gasInformationFormInputData.keys() and \
                        "Station_Capacity" in gasInformationFormInputData.keys():
            Calculation.result["T_before_run"] = Calculation.__runHeatTransferLossCal(runData, afterHeaterLineData,
                                                                                      gasInformationFormInputData)
            pass

        # TODO if the velocity is null the wind velocity is 0.5 and the further method must be added

        if bool(afterHeaterLineData) and "Wind_velocity" in gasInformationFormInputData.keys() and \
                        "T_environment" in gasInformationFormInputData.keys():
            Calculation.__beforeHeaterHeatLossCal(beforeHeaterLineData, gasInformationFormInputData)
            pass

        print(Calculation.result)

        Calculation.__energy_Consumption(Calculation.result, gasInformationFormInputData, beforeHeaterLineData,
                                         afterHeaterLineData, runData)
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

                # print("efficiency: ", "heater ", keys, " burner ", key, Calculation.result["heater"][keys][key].eff)

        pass

    @classmethod
    def __runHeatTransferLossCal(cls, runData, afterHeaterLineData, gasInformationFormInputData):
        # print(runData['run_debi'])
        Calculation.result.setdefault("heat_loss", {})
        Calculation.result["heat_loss"].setdefault("run", {})
        t_max = 0
        for key in runData["run_debi"].keys():
            Calculation.result["heat_loss"]["run"][key] = PipeLineEnd(gasInformationFormInputData["T_environment"],
                                                               gasInformationFormInputData["Wind_velocity"],
                                                               # as Tin
                                                               Calculation.result["T_before_regulator"],
                                                               gasInformationFormInputData["P_input"],
                                                               gasInformationFormInputData["gas"],
                                                               runData["OD"],
                                                               runData["ID"],
                                                               runData["length"],
                                                               runData["run_debi"][key], 0, 0)

            t_max = max(t_max, Calculation.result["heat_loss"]["run"][key].Tout)
        Calculation.result["heat_loss"]["After_Heater_Pipeline"] = PipeLineEnd(
            gasInformationFormInputData["T_environment"],
            gasInformationFormInputData["Wind_velocity"],
            # as Tin
            t_max,
            gasInformationFormInputData["P_input"],
            gasInformationFormInputData["gas"],
            afterHeaterLineData["OD"],
            afterHeaterLineData["ID"],
            afterHeaterLineData["length"],
            gasInformationFormInputData["Station_Capacity"],
            afterHeaterLineData["insulation_thickness"],
            afterHeaterLineData["thermal_conductivity"])
        return t_max
        # print(Calculation.result["heat_loss"]["After_Heater_Pipeline"].Tout)

        # print(Calculation.result)

    @classmethod
    def __beforeHeaterHeatLossCal(cls, beforeHeaterLineData, gasInformationFormInputData):
        # print(gasInformationFormInputData["T_input"])
        Calculation.result["heat_loss"]["Before_Heater_Pipeline"] = PipeLineHead(
            gasInformationFormInputData["T_environment"],
            gasInformationFormInputData["Wind_velocity"],
            gasInformationFormInputData["T_input"],
            gasInformationFormInputData["P_input"],
            gasInformationFormInputData["gas"],
            beforeHeaterLineData["OD"],
            beforeHeaterLineData["ID"],
            beforeHeaterLineData["length"],
            gasInformationFormInputData[
                "Station_Capacity"],
            beforeHeaterLineData["insulation_thickness"],
            beforeHeaterLineData["thermal_conductivity"])  # TODO it must be checked for Station capacity and runs flows
        pipeline_without_insulation = PipeLineHead(
            gasInformationFormInputData["T_environment"],
            gasInformationFormInputData["Wind_velocity"],
            gasInformationFormInputData["T_input"],
            gasInformationFormInputData["P_input"],
            gasInformationFormInputData["gas"],
            beforeHeaterLineData["OD"],
            beforeHeaterLineData["ID"],
            beforeHeaterLineData["length"],
            gasInformationFormInputData[
                "Station_Capacity"],
            0,
            0)

        print("Pipe line with insulation is ", Calculation.result["heat_loss"]["Before_Heater_Pipeline"].Tout,
              "\nand Pipe "
              "line "
              "without "
              "insulation "
              "T out is "
              "",
              pipeline_without_insulation.Tout)

        pass

    @classmethod
    def __energy_Consumption(cls, result, gasInformationFormInputData, beforeHeaterLineData, afterHeaterLineData,
                             runData):
        if "heat_loss" in result.keys():
            if "After_Heater_Pipeline" in result["heat_loss"].keys():
                result["T_after_heater"] = result["heat_loss"]["After_Heater_Pipeline"].Tout
            elif "T_before_run" in result.keys():
                result["T_after_heater"] = result["T_before_run"]
            elif "T_before_regulator" in result.keys():
                result["T_after_heater"] = result["T_before_regulator"]
            else:
                print("something wrong gonna happen there is no data for after heater temperature")
                pass
            if "Before_Heater_Pipeline" in result["heat_loss"].keys():
                result["T_before_heater"] = result["heat_loss"]["Before_Heater_Pipeline"].Tout
            elif "T_input" in gasInformationFormInputData.keys():
                result["T_before_heater"] = gasInformationFormInputData["T_input"]
            else:
                print("there is no data for before heater temperature please check the inputs")
                pass
        else:
            result["T_after_heater"] = result["T_before_regulator"]
            result["T_before_heater"] = gasInformationFormInputData["T_input"]
            print("there is no data for heat loss so default data will be used")

        pass


if __name__ == "__main__":
    pass
