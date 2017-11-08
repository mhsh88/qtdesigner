from behinesazan.gas.station.software.model.HeatLoss.PipeLineEndDefined.PipeLineEndDefinedHeatLoss import PipeLineEnd
from behinesazan.gas.station.software.model.Logic.calculation.capacityCalculation.CapacityCalculation import \
    CapacityCalculation


class RunHeatLoss:
    result = {}
    T_before_run = None

    def __init__(self, runData, gasInformationFormInputData, T_regulator, HHV):
        self.heatloss = ""
        self.capacity_calculation = CapacityCalculation()
        if bool(runData) and 'Wind_velocity' in gasInformationFormInputData.keys() and \
                        "T_environment" in gasInformationFormInputData.keys() and \
                        "Station_Capacity" in gasInformationFormInputData.keys():
            self.T_before_run = self.runCal(runData, gasInformationFormInputData, T_regulator, HHV)
        else:
            self.T_before_run = T_regulator
            return

    def runCal(self, runData, gasInformationFormInputData, T_regulator, HHV):
        # print(runData['run_debi'])
        self.heatloss = ""
        self.result.setdefault("heat_loss", {})
        self.result["heat_loss"].setdefault("run", {})
        t_max = 0
        for key in runData["run_debi"].keys():
            self.result["heat_loss"]["run"].setdefault(key, {})
            self.result["heat_loss"]["run"][key].setdefault("", {})
            self.result["heat_loss"]["run"][key] = PipeLineEnd(gasInformationFormInputData["T_environment"],
                                                               gasInformationFormInputData["Wind_velocity"],
                                                               # as Tin
                                                               T_regulator,
                                                               gasInformationFormInputData["P_input"],
                                                               gasInformationFormInputData["gas"],
                                                               runData["OD"],
                                                               runData["ID"],
                                                               runData["length"],
                                                               runData["run_debi"][key], 0, 0)

            consumption = self.capacity_calculation.gasConsumptionCal(
                gasInformationFormInputData["P_input"],
                self.result["heat_loss"]["run"][key].Tout,
                gasInformationFormInputData["P_input"],
                T_regulator,
                gasInformationFormInputData["gas"],
                HHV,
                runData["run_debi"][key])
            self.result["heat_loss"]["run"][key]["consumption"] = consumption

            t_max = max(t_max, self.result["heat_loss"]["run"][key].Tout)
            # string = ("تلفات حرارتی ران %s ،%s\n" % (key, self.result["heat_loss"]["run"][key]["consumption"]))
            # self.heatloss += string

        return t_max
