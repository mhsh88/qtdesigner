from behinesazan.gas.station.software.model.gas.Gas import Gas
import numpy as np
from scipy.interpolate import interp1d


class Combustion:
    O2factor = [0, 0, 2, 3.5, 5, 6.5, 6.5, 8, 8, 9.5, 11, 12.5, 14, 15.5, 1, 0, 0.5, 0, 0, 0, 0]
    H2Ofactor = [0, 0, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10, 11, 2, 0, 0, 1, 0, 0, 0]
    CO2factor = [0, 1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10, 0, 0, 1, 0, 0, 0, 0]
    N2factor = np.multiply([1/3.76, 0, 2, 3.5, 5, 6.5, 6.5, 8, 8, 9.5, 11, 12.5, 14, 15.5, 1, 0, 0.5, 0, 0, 0, 0],  3.76)
    dencity = [1.2504, 1.977, 0.7175, 1.355, 2.011, 2.7083, 2.5326, 2.975, 2.975, 0, 0, 0, 0, 0, 0.0845, 1.429, 1.165,
               0.5040, 1.434, 0.1664, 1.661]
    HHV = [0, 0, 55499, 51876, 50346, 49500, 49500, 48776, 48776, 0, 0, 0, 0, 0, 141790, 0, 10160.4048, 0, 0, 0, 0]
    temp = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    Cp_Co2 = interp1d(temp, [1.620, 1.725, 1.808, 1.884, 1.951, 2.009, 2.064, 2.110, 2.156, 2.189, 2.227], kind='cubic')
    Cp_O2 = interp1d(temp, [1.306, 1.319, 1.340, 1.360, 1.381, 1.398, 1.419, 1.436, 1.453, 1.469, 1.482], kind='cubic')
    Cp_N2 = interp1d(temp, [1.302, 1.302, 1.306, 1.310, 1.323, 1.335, 1.344, 1.360, 1.377, 1.386, 1.398], kind='cubic')
    Cp_H2O = interp1d(temp, [1.427, 1.440, 1.457, 1.473, 1.494, 1.520, 1.545, 1.570, 1.595, 1.620, 1.645], kind='cubic')
    tempforH2O = [100, 120, 160, 200, 240, 280, 320, 360, 400, 440, 500]
    ro_H2O = interp1d(tempforH2O, [0.590, 0.558, 0.504, 0.460, 0.424, 0.393, 0.366, 0.343, 0.322, 0.304, 0.281],
                      kind='cubic')
    HHVmole = [0, 0, 889, 1560, 2220, 2877, 2877, 3507, 3507, 4163, 4817, 5470, 6125, 6778, 286, 0, 0, 0, 0, 0, 0]

    # hexane  663.700 heptane 683.7



    def __init__(self, g, O2percent, Tamb, Tstack):
        g.calculate(101.325, 273.15 + 15)
        A0 = 1 / 0.21 * np.dot(g.component, self.O2factor)
        G0prime = np.dot(g.component, self.CO2factor) + 3.76 * np.dot(g.component, self.O2factor)
        Gwf = np.dot(g.component, self.H2Ofactor)

        G0 = G0prime + Gwf

        CO2max = 100 / G0prime * np.dot(g.component, self.CO2factor)

        landa = 1 + ((G0prime / A0) * (O2percent / (21 - O2percent)))
        dry_mass = np.dot(self.CO2factor, g.component) * 44.01 + np.dot(self.O2factor, g.component) * 32 * (landa - 1) +\
                   np.dot(self.N2factor, g.component) * landa * 28.01
        dry_mass_fraction = dry_mass/g.M
        CO2 = CO2max * ((21 - O2percent) / 21)
        # O2 = O2percent  # TODO check
        O2 = 21 - (21 / landa)
        N2 = 100 - (O2 + CO2)
        dry_gas_dencity = np.dot([N2, CO2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, O2, 0, 0, 0, 0, 0],
                                 self.dencity) / 100
        CP_Stack = (self.Cp_Co2(Tstack) * CO2 / 100 + self.Cp_O2(Tstack) * O2 / 100 + self.Cp_N2(
            Tstack) * N2 / 100) / dry_gas_dencity
        CP_amb = (self.Cp_Co2(Tamb) * CO2 / 100 + self.Cp_O2(Tamb) * O2 / 100 + self.Cp_N2(
            Tamb) * N2 / 100) / dry_gas_dencity

        CP_Total_mass = (CP_Stack + CP_amb) / (2 * dry_gas_dencity)

        if Tstack < 55:
            latent_heat = 0
        else:
            latent_heat = 2260

        massFraction = np.multiply(g.component, self.dencity) / np.dot(g.component, self.dencity)
        mH2O = np.dot(self.H2Ofactor, g.component) * 18.02
        mH20_fraction = mH2O / g.M
        # muH2OtoFuel = mH2O / g.M
        heatCapacity = np.dot(self.HHV, massFraction)
        self.HHVd = heatCapacity * g.D
        # (G0prime * 21 / (21 - O2percent)
        self.loss = (dry_mass_fraction * (CP_Stack * Tstack - CP_amb * Tamb) + mH20_fraction * (
            (self.Cp_H2O(Tstack) / self.ro_H2O(Tstack)) * Tstack - (self.Cp_H2O(Tamb) / self.ro_H2O(Tamb)) * Tamb) +
                     mH20_fraction * latent_heat) / self.HHVd
        self.eff = 1 - self.loss


if __name__ == "__main__":
    g = Gas()
    c = Combustion(g, 5, 25 + 273.15, 200 + 273.15)
