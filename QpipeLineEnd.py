import sys
import math
# sys.path.append('D:\\hossein sharifi 96-01-19\\behinesazan\\narmafzar\\myqtdesigner\\AgaQt')
# sys.path.append('C:\\Users\\Hossein\\Desktop\\myqtdesigner\\96-02-20\\GasStationSoftware\\myqtdesigner\\AgaQt')
from AgaQt import Gas
from math import exp
from scipy.optimize import fsolve



class PipeLineEnd():
    # ID = 0.4
    # OD = 0.5
    # pipeLength = 20
    # Tin = 5
    # T_air = 20

    def __init__(self, T_air, v_air, Tin, P, g, OD, ID, pipeLength, QSdot):
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

        Qdot = (QSdot/3600) * (P2 * Z1 * T1)/(P1 * Z2 * T2)

        A = math.pi * self.ID * self.ID / 4
        V = Qdot/A
        # print('\nV is = ' + str(V))
        self.g = g


        # print('mdot is = ' + str(math.fsum(mdot)))

        t1 = Tin
        t2 = t1 + 1
        # print('Tin = ' + str(Tin))

        while math.fabs((t1 - t2) / t2) > 10**-4:


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

            hair = 10.45 - v_air + 10 * v_air ** (1 / 2)

            gamma = self.g.M / 28.966

            k_steel = 52  # thermal conductivity of steel is 45 W/m.K







            # self.m = 0
            friction = fsolve(self.friction, 8)
            friction = math.fabs(friction)
            print(friction)
            deltaP = friction * self.g.D * (V**2 / (2*self.ID)) * self.pipeLength
            Power = deltaP * Qdot
            # print('delta P = %s' %Power)




            ##
            # Nu = ((friction / 8) * (self.R - 1000) * Pr) / (1 + 12.7 * ((friction / 8) ** 0.5) * (Pr ** (2/3) - 1))
            # h_gas = Nu * k_gas/self.ID

            Nu = 4.82 + 0.0185 * (self.R * Pr) ** 0.827

            h_gas = Nu * k_gas / self.ID

            self.h_Total = 1 / (1 / hair + 1 / h_gas + ((self.OD - self.ID) / math.log(self.OD / self.ID)) / k_steel)
            # self.Tout = (self.Tin - self.T_air) * exp(-math.pi*self.ID * self.pipeLength * self.h_Total / (self.mdot * g.C_p * 1000)) + self.T_air
            self.Tout = (self.Tin - self.T_air)/exp(-math.pi*self.ID * self.pipeLength * self.h_Total / (self.mdot * self.g.C_p * 1000)) + self.T_air
            # print('Tin is = ' + str(self.Tin - 273.15) +'\nTout is = ' + str(self.Tout - 273.15) + "\n deltaT = " + str(self.Tin - self.Tout))
            self.Qdot = self.mdot * self.g.C_p * (self.Tin - self.Tout)
            # print('Qdot = ' + str(self.mdot * g.C_p * 1000 * (self.Tout - self.Tin)))
            # print('delta P  = ' + str(P))

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
        deltaTm = ((self.T_air - tout) - (self.T_air - self.Tin)) / math.log((self.T_air - tout)/(self.T_air - self.Tin))

        return ((self.mdot * self.g.C_p * 1000) * ((tout - self.Tin) / deltaTm)) / (math.pi * self.ID * self.pipeLength) \
               - self.h_Total

    def calcul(self, pipelength, ID, OD):
        self.pipeLength = pipelength
        self.ID = ID
        self.OD = OD
        print('pipeLength, ID, OD', self.pipeLength, self.ID, self.OD)
        self.__init__(self.P, self.Tin)



if __name__ == "__main__":
    g = Gas()
    R = PipeLineEnd(10 + 273.15, 20, 5 + 273.15, 5000, g, 0.4, 0.38, 20, 10000)
    print(R.Tout-273.15)

    # R.calcul(50, 0.5, 0.7)
