from behinesazan.gas.station.software.model.HeatLoss.PipeLineEndDefined.PipeLineEndDefinedHeatLoss import PipeLineEnd


class AfterHeaterHeatLoss:
    T_out_with_insulation = None
    T_out_without_insulation = None

    def __init__(self, afterHeaterLineData, gasInformationFormInputData, T_before_run):

        if bool(afterHeaterLineData) and "Wind_velocity" in gasInformationFormInputData.keys() and \
                        "T_environment" in gasInformationFormInputData.keys() and \
                        "Station_Capacity" in gasInformationFormInputData.keys():
            self.__afterHeaterHeatLossCal(afterHeaterLineData, gasInformationFormInputData, T_before_run)
        else:
            self.T_out_with_insulation = T_before_run
            self.T_out_without_insulation = T_before_run

            pass

        return


    def __afterHeaterHeatLossCal(self, afterHeaterLineData, gasInformationFormInputData, T_before_run):

        after_heater_pipeline_with_insulation = PipeLineEnd(
            gasInformationFormInputData["T_environment"],
            gasInformationFormInputData["Wind_velocity"],
            # as Tin
            T_before_run,
            gasInformationFormInputData["P_input"],
            gasInformationFormInputData["gas"],
            afterHeaterLineData["OD"],
            afterHeaterLineData["ID"],
            afterHeaterLineData["length"],
            gasInformationFormInputData["Station_Capacity"],
            afterHeaterLineData["insulation_thickness"],
            afterHeaterLineData["thermal_conductivity"])
        after_heater_pipeline_without_insulation = PipeLineEnd(
            gasInformationFormInputData["T_environment"],
            gasInformationFormInputData["Wind_velocity"],
            # as Tin
            T_before_run,
            gasInformationFormInputData["P_input"],
            gasInformationFormInputData["gas"],
            afterHeaterLineData["OD"],
            afterHeaterLineData["ID"],
            afterHeaterLineData["length"],
            gasInformationFormInputData["Station_Capacity"],
            0,
            0)
        self.T_out_with_insulation = after_heater_pipeline_with_insulation.Tout
        self.T_out_without_insulation = after_heater_pipeline_without_insulation.Tout

        pass
