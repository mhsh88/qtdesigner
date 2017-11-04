from behinesazan.gas.station.software.model.Combustion.Combustion import Combustion
from behinesazan.gas.station.software.model.Logic.calculation.Calculation import Calculation


class CombustionCalculation:

    def __init__(self):
        return

    @staticmethod
    def combustionCal(heaterData, gasInformationFormInputData):
        Calculation.result.setdefault('heater', {})
        if bool(heaterData) and "T_environment" in gasInformationFormInputData.keys():

            for keys in heaterData:
                Calculation.result["heater"].setdefault(keys, {})
                for key in heaterData[keys]:
                    Calculation.result["heater"][keys].setdefault(key, None)
                    Calculation.result["heater"][keys][key] = Combustion(gasInformationFormInputData["gas"],
                                                                         heaterData[keys][key]["oxygen"],
                                                                         gasInformationFormInputData["T_environment"],
                                                                         heaterData[keys][key]["fluegas"])
        else:
            return

                # print("efficiency: ", "heater ", keys, " burner ", key, Calculation.result["heater"][keys][key].eff)

        pass

    pass
