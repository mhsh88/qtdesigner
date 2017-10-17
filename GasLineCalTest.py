import sys
import math
# sys.path.append('D:\\hossein sharifi 96-01-19\\behinesazan\\narmafzar\\myqtdesigner\\AgaQt')
# sys.path.append('C:\\Users\\Hossein\\Desktop\\myqtdesigner\\96-02-20\\GasStationSoftware\\myqtdesigner\\AgaQt')
from AgaQt import Gas
from math import exp
from scipy.optimize import fsolve



class Reynolds():
    ID = 0.4
    OD = 0.5
    pipeLength = 20
    Tin = 5
    T_air = 20

    def __init__(self, P , Tin):
        self.P = P
        self.Tin = Tin

        print('pipeLength, ID, OD ---> after init', self.pipeLength, self.ID, self.OD)

        g = Gas()
        g.P = P
        g.calculate(g.P, 273.15 + Tin)
        g2 = Gas()
        g2.calculate(g2.p_theta, g2.T_theta)
        Qdot = (100000/3600) * (g2.P * g.Z * g.T)/(g.P * g2.Z * g2.T)

        A = math.pi * self.ID * self.ID / 4
        V = Qdot/A
        # print('\nV is = ' + str(V))

        self.g = g

        mdot = Qdot * g.rou
        self.mdot = mdot
        # print('mdot is = ' + str(math.fsum(mdot)))


        rou = g.rou * 0.001
        T = g.T * 1.8
        Mg = g.M
        X = 3.5 + 986 / T + 0.01 * Mg
        Y = 2.4 - 0.2 * X
        K = ((9.4 + 0.02 * Mg) * T ** 1.5) / (209 + 19 * Mg + T)
        mu = (K * 10 ** -4) * exp(X * rou ** Y)

        self.R = g.rou * V * self.ID / (mu * 0.001)
        # print('rou, V, mu', g.rou, V, mu)


        LtoDratio = self.pipeLength / self.ID


        k_gas = 0.05

        Pr = g.C_p * mu / k_gas  # [mu] --> cp, [C_p] --> kJ/kg.K, [k_gas (thermal conductivity)] --> W/m.K
        x = 1000
        GzD = self.R * Pr / (x / self.ID)
        # print('Prandtl = ' + str(math.fsum(Pr)), '\nGzD^-1 = ' + str(math.fsum(1 / GzD)))

        # entrance region
        if Pr > 0.1:
            Nu = 4.36
        h = k_gas * Nu / self.ID
        # print('h gas with Nu (4.36) is = ' + str(h))
        # Tin = self.Tin


        v_air = 5
        hair = 10.45 - v_air + 10 * v_air ** (1 / 2)
        # hair = 0.06
        gamma = g.M / 28.966
        # print(gamma)
        k_steel = 52  # thermal conductivity of steel is 45 W/m.K
        q_ = (self.T_air - Tin) / (1/hair + 1/h + ((self.OD - self.ID) / math.log(self.OD / self.ID)) / k_steel)
        Q = q_ * self.OD * math.pi * self.pipeLength
        # print('Qflux is = ' + str(q_), '\nQ  = ' + str(Q))

        deltaTpipe = Q / (mdot * g.C_p * 1000)
        # print('deltaT is = ' + str(math.fsum(deltaTpipe)))


        # print('Re * Pr = ' + str(math.fsum(Pr * self.R)))
        # print('Reynolds is = ' + str(math.fsum(self.R)))







        # self.m = 0
        friction = fsolve(self.friction, -7)
        friction = math.fabs(friction)
        deltaP = friction * g.rou * (V**2 / (2*self.ID)) * self.pipeLength
        P = deltaP * Qdot


        ##
        Nu = ((friction / 8) * (self.R - 1000) * Pr) / (1 + 12.7 * ((friction / 8) ** 0.5) * (Pr ** (2/3) - 1))
        h_gas = Nu * k_gas/self.ID
        # print("h gas = " + str(math.fsum(h_gas)))
        # print('Nu is = ' + str(math.fsum(Nu)))


        self.h_Total = (1 / hair + 1 / h_gas + ((self.OD - self.ID) / math.log(self.OD / self.ID)) / k_steel)
        # print('H_total is = ' + str(self.h_Total))
        #
        Tm_o = fsolve(self.tOutCal, Tin + 1)
        # print("till hear!!!")


        q_ = (self.T_air - self.Tin) / (1/hair + 1/h_gas + ((self.OD - self.ID) / math.log(self.OD / self.ID)) / k_steel)
        Q = q_ * self.OD * math.pi * self.pipeLength
        # print('Qflux is = ' + str(q_), '\nQ  = ' + str(Q))

        deltaTpipe = Q / (mdot * g.C_p * 1000)
        # print('deltaT is = ' + str(math.fsum(deltaTpipe)))


        ##
        Nu = 4.82 + 0.0185 * (self.R * Pr) ** 0.827

        h_gas = Nu * k_gas / self.ID
        # print("h gas = " + str(math.fsum(h_gas)))
        # print('Nu is = ' + str(math.fsum(Nu)))

        q_ = (self.T_air - Tin) / (1 / hair + 1 / h_gas + ((self.OD - self.ID) / math.log(self.OD / self.ID)) / k_steel)
        Q = q_ * self.OD * math.pi * self.pipeLength
        # print('Qflux is = ' + str(q_), '\nQ  = ' + str(Q))

        deltaTpipe = Q / (mdot * g.C_p * 1000)
        # print('deltaT is = ' + str(math.fsum(deltaTpipe)))

        self.h_Total = 1 / (1 / hair + 1 / h_gas + ((self.OD - self.ID) / math.log(self.OD / self.ID)) / k_steel)
        # print('H_total is = ' + str(self.h_Total))

        # Tm_o = fsolve(self.tOutCal, Tin + 1)
        # print("till hear!!!")
        #
        # print('new one')
        # print('h_total is = ' + str(self.h_Total))
        self.Tout = (self.Tin - self.T_air) * exp(-math.pi*self.ID * self.pipeLength * self.h_Total / (self.mdot * g.C_p * 1000)) + self.T_air
        print('Tout is = ' + str(self.Tout))
        print('Qdot = ' + str(self.mdot * g.C_p * 1000 * (self.Tout - self.Tin)))




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
    R = Reynolds(5000, 5)
    R.calcul(50, 0.5, 0.7)
