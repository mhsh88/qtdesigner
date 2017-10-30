import unittest
import numpy as np

from behinesazan.gas.station.software.model.Logic.calculation.Calculation import Calculation
from behinesazan.gas.station.software.model.gas.Gas import Gas as gas
from AgaQt import Gas as agagas
from behinesazan.gas.station.software.model.Regulator.Regulator import Regulator


class CalculationTest(unittest.TestCase):
    def test_calculate(self, g):
        data = {'gas': g, 'P_station_out': 1723.69, 'P_Standard': 698.611557, 'T_input': 280.15, 'P_input': 4136.856, 'T_station_out': 281.15, 'T_Standard': 288.15}

        regulator = Regulator(data["P_input"], data["T_station_out"], data["P_station_out"], data["gas"])
        # self.assertEqual(regulator.Tin, [292.65335678])
        print(regulator.Tin)



        pass


if __name__ == "__main__":
    calculationTest = CalculationTest()
    g1 = gas()
    g2 = agagas()
    calculationTest.test_calculate(g2)
    calculationTest.test_calculate(g1)

    pass
