from behinesazan.gas.station.software.model.Combustion.Combustion import Combustion
from behinesazan.gas.station.software.model.HeatLoss.PipeLineEndDefined.PipeLineEndDefinedHeatLoss import PipeLineEnd
from behinesazan.gas.station.software.model.HeatLoss.PipeLineHeadDefined.PipeLineHeadDefinedHeatLoss import PipeLineHead
from behinesazan.gas.station.software.model.Logic.calculation.capacityCalculation.CapacityCalculation import \
    CapacityCalculation
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
        combustionCalculation = CombustionCalculation()
        combustionCalculation.combustionCal(heaterData, gasInformationFormInputData)

        runHeatLoss = RunHeatLoss(runData, gasInformationFormInputData,
                                  Calculation.noHeatLossConsumption.T_before_regulator, Calculation.noHeatLossConsumption.HHV)

        afterHeaterHeatLoss = AfterHeaterHeatLoss(afterHeaterLineData, gasInformationFormInputData,
                                                                runHeatLoss.T_before_run)

        beforeHeaterHeatLoss = BeforeHeaterHeatLoss(beforeHeaterLineData, gasInformationFormInputData)


        consumption_without_heatloss = Calculation.noHeatLossConsumption.Q_heater

        capacity_calculation = CapacityCalculation()

        before_heater_heat_loss_without_insulation_consumption = \
            capacity_calculation.gasConsumptionCal(gasInformationFormInputData["P_input"],
                                                   gasInformationFormInputData["T_input"],
                                                   gasInformationFormInputData["P_input"],
                                                   beforeHeaterHeatLoss.T_out_without_insulation,
                                                   gasInformationFormInputData["gas"],
                                                   Calculation.noHeatLossConsumption.HHV,
                                                   gasInformationFormInputData["Station_Capacity"])
        before_heater_heat_loss_with_insulation_consumption = \
            capacity_calculation.gasConsumptionCal(gasInformationFormInputData["P_input"],
                                                   gasInformationFormInputData["T_input"],
                                                   gasInformationFormInputData["P_input"],
                                                   beforeHeaterHeatLoss.T_out_with_insulation,
                                                   gasInformationFormInputData["gas"],
                                                   Calculation.noHeatLossConsumption.HHV,
                                                   gasInformationFormInputData["Station_Capacity"])
        after_heater_heat_loss_without_insulation_consumption = \
            capacity_calculation.gasConsumptionCal(gasInformationFormInputData["P_input"],
                                                   afterHeaterHeatLoss.T_out_without_insulation,
                                                   gasInformationFormInputData["P_input"],
                                                   runHeatLoss.T_before_run,
                                                   gasInformationFormInputData["gas"],
                                                   Calculation.noHeatLossConsumption.HHV,
                                                   gasInformationFormInputData["Station_Capacity"])
        after_heater_heat_loss_with_insulation_consumption = \
            capacity_calculation.gasConsumptionCal(gasInformationFormInputData["P_input"],
                                                   afterHeaterHeatLoss.T_out_with_insulation,
                                                   gasInformationFormInputData["P_input"],
                                                   runHeatLoss.T_before_run,
                                                   gasInformationFormInputData["gas"],
                                                   Calculation.noHeatLossConsumption.HHV,
                                                   gasInformationFormInputData["Station_Capacity"])
        afterheater = [Calculation.noHeatLossConsumption.Q_heater, after_heater_heat_loss_with_insulation_consumption,
                       after_heater_heat_loss_without_insulation_consumption]

        print(afterheater)

        beforeheater = [Calculation.noHeatLossConsumption.Q_heater, before_heater_heat_loss_with_insulation_consumption,
                        before_heater_heat_loss_without_insulation_consumption]

        print(beforeheater)


        string =  ("دمای هیدرات = %s \n"
                "بار حرارتی = %s\n"
                "راندمان مشعل = %s\n"
                   "تلفات حرارتی ران = %s\n" % (Calculation.noHeatLossConsumption.T_hydrate, Calculation.noHeatLossConsumption.Q_heater +
                      after_heater_heat_loss_with_insulation_consumption, combustionCalculation.efficiency, runHeatLoss.heatloss))
        print(string)


if __name__ == "__main__":
    pass
