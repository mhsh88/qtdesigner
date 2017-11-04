from behinesazan.gas.station.software.model.HeatLoss.PipeLineEndDefined.PipeLineEndDefinedHeatLoss import PipeLineEnd


class RunHeatLoss:
    result = {}
    T_before_run = None

    def __init__(self, runData, gasInformationFormInputData, T_regulator):
        if bool(runData) and 'Wind_velocity' in gasInformationFormInputData.keys() and \
                        "T_environment" in gasInformationFormInputData.keys() and \
                        "Station_Capacity" in gasInformationFormInputData.keys():
            T_before_run = self.runCal(runData, gasInformationFormInputData)
        else:
            T_before_run = T_regulator
            return

    def runCal(self, runData, gasInformationFormInputData, T_regulator):
        # print(runData['run_debi'])
        self.result.setdefault("heat_loss", {})
        self.result["heat_loss"].setdefault("run", {})
        t_max = 0
        for key in runData["run_debi"].keys():
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

            t_max = max(t_max, Calculation.result["heat_loss"]["run"][key].Tout)

        return t_max
