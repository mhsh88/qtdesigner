from behinesazan.gas.station.software.model.HeatLoss.PipeLineHeadDefined.PipeLineHeadDefinedHeatLoss import PipeLineHead


class BeforeHeaterHeatLoss:
    T_out_with_insulation = None
    T_out_without_insulation = None

    def __init__(self, beforeHeaterLineData, gasInformationFormInputData):
        if bool(beforeHeaterLineData) and "Wind_velocity" in gasInformationFormInputData.keys() and \
                        "T_environment" in gasInformationFormInputData.keys():
            self.__beforeHeaterHeatLossCal(beforeHeaterLineData, gasInformationFormInputData)
        else:
            self.T_out_with_insulation = gasInformationFormInputData["T_input"]
            self.T_out_without_insulation = gasInformationFormInputData["T_input"]
            pass

    def __beforeHeaterHeatLossCal(self, beforeHeaterLineData, gasInformationFormInputData):
        before_heater_pipeline_with_insulation = PipeLineHead(
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
                beforeHeaterLineData[
                    "thermal_conductivity"])  # TODO it must be checked for Station capacity and runs flows
        before_heater_pipeline_without_insulation = PipeLineHead(
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

        self.T_out_with_insulation = before_heater_pipeline_with_insulation.Tout
        self.T_out_without_insulation = before_heater_pipeline_without_insulation.Tout

