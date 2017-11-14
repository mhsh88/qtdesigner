from behinesazan.gas.station.software.model.Combustion.Combustion import Combustion


class CombustionCalculation:
    result = {}

    def __init__(self):
        self.efficiency = []
        return

    def combustionCal(self, heaterData, gasInformationFormInputData):
        self.efficiency = []
        self.result.setdefault('heater', {})
        if bool(heaterData) and "T_environment" in gasInformationFormInputData.keys():

            for keys in sorted(heaterData.keys()):
                self.result["heater"].setdefault(keys, {})
                for key in sorted(heaterData[keys].keys()):
                    burner = []
                    self.result["heater"][keys].setdefault(key, None)
                    self.result["heater"][keys][key] = Combustion(gasInformationFormInputData["gas"],
                                                                  heaterData[keys][key]["oxygen"],
                                                                  gasInformationFormInputData["T_environment"],
                                                                  heaterData[keys][key]["fluegas"])

                    string = ("گرم کن %s، مشعل %s" % (keys, key))
                    burner = [string,  self.result["heater"][keys][key].eff]
                    # print(string)
                    self.efficiency.append(burner)
        else:
            return

            # print("efficiency: ", "heater ", keys, " burner ", key, self.result["heater"][keys][key].eff)

        pass

    pass
