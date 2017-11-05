

class CapacityCalculation:

    def __init__(self):
        pass

    def gasConsumptionCal(self, Pin, Tin, Pout, Tout, g, HHV, debi):
        g.calculate(Pin, Tin)
        H1 = g.H
        g.calculate(Pout, Tout)
        H2 = g.H
        gasConsumption = self.capacityCal(Pin,
                                                   Tin,
                                                   g,
                                                   H1,
                                                   H2,
                                                   HHV,
                                                   debi)
        return gasConsumption

    def capacityCal(self, P, T, g, H1, H2, HHV, Q_standard):
        g.calculate(g.p_theta, g.T_theta)
        P2 = g.P
        Z2 = g.Z
        T2 = g.T
        Dstd = g.D
        g.calculate(P, T)
        P1 = g.P
        Z1 = g.Z
        T1 = g.T

        Qdot = (Q_standard / 3600) * (P2 * Z1 * T1) / (P1 * Z2 * T2)
        # Q1Heater = Qdot * g.D * (H2 - H1) / HHV * 3600
        Q1Heater = Qdot * g.D * (H2 - H1) / HHV * 3600
        Q1Heater = Q1Heater / Dstd
        return Q1Heater