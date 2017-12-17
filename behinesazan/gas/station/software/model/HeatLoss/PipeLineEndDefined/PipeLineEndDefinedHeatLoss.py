import math

import numpy
from scipy.interpolate import interp1d

from behinesazan.gas.station.software.model.gas.Gas import Gas
from math import exp
from scipy.optimize import fsolve


class PipeLineEnd:
    # ID = 0.4
    # OD = 0.5
    # pipeLength = 20
    # Tin = 5
    # T_air = 20

    def __init__(self, T_air, v_air, Tin, P, g, OD, ID, pipeLength, QSdot, t, k_insolation):
        if QSdot == 0:
            self.Tout = Tin
            self.Qdot = 0.0
            self.g = g
            self.mdot = 0
            g.calculate(P, Tin)
            return

        self.P = P
        self.Tin = Tin
        self.T_air = T_air
        self.pipeLength = pipeLength
        self.OD = OD
        self.ID = ID

        # print('pipeLength, ID, OD ---> after init', self.pipeLength, self.ID, self.OD)

        # g = Gas()
        # g.P = P
        g.calculate(g.p_theta, g.T_theta)
        P2 = g.P
        Z2 = g.Z
        T2 = g.T
        g.calculate(P, Tin)
        P1 = g.P
        Z1 = g.Z
        T1 = g.T

        Qdot = (QSdot / 3600) * (P2 * Z1 * T1) / (P1 * Z2 * T2)

        A = math.pi * self.ID * self.ID / 4
        V = Qdot / A
        # print('\nV is = ' + str(V))
        self.g = g

        # print('mdot is = ' + str(math.fsum(mdot)))

        t1 = Tin
        t2 = t1 + 1
        Ts = T_air + 5
        # print('Tin = ' + str(Tin))

        while math.fabs((t1 - t2) / t2) > 10 ** -4:
            self.g.calculate(self.g.P, (t1 + t2) / 2)
            # mdot =
            self.mdot = Qdot * self.g.D
            t1 = t2

            rou = self.g.D * 0.001
            T = self.g.T * 1.8
            Mg = self.g.M
            X = 3.5 + 986 / T + 0.01 * Mg
            Y = 2.4 - 0.2 * X
            K = ((9.4 + 0.02 * Mg) * T ** 1.5) / (209 + 19 * Mg + T)
            mu = (K * 10 ** -4) * exp(X * rou ** Y)

            self.R = self.g.D * V * self.ID / (mu * 0.001)

            k_gas = 0.05

            Pr = self.g.C_p * mu / k_gas  # [mu] --> cp, [C_p] --> kJ/kg.K, [k_gas (thermal conductivity)] --> W/m.K
            if v_air >= 2:
                hair = 10.45 - v_air + 10 * v_air ** (1 / 2)
            else:
                hair = self.hairCalculation(Ts)

            gamma = self.g.M / 28.966

            k_steel = 52  # thermal conductivity of steel is 45 W/m.K

            # self.m = 0
            friction = fsolve(self.friction, 8)
            friction = math.fabs(friction)
            # print(friction)
            deltaP = friction * self.g.D * (V ** 2 / (2 * self.ID)) * self.pipeLength
            Power = deltaP * Qdot
            # print('delta P = %s' %Power)




            ##
            # Nu = ((friction / 8) * (self.R - 1000) * Pr) / (1 + 12.7 * ((friction / 8) ** 0.5) * (Pr ** (2/3) - 1))
            # h_gas = Nu * k_gas/self.ID

            Nu = 4.82 + 0.0185 * (self.R * Pr) ** 0.827

            h_gas = Nu * k_gas / self.ID

            if t > 0:
                self.h_Total = 1 / (1 / hair + 1 / h_gas + ((self.OD - self.ID) / math.log(self.OD / self.ID)) / k_steel +
                                ((self.OD + 2 * t - self.OD) / math.log((self.OD + 2 * t) / self.OD)) / k_insolation)
            else:
                self.h_Total = 1 / (1 / hair + 1 / h_gas + ((self.OD - self.ID) / math.log(self.OD / self.ID)) / k_steel)

            # self.Tout = (self.Tin - self.T_air) * exp(-math.pi*self.ID * self.pipeLength * self.h_Total / (self.mdot * g.C_p * 1000)) + self.T_air
            self.Tout = (self.Tin - self.T_air) / exp(
                -math.pi * self.ID * self.pipeLength * self.h_Total / (self.mdot * self.g.C_p * 1000)) + self.T_air
            # print('Tin is = ' + str(self.Tin - 273.15) +'\nTout is = ' + str(self.Tout - 273.15) + "\n deltaT = " + str(self.Tin - self.Tout))
            self.Qdot = self.mdot * self.g.C_p * (self.Tin - self.Tout)
            # print('Qdot = ' + str(self.mdot * g.C_p * 1000 * (self.Tout - self.Tin)))
            # print('delta P  = ' + str(P))
            outter_A = math.pi * self.OD * self.OD / 4
            deltaT = self.Qdot * 1000 / (hair * outter_A)
            Ts = T_air + deltaT

            t2 = self.Tout

            # print('Tin ' + str(self.Tout - 273.15) + ', Tout = ' + str(self.Tin - 273.15) + ', T_air = ' + str(T_air - 273.15) + '\nQdot = ' + str(self.Qdot) + '\nmdot = ' + str(self.mdot)
            #       + '\nC_p = ' + str(self.g.C_p) + '\ndeltaT = ' + str(self.Tin - self.Tout) + '\nV = ' + str(V))

    def friction(self, f):
        # self.m +=1
        if f <= 0:
            f = math.fabs(f)

        return 1 / math.sqrt(f) + 2 * math.log2(0.01 / (0.4 * 3.7) + 2.57 / (self.R * math.sqrt(f)))

    def tOutCal(self, tout):
        # print('H total is = ' + str(self.h_Total))
        # print('T air is = ' + str(self.T_air), '\nT in is = ' + str(self.Tin))
        # print("T_out is = " + str(math.fsum(tout)))

        # if To >= self.T_air:
        #     To = self.T_air - 1
        deltaTm = ((self.T_air - tout) - (self.T_air - self.Tin)) / math.log(
            (self.T_air - tout) / (self.T_air - self.Tin))

        return ((self.mdot * self.g.C_p * 1000) * ((tout - self.Tin) / deltaTm)) / (math.pi * self.ID * self.pipeLength) \
               - self.h_Total

    def calcul(self, pipelength, ID, OD):
        self.pipeLength = pipelength
        self.ID = ID
        self.OD = OD
        print('pipeLength, ID, OD', self.pipeLength, self.ID, self.OD)
        self.__init__(self.P, self.Tin)

    def hairCalculation(self, Ts):
        Temp = [175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900,
                950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1500, 1600, 1700, 1800, 1900]
        cp = [1002.3, 1002.5, 1002.7, 1003.1, 1003.8, 1004.9, 1006.3, 1008.2, 1010.6, 1013.5, 1020.6, 1029.5, 1039.8,
              1051.1, 1062.9, 1075, 1087, 1098.7, 1110.1, 1120.9, 1131.3, 1141.1, 1150.2, 1158.9, 1167, 1174.6, 1181.7,
              1188.4, 1194.6, 1200.5, 1211.2, 1220.7, 1229.3, 1237, 1244]
        mu_table = [0.00001182, 0.00001329, 0.00001467, 0.00001599, 0.00001725, 0.00001846, 0.00001962, 0.00002075,
                    0.00002181, 0.00002286, 0.00002485, 0.0000267, 0.00002849, 0.00003017, 0.00003178, 0.00003332,
                    0.00003482, 0.00003624, 0.00003763, 0.00003897, 0.00004026, 0.00004153, 0.00004276, 0.00004396,
                    0.00004511, 0.00004626, 0.00004736, 0.00004846, 0.00004952, 0.00005057, 0.00005264, 0.00005457,
                    0.00005646, 0.00005829, 0.00006008]
        k_table = [0.00001593, 0.00001809, 0.0000202, 0.00002227, 0.00002428, 0.00002624, 0.00002816, 0.00003003,
                   0.00003186, 0.00003365, 0.0000371, 0.00004041, 0.00004357, 0.00004661, 0.00004954, 0.00005236,
                   0.00005509, 0.00005774, 0.0000603, 0.00006276, 0.0000652, 0.00006754, 0.00006985, 0.00007209,
                   0.00007427, 0.0000764, 0.00007849, 0.00008054, 0.00008253, 0.0000845, 0.00008831, 0.00009199,
                   0.00009554, 0.00009899, 0.00010233]
        rou_table = [2.017, 1.765, 1.569, 1.412, 1.284, 1.177, 1.086, 1.009, 0.9413, 0.8824, 0.7844, 0.706, 0.6418,
                     0.5883, 0.543, 0.5043, 0.4706, 0.4412, 0.4153, 0.3922, 0.3716, 0.353, 0.3362, 0.3209, 0.3069,
                     0.2941, 0.2824, 0.2715, 0.2615, 0.2521, 0.2353, 0.2206, 0.2076, 0.1961, 0.1858]
        mu_interpole = interp1d(Temp,mu_table, kind='cubic')
        rou_interpole = interp1d(Temp, rou_table, kind='cubic')
        cp_interpole = interp1d(Temp, cp, kind='cubic')
        k_interpole = interp1d(Temp, k_table, kind='cubic')

        g = 9.81
        mu = mu_interpole(self.T_air)
        rou = rou_interpole(self.T_air)
        Cp_air = cp_interpole(self.T_air)
        k_air = k_interpole(self.T_air)
        beta = 2 / (Ts - self.T_air)
        nu = mu / rou
        Gr = (g * beta * (Ts - self.T_air) * self.OD ** 3) / nu ** 2
        Pr = mu * Cp_air / k_air
        Ra = Gr * Pr
        Tf = (Ts + self.T_air) / 2
        Nu = (0.6 + ((0.387 * Ra ** (1 / 6)) / (1 + (0.559 / Pr) ** (9 / 16)) ** (8 / 27))) ** 2
        hair = k_air * Nu / self.OD
        return hair


if __name__ == "__main__":
    g = Gas()
    g.component = [0.057, 0.076, 0.812, 0.043, 0.009, 0.0015, 0.0015, 0., 0., 0.
        , 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.
        , 0.]
    # numpy.arange(0.0, 1.0, 0.1)
    # for v in numpy.arange(0.0, 4.0, 0.05):
    R = PipeLineEnd(30 + 273.15, 10, 20 + 273.15, 7000, g, 0.4, 0.38, 20, 4000, .05, 100)
    print(R.Tout - 273.15)

        # R.calcul(50, 0.5, 0.7)
