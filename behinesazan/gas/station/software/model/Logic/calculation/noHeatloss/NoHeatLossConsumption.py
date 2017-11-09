from behinesazan.gas.station.software.model.Combustion.Combustion import Combustion
from behinesazan.gas.station.software.model.Logic.calculation.capacityCalculation.CapacityCalculation import \
    CapacityCalculation
from behinesazan.gas.station.software.model.Regulator.Regulator import Regulator


class NoHeatLossConsumption:
    T_before_regulator = None
    T_hydrate = None
    Q_heater = None
    HHV = None

    def __init__(self, gasInformationFormInputData):
        tempHHV = Combustion(gasInformationFormInputData["gas"], 2, 15+273.15, 200)
        self.HHV = tempHHV.HHVd
        regulator = Regulator(gasInformationFormInputData["P_input"], gasInformationFormInputData["T_station_out"],
                              gasInformationFormInputData["P_station_out"], gasInformationFormInputData["gas"])
        tBeforeRegulator = regulator.Tin


        capacity_calculation = CapacityCalculation()


        self.T_before_regulator = tBeforeRegulator

        # for temporary calculation
        gasInformationFormInputData["gas"].calculate(gasInformationFormInputData["P_station_out"],
                                                     gasInformationFormInputData["T_station_out"])
        print("this is print in calculate method of Calculation class T hydrate is ",
              gasInformationFormInputData["gas"].T_h, " at ", round(gasInformationFormInputData["gas"].P / 6.89476, 5),
              "psi")
        self.T_hydrate = gasInformationFormInputData["gas"].T_h

        # check if Station Capacity is entered to calculation amount of energy needed

        if "Station_Capacity" in gasInformationFormInputData.keys():
            self.Q_heater = capacity_calculation.gasConsumptionCal(gasInformationFormInputData["P_input"],
                                                                   gasInformationFormInputData["T_input"],
                                                                   gasInformationFormInputData["P_input"],
                                                                   tBeforeRegulator,
                                                                   gasInformationFormInputData["gas"],
                                                                   self.HHV,
                                                                   gasInformationFormInputData["Station_Capacity"])

        pass


if __name__ == "__main__":
    pass
