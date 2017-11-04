from behinesazan.gas.station.software.model.Combustion.Combustion import Combustion
from behinesazan.gas.station.software.model.HeatLoss.PipeLineEndDefined.PipeLineEndDefinedHeatLoss import PipeLineEnd
from behinesazan.gas.station.software.model.HeatLoss.PipeLineHeadDefined.PipeLineHeadDefinedHeatLoss import PipeLineHead
from behinesazan.gas.station.software.model.Logic.calculation.combustionCalculation.CombustionCalculation import \
    CombustionCalculation
from behinesazan.gas.station.software.model.Logic.calculation.heatloss.afterHeaterHeatLoss.AfterHeaterHeatLoss import \
    AfterHeaterHeatLoss
from behinesazan.gas.station.software.model.Logic.calculation.heatloss.beforeHeaterHeatLoss.BeforeHeaterHeatLoss import \
    BeforeHeaterHeatLoss
from behinesazan.gas.station.software.model.Logic.calculation.heatloss.runHeatloss.RunHeatLoss import RunHeatLoss
from behinesazan.gas.station.software.model.Logic.calculation.noHeatloss.NoHeatLossConsumption import \
    NoHeatLossConsumption
from behinesazan.gas.station.software.model.Regulator.Regulator import Regulator


class Calculation:
    result = {}
    result.setdefault("heat_loss", {})

    def __init__(self):
        return

    @staticmethod
    def calculate(gasInformationFormInputData, beforeHeaterLineData, heaterData, afterHeaterLineData, runData):
        # try:
        Calculation.noHeatLossConsumption = NoHeatLossConsumption(gasInformationFormInputData)

        # check if heater data form is defined and air temperature is defined in Gas information form input data
        CombustionCalculation.combustionCal(heaterData, gasInformationFormInputData)

        runHeatLoss = RunHeatLoss(runData, gasInformationFormInputData,
                                  Calculation.noHeatLossConsumption.T_before_regulator)

        afterHeaterHeatLossWithInsulation = AfterHeaterHeatLoss(afterHeaterLineData, gasInformationFormInputData,
                                                                runHeatLoss.T_before_run)
        afterHeaterHeatLossWithoutInsulation = AfterHeaterHeatLoss(afterHeaterLineData, gasInformationFormInputData,
                                                                   runHeatLoss.T_before_run)

        beforeHeaterHeatLossWithInsulation = BeforeHeaterHeatLoss(beforeHeaterLineData, gasInformationFormInputData)
        beforeHeaterHeatLossWithoutInsulation = BeforeHeaterHeatLoss(beforeHeaterLineData, gasInformationFormInputData)


        print(Calculation.result)

        Calculation.__energy_Consumption_with_insulation(Calculation.result, gasInformationFormInputData, beforeHeaterLineData,
                                         afterHeaterLineData, runData)
        Calculation.__energy_Consumption_without_insulation(Calculation.result, gasInformationFormInputData,
                                                         beforeHeaterLineData,
                                                         afterHeaterLineData, runData)
        return Calculation.result

    @classmethod
    def __gasConsumptionCal(cls, P, T, gasInformationFormInputData):
        gasInformationFormInputData["gas"].calculate(gasInformationFormInputData["P_input"],
                                                     result["T_before_heater"])
        H1 = gasInformationFormInputData["gas"].H
        gasInformationFormInputData["gas"].calculate(gasInformationFormInputData["P_input"], result["T_after_heater"])
        H2 = gasInformationFormInputData["gas"].H
        tempHHV = Combustion(gasInformationFormInputData["gas"], 2, 15, 200)
        HHV = tempHHV.HHVd
        Q_with_heat_loss = Calculation.__capacityCal(gasInformationFormInputData["P_input"],
                                                     gasInformationFormInputData["T_input"],
                                                     gasInformationFormInputData["gas"],
                                                     H1,
                                                     H2,
                                                     HHV,
                                                     gasInformationFormInputData["Station_Capacity"])
        pass

    @staticmethod
    def __capacityCal(P, T, g, H1, H2, HHV, Q_standard):

        g.calculate(g.p_theta, g.T_theta)
        P2 = g.P
        Z2 = g.Z
        T2 = g.T
        Dstd = g.D
        g.calculate(P, T)
        P1 = g.P
        Z1 = g.Z
        T1 = g.T

        Qdot = (Q_standard / 3600) * (P2 * Z1 * T1) / (P1 * Z2 * T2)
        # Q1Heater = Qdot * g.D * (H2 - H1) / HHV * 3600
        Q1Heater = Qdot * g.D * (H2 - H1) / HHV * 3600
        Q1Heater = Q1Heater / Dstd
        return Q1Heater



    @classmethod
    def __energy_Consumption_with_insulation(cls, result, gasInformationFormInputData, beforeHeaterLineData, afterHeaterLineData,
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

        gasInformationFormInputData["gas"].calculate(gasInformationFormInputData["P_input"],
                                                     result["T_before_heater"])
        H1 = gasInformationFormInputData["gas"].H
        gasInformationFormInputData["gas"].calculate(gasInformationFormInputData["P_input"], result["T_after_heater"])
        H2 = gasInformationFormInputData["gas"].H
        tempHHV = Combustion(gasInformationFormInputData["gas"], 2, 15, 200)
        HHV = tempHHV.HHVd
        Q_with_heat_loss = Calculation.__capacityCal(gasInformationFormInputData["P_input"],
                                                     gasInformationFormInputData["T_input"],
                                                     gasInformationFormInputData["gas"],
                                                     H1,
                                                     H2,
                                                     HHV,
                                                     gasInformationFormInputData["Station_Capacity"])
        print("Q with heat loss", Q_with_heat_loss)

        pass

    @classmethod
    def __energy_Consumption_without_insulation(cls, result, gasInformationFormInputData, beforeHeaterLineData,
                                             afterHeaterLineData,
                                             runData):
        if "heat_loss" in result.keys():
            if "After_Heater_Pipeline_without_insulation" in result["heat_loss"].keys():
                result["T_after_heater_without_insulation"] = result["heat_loss"]["After_Heater_Pipeline_without_insulation"].Tout
            elif "T_before_run" in result.keys():
                result["T_after_heater_without_insulation"] = result["T_before_run"]
            elif "T_before_regulator" in result.keys():
                result["T_after_heater_without_insulation"] = result["T_before_regulator"]
            else:
                print("something wrong gonna happen there is no data for after heater temperature")
                pass
            if "Before_Heater_Pipeline_without_insulation" in result["heat_loss"].keys():
                result["T_before_heater_without_insulation"] = result["heat_loss"]["Before_Heater_Pipeline_without_insulation"].Tout
            elif "T_input" in gasInformationFormInputData.keys():
                result["T_before_heater_without_insulation"] = gasInformationFormInputData["T_input"]
            else:
                print("there is no data for before heater temperature please check the inputs")
                pass
        else:
            result["T_after_heater_without_insulation"] = result["T_before_regulator"]
            result["T_before_heater_without_insulation"] = gasInformationFormInputData["T_input"]
            print("there is no data for heat loss so default data will be used")

        gasInformationFormInputData["gas"].calculate(gasInformationFormInputData["P_input"],
                                                     result["T_before_heater_without_insulation"])
        H1 = gasInformationFormInputData["gas"].H
        gasInformationFormInputData["gas"].calculate(gasInformationFormInputData["P_input"], result["T_after_heater_without_insulation"])
        H2 = gasInformationFormInputData["gas"].H
        tempHHV = Combustion(gasInformationFormInputData["gas"], 2, 15, 200)
        HHV = tempHHV.HHVd
        Q_without_heat_loss = Calculation.__capacityCal(gasInformationFormInputData["P_input"],
                                                     result["T_before_heater_without_insulation"],
                                                     gasInformationFormInputData["gas"],
                                                     H1,
                                                     H2,
                                                     HHV,
                                                     gasInformationFormInputData["Station_Capacity"])
        print("Q without heat loss", Q_without_heat_loss)

        pass


if __name__ == "__main__":
    pass
