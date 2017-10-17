from AgaQt import Gas
from scipy.optimize import fsolve


class Regulator():

    def __init__(self, Pin, Tout, Pout, g):
        self.Pin = Pin
        self.Tout = Tout
        self.Pout = Pout
        self.g = g



        muuu = 1000
        self.g.mu = 1
        # print("T out staion " + str(ui.toutStation) + " \n" + "P out Station " + str(ui.poutStation) + "\n P in " + str(
        #     ui.Pin) + "\nTin = " + str(ui.Tin))
        while abs((muuu - self.g.mu) / self.g.mu) > 10e-7:
            self.Tin = fsolve(self.joultompson, 2)
            muuu = (self.Tout - self.Tin) / (self.Pout - self.Pin) * 1000
            self.g.calculate(self.Pin, self.Tin)

        # self.tBeforeRegulator = T2
    # print('it might be first')


    def joultompson(self, T2):
        return ((self.Tout - T2) / (self.Pout - self.Pin) * 1000 - self.g.mu)

if __name__ == "__main__":
    g = Gas()
    R = Regulator(7000, 288, 2000, g)
    print(R.Tin-273.15)