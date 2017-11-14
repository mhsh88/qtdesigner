import copy

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
        runsum = 0
        if 'run_debi' in runData:
            for key in runData['run_debi']:
                runsum +=  runData['run_debi'][key]
            if runsum > gasInformationFormInputData['Station_Capacity'] or  runsum <= gasInformationFormInputData['Station_Capacity']:
                gasInformationFormInputData['Station_Capacity'] = runsum
        result = {}
        temp = copy.deepcopy(gasInformationFormInputData)
        result['user'] = Calculation.consumption_calculation(temp,
                                                                 beforeHeaterLineData,
                                                                 heaterData, afterHeaterLineData, runData)


        temp1 = copy.deepcopy(gasInformationFormInputData)
        temp1["T_station_out"] = Calculation.noHeatLossConsumption.T_hydrate + 273.15
        result['T_hydrate'] = Calculation.consumption_calculation(temp1,
                                                                       beforeHeaterLineData,
                                                                       heaterData, afterHeaterLineData, runData)
        temp2 = copy.deepcopy(gasInformationFormInputData)
        temp2["T_station_out"] = Calculation.noHeatLossConsumption.T_hydrate + 273.15 + 2
        result['T_hydrate_plus_2'] = Calculation.consumption_calculation(temp2,
                                                                       beforeHeaterLineData,
                                                                       heaterData, afterHeaterLineData, runData)

        return result

        pass

    @staticmethod
    def consumption_calculation(gasInformationFormInputData, beforeHeaterLineData, heaterData, afterHeaterLineData, runData):
        burnerconsumption = {}
        # try:
        Calculation.noHeatLossConsumption = NoHeatLossConsumption(gasInformationFormInputData)

        # check if heater data form is defined and air temperature is defined in Gas information form input data
        combustionCalculation = CombustionCalculation()
        combustionCalculation.combustionCal(heaterData, gasInformationFormInputData)



        runHeatLoss = RunHeatLoss(runData, gasInformationFormInputData,
                                  Calculation.noHeatLossConsumption.T_before_regulator,
                                  Calculation.noHeatLossConsumption.HHV)
        runconsumption = 0
        for run in runHeatLoss.heatloss:
            runconsumption += run[1]




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

        heater_consumption = capacity_calculation.gasConsumptionCal(gasInformationFormInputData["P_input"],
                                                                    beforeHeaterHeatLoss.T_out_without_insulation,
                                                                    gasInformationFormInputData["P_input"],
                                                                    afterHeaterHeatLoss.T_out_with_insulation,
                                                                    gasInformationFormInputData["gas"],
                                                                    Calculation.noHeatLossConsumption.HHV,
                                                                    gasInformationFormInputData["Station_Capacity"])
        afterheater = [Calculation.noHeatLossConsumption.Q_heater, after_heater_heat_loss_with_insulation_consumption,
                       after_heater_heat_loss_without_insulation_consumption]


        beforeheater = [Calculation.noHeatLossConsumption.Q_heater, before_heater_heat_loss_with_insulation_consumption,
                        before_heater_heat_loss_without_insulation_consumption]

        saving_percent = Calculation.difference_heatloss(Calculation.noHeatLossConsumption.Q_heater, heater_consumption,
                                                         before_heater_heat_loss_without_insulation_consumption,
                                                         before_heater_heat_loss_with_insulation_consumption,
                                                         after_heater_heat_loss_without_insulation_consumption,
                                                         after_heater_heat_loss_with_insulation_consumption)

        heaterpartialconsumption = (consumption_without_heatloss -before_heater_heat_loss_with_insulation_consumption -
             after_heater_heat_loss_with_insulation_consumption - runconsumption) / len(combustionCalculation.result.keys())

        for heater in combustionCalculation.result["heater"].keys():
            burnerconsumption.setdefault(heater, {})
            burnerpartialconsumption = heaterpartialconsumption/len(combustionCalculation.result["heater"][heater])

            for burner in combustionCalculation.result["heater"][heater].keys():
                burnerconsumption[heater][burner] = burnerpartialconsumption/combustionCalculation.result["heater"][heater][burner].eff
        rr = {}
        rr["دمای هیدرات"] = round(Calculation.noHeatLossConsumption.T_hydrate,3)
        rr['دمای گاز قبل از رگولاتور'] =Calculation.noHeatLossConsumption.T_before_regulator - 273.15
        rr["بار حرارتی"] = consumption_without_heatloss -before_heater_heat_loss_with_insulation_consumption - \
                           after_heater_heat_loss_with_insulation_consumption - runconsumption
        rr["بار حرارتی بدون تلفات لوله"]=consumption_without_heatloss
        rr['راندمان مشعل'] = combustionCalculation.efficiency
        rr['تلفات حرارتی ران'] = runHeatLoss.heatloss
        rr['تلفات خط لوله قبل از گرم کن'] = [before_heater_heat_loss_without_insulation_consumption, before_heater_heat_loss_with_insulation_consumption]
        rr['تلفات خط لوله بعد از گرم کن'] = [after_heater_heat_loss_without_insulation_consumption,
                                         after_heater_heat_loss_with_insulation_consumption]
        rr['مصرف با راندمان محاسبه شده'] = burnerconsumption
        rr['درصد صرفه جویی عایق'] =  saving_percent * 100
        rr['مصرف هیتر با راندمان ۸۰ درصد'] = (consumption_without_heatloss - before_heater_heat_loss_with_insulation_consumption -
             after_heater_heat_loss_with_insulation_consumption - runconsumption) / 0.8
        r = [["دمای هیدرات", round(Calculation.noHeatLossConsumption.T_hydrate,3)],['دمای گاز قبل از رگولاتور',
                                                                                       Calculation.noHeatLossConsumption.T_before_regulator - 273.15],
             ["بار حرارتی", consumption_without_heatloss -before_heater_heat_loss_with_insulation_consumption -
             after_heater_heat_loss_with_insulation_consumption - runconsumption],
             ["بار حرارتی بدون تلفات لوله",consumption_without_heatloss],
             ['راندمان مشعل', combustionCalculation.efficiency],
             ['تلفات حرارتی ران', runHeatLoss.heatloss],
             ['تلفات خط لوله قبل از گرم کن', [before_heater_heat_loss_without_insulation_consumption,
                                        before_heater_heat_loss_with_insulation_consumption]],
             ['تلفات خط لوله بعد از گرم کن', [after_heater_heat_loss_without_insulation_consumption,
                                        after_heater_heat_loss_with_insulation_consumption]],
             ['درصد صرفه جویی عایق',saving_percent * 100],
             ['مصرف با راندمان محاسبه شده', burnerconsumption],
             ['مصرف هیتر با راندمان ۸۰ درصد', (consumption_without_heatloss -before_heater_heat_loss_with_insulation_consumption -
             after_heater_heat_loss_with_insulation_consumption - runconsumption) / 0.8]]

        return rr

    @staticmethod
    def difference_heatloss(q_heater, q_heater_heat_loss, before, before_insulation, after, after_insulation):
        if q_heater < 0.0000000001:
            return 0.0

        Q_with_heat_loss = q_heater - before - after
        Q_with_insulation = q_heater - before_insulation - after_insulation
        return (Q_with_heat_loss - Q_with_insulation) / Q_with_heat_loss


if __name__ == "__main__":
    pass
