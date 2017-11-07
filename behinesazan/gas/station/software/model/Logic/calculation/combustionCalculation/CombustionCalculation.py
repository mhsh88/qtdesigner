from behinesazan.gas.station.software.model.Combustion.Combustion import Combustion


class CombustionCalculation:
    result = {}

    def __init__(self):
        self.efficiency = ""
        return

    def combustionCal(self, heaterData, gasInformationFormInputData):
        self.efficiency = ""
        self.result.setdefault('heater', {})
        if bool(heaterData) and "T_environment" in gasInformationFormInputData.keys():

            for keys in heaterData:
                self.result["heater"].setdefault(keys, {})
                for key in heaterData[keys]:
                    self.result["heater"][keys].setdefault(key, None)
                    self.result["heater"][keys][key] = Combustion(gasInformationFormInputData["gas"],
                                                                  heaterData[keys][key]["oxygen"],
                                                                  gasInformationFormInputData["T_environment"],
                                                                  heaterData[keys][key]["fluegas"])

                    string = ("هیتر %s، مشعل %s، %s\n" % (keys, key, self.result["heater"][keys][key].eff[0]))
                    print(string)
                    self.efficiency = self.efficiency + string
        else:
            return

            # print("efficiency: ", "heater ", keys, " burner ", key, self.result["heater"][keys][key].eff)

        pass

    pass
